import tkinter as tk
import socket
import threading
import cv2
from matplotlib import pyplot as plt
import numpy as np
from illusion.four_tactors_tactile_brush import generate_tactile_brush_results
from illusion.four_tactors_tactile_brush import generate_SOA
from ardui.arduino_connect import generate_atm_arduino
import _thread
'''
Author: Kaixing ZHAO
This file is the user interface which can be used to choose different directional images and test the users' ability 
to follow a path with only apparent tactile motion
'''

'''Global variables to record x, y positions and the image path'''
str_x_global = 0.0
str_y_global = 0.0
shape_path = ''

'''Function to update the global variables with the finger position changes'''
def set_coor_global(x, y):
    global str_x_global
    global str_y_global
    str_x_global = x
    str_y_global = y
    #print(str_x_global, str_y_global)

'''Function to compare current pixel color with designed colors to determine the direction'''
def compare_pixel(rec_x, rec_y, flag):
    #print(shape_path)
    img = cv2.imread(shape_path)
    height, width = img.shape[:2]
    x, y = convert_coord(rec_x, rec_y, height, width)
    x_final = round(x)
    y_final = round(y)
    color_pixel = img[y_final][x_final]
    #print(color_pixel)

    horizontal_arr = [255, 0, 0]
    np_horizontal_arr = np.array(horizontal_arr)
    vertical_arr = [0, 255, 0]
    np_vertical_arr = np.array(vertical_arr)
    slash_arr = [0, 0, 255]
    np_slash_arr = np.array(slash_arr)
    backslash_arr = [255, 255, 0]
    np_backslash_arr = np.array(backslash_arr)

    if (color_pixel == np_horizontal_arr).all():
        int_direction = 1
    elif (color_pixel == np_vertical_arr).all():
        int_direction = 2
    elif (color_pixel == np_slash_arr).all():
        int_direction = 3
    elif (color_pixel == np_backslash_arr).all():
        int_direction = 4
    else:
        int_direction = 0

    if flag != int_direction:
        flag = int_direction
        print(int_direction)
        start_atm(int_direction)

    return flag

'''Function to control Arduino and launch the Apparent Tactile Motion according to direction'''
def start_atm(int_direction):
    distance = 20
    no_direction = int_direction
    phantom_res_list, vib_duration = generate_tactile_brush_results(1.0, distance, 500)
    start_vib_list = []
    end_vib_list = []
    temp_start_x = 0
    temp_start_y = 0
    temp_end_x = 0
    temp_end_y = 0

    if no_direction == 1:
        temp_start_x = 0
        temp_start_y = 0
        temp_end_x = distance
        temp_end_y = 0
    elif no_direction == 2:
        temp_start_x = 0
        temp_start_y = 0
        temp_end_x = 0
        temp_end_y = distance
    elif no_direction == 3:
        temp_start_x = 0
        temp_start_y = 0
        temp_end_x = distance
        temp_end_y = distance
    elif no_direction == 4:
        temp_start_x = 0
        temp_start_y = distance
        temp_end_x = distance
        temp_end_y = 0

    if no_direction != 0:
        for phantom_item in phantom_res_list:
            if temp_start_x == phantom_item[0] and temp_start_y == phantom_item[1]:
                start_vib_list.append(temp_start_x)
                start_vib_list.append(temp_start_y)
                start_vib_list.append(phantom_item[2])
                start_vib_list.append(phantom_item[3])
                start_vib_list.append(phantom_item[4])
                start_vib_list.append(phantom_item[5])
        start_vib_list.append(vib_duration)
        for phantom_item_end in phantom_res_list:
            if temp_end_x == phantom_item_end[0] and temp_end_y == phantom_item_end[1]:
                end_vib_list.append(temp_end_x)
                end_vib_list.append(temp_end_y)
                end_vib_list.append(phantom_item_end[2])
                end_vib_list.append(phantom_item_end[3])
                end_vib_list.append(phantom_item_end[4])
                end_vib_list.append(phantom_item_end[5])
        end_vib_list.append(vib_duration)

        time_SOA = generate_SOA(500, vib_duration)
        try:
            _thread.start_new_thread(generate_atm_arduino, (start_vib_list, end_vib_list, time_SOA))
            # _thread.start_new_thread(generate_atm_arduino, (end_vib_list, start_vib_list, time_SOA))
        except:
            print('Infrared ATM error')

        print('Start Vib List: ')
        print(start_vib_list)
        print('End Vib List: ')
        print(end_vib_list)

'''Function to listen to the socket port and receive the real time position data'''
def receive_from_infra():
    HOST = '127.0.0.1'
    PORT = 19000
    BUFSIZE = 1024
    ADDR = (HOST, PORT)
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(ADDR)
    serversocket.listen(5)

    while True:
        flag_direction = 0
        clientsocket, addr = serversocket.accept()
        while 1:
            data = clientsocket.recv(BUFSIZE)
            rec_data_str = data.decode('utf-8')
            data_arr = rec_data_str.split(':')
            if len(data_arr) > 2 and data_arr[0] == '1':
                x_float = float(data_arr[1])
                y_float = float(data_arr[2])
                if x_float > 0 and y_float > 0:
                    set_coor_global(x_float, y_float)
                    flag_get = compare_pixel(x_float, y_float, flag_direction)
                    flag_direction = flag_get

        clientsocket.close()

'''Function to convert initial received data to real image scale positions'''
def convert_coord(x_origin, y_origin, image_height, image_width):
    x = image_width * x_origin
    y = image_height * y_origin
    return x, y

'''Function of the UI, could draw position in real time'''
def simple_shape_interface():
    root = tk.Tk()
    root.minsize(800, 600)
    root.maxsize(800, 600)
    root.title('Simple Shape Perception Using Tactile Illusions')
    main_frame = tk.Frame(root, bg='white')
    main_frame.pack(fill=tk.X)

    v_shape = tk.IntVar()
    label_shape_text = tk.Label(main_frame, text='Shape', bg='white').grid(row=0, column=0)
    tk.Radiobutton(main_frame, text='Horizontal', variable=v_shape, value=1, bg='white').grid(row=0, column=1, ipadx=20)
    tk.Radiobutton(main_frame, text='Vertical', variable=v_shape, value=2, bg='white').grid(row=0, column=2, ipadx=20)
    tk.Radiobutton(main_frame, text='Slash', variable=v_shape, value=3, bg='white').grid(row=0, column=3, ipadx=20)
    tk.Radiobutton(main_frame, text='Backslash', variable=v_shape, value=4, bg='white').grid(row=0, column=4, ipadx=20)
    def choose_shape_click():
        no_shape = v_shape.get()
        global shape_path
        if no_shape == 1:
            shape_path = 'horizontal.png'
        elif no_shape == 2:
            shape_path = 'vertical.png'
        elif no_shape == 3:
            shape_path = 'slash.png'
        elif no_shape == 4:
            shape_path = 'backslash.png'

        img = cv2.imread(shape_path)
        '''img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(img)
        plt.show()'''
        height, width = img.shape[:2]

        while True:
            cv2.imshow('image', img)
            key = cv2.waitKey(1)
            x, y = convert_coord(str_x_global, str_y_global, height, width)
            x_final = round(x)
            y_final = round(y)
            cv2.circle(img, (x_final, y_final), 5, (0, 0, 0), -1)
            if key == 27:
                cv2.destroyAllWindows()
                return 0

    btn_shape = tk.Button(main_frame, text='Choose Shape', command=choose_shape_click, width=25)
    btn_shape.grid(row=0, column=5)

    root.mainloop()

'''Main function, call two different threads to listen socket port and draw UI respectively'''
def main_process():
    threads = []
    t1 = threading.Thread(target=receive_from_infra)
    threads.append(t1)
    t2 = threading.Thread(target=simple_shape_interface)
    threads.append(t2)
    for t in threads:
        t.start()
    for t in threads:
        t.join()


main_process()