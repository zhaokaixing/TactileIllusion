import socket
import cv2
import threading
import tkinter as tk
import numpy as np
from illusion.four_tactors_tactile_brush import generate_tactile_brush_results
from illusion.four_tactors_tactile_brush import generate_SOA
from ardui.arduino_connect import generate_atm_arduino_without_single_vibration
import _thread
from ardui.arduino_connect import generate_single_vibration_arduino

str_x_global = 0.0
str_y_global = 0.0
shape_path = ''
int_direction = 0
flag_list = []


def traverse_list(list):
    for i in list:
        if (i != 0) and (not ( i is None)):
            return i


def compare_pixel_atm(rec_x, rec_y, flag):
    global flag_list
    flag_list.append(flag)

    img = cv2.imread(shape_path)
    height, width = img.shape[:2]
    img_resize = cv2.resize(img, (int(width / 3), int(height / 3)))
    height_resize, width_resize = img_resize.shape[:2]

    x, y = convert_coord(rec_x, rec_y, height_resize, width_resize)
    x_final = round(x)
    y_final = round(y)
    color_pixel = img_resize[y_final][x_final]

    global int_direction
    if shape_path == './shapeandroid/horizontalMobile.png':
        horizontal_arr = [0, 0, 255]
        np_horizontal_arr = np.array(horizontal_arr)
        #print('66666666666666666666666')
        #print(traverse_list(flag_list))
        initial_direction = traverse_list(flag_list)

        if x_final < width_resize/2 and (color_pixel == np_horizontal_arr).all():
            if flag_list[-1] == 0:
                if initial_direction == 1:
                    int_direction = 1
                else:
                    int_direction = -1
            if flag_list[-1] == 1:
                int_direction = 1
        elif x_final >= width_resize/2 and (color_pixel == np_horizontal_arr).all():
            if flag_list[-1] == 0:
                if initial_direction == -1:
                    int_direction = -1
                else:
                    int_direction = 1
            if flag_list[-1] == -1:
                int_direction = -1

        else:
            int_direction = 0

        if flag != int_direction:
            start_atm(int_direction)
            flag = int_direction

        '''horizontal_arr = [0, 0, 255]
        np_horizontal_arr = np.array(horizontal_arr)

        if x_final < width_resize / 2 and (color_pixel == np_horizontal_arr).all():
            if flag_list[-1] == 0:
                int_direction = -1
                if flag != int_direction:
                    start_atm_duration(int_direction, 500)
                    flag = int_direction
            if flag_list[-1] == 1:
                int_direction = -1
                if flag != int_direction:
                    start_atm_duration(-int_direction, 300)
                    flag = int_direction
        elif x_final >= width_resize / 2 and (color_pixel == np_horizontal_arr).all():
            if flag_list[-1] == 0:
                int_direction = 1
                if flag != int_direction:
                    start_atm_duration(int_direction, 500)
                    flag = int_direction
            if flag_list[-1] == -1:
                int_direction = 1
                if flag != int_direction:
                    start_atm_duration(-int_direction, 300)
                    flag = int_direction
        else:
            int_direction = 0
        if flag != int_direction:
                start_atm(int_direction)
                flag = int_direction'''


    elif shape_path == './shapeandroid/squareMobile.png':
        horizontal_arr_top = [0, 1, 255]
        np_horizontal_arr_top = np.array(horizontal_arr_top)
        horizontal_arr_bottom = [0, 0, 255]
        np_horizontal_arr_bottom = np.array(horizontal_arr_bottom)
        vertical_arr_left = [0, 255, 1]
        np_vertical_arr_left = np.array(vertical_arr_left)
        vertical_arr_right = [0, 255, 0]
        np_vertical_arr_right = np.array(vertical_arr_right)

        rec_point_1 = [0, 0, 0]
        np_rec_point_1 = np.array(rec_point_1)
        rec_point_2 = [0, 0, 100]
        np_rec_point_2 = np.array(rec_point_2)
        rec_point_3 = [0, 0, 200]
        np_rec_point_3 = np.array(rec_point_3)
        rec_point_4 = [0, 200, 200]
        np_rec_point_4 = np.array(rec_point_4)

        if (color_pixel == np_horizontal_arr_top).all():
            int_direction = -1
        elif (color_pixel == np_horizontal_arr_bottom).all():
            int_direction = 1
        elif (color_pixel == np_vertical_arr_left).all():
            int_direction = 2
        elif (color_pixel == np_vertical_arr_right).all():
            int_direction = -2
        elif (color_pixel == np_rec_point_1).all():
            int_direction = -1
        elif (color_pixel == np_rec_point_2).all():
            int_direction = -2
        elif (color_pixel == np_rec_point_3).all():
            int_direction = 1
        elif (color_pixel == np_rec_point_4).all():
            int_direction = 2
        else:
            int_direction = 0
        if flag != int_direction:
            start_atm(int_direction)
            flag = int_direction

    return flag


def start_atm_duration(int_direction, duration):
    distance = 20
    no_direction = int_direction
    phantom_res_list, vib_duration = generate_tactile_brush_results(0.7, distance, duration)
    start_vib_list = []
    end_vib_list = []
    temp_start_x = 0
    temp_start_y = 0
    temp_end_x = 0
    temp_end_y = 0

    if no_direction == 1:
        temp_start_x = distance
        temp_start_y = distance
        temp_end_x = 0
        temp_end_y = distance
    elif no_direction == 2:
        temp_start_x = 0
        temp_start_y = 0
        temp_end_x = 0
        temp_end_y = distance
    elif no_direction == -1:
        temp_start_x = 0
        temp_start_y = distance
        temp_end_x = distance
        temp_end_y = distance
    elif no_direction == -2:
        temp_start_x = 0
        temp_start_y = distance
        temp_end_x = 0
        temp_end_y = 0
    elif no_direction == 3:
        temp_start_x = 0
        temp_start_y = 0
        temp_end_x = distance
        temp_end_y = distance
    elif no_direction == -3:
        temp_start_x = distance
        temp_start_y = distance
        temp_end_x = 0
        temp_end_y = 0
    elif no_direction == 4:
        temp_start_x = 0
        temp_start_y = distance
        temp_end_x = distance
        temp_end_y = 0
    elif no_direction == -4:
        temp_start_x = distance
        temp_start_y = 0
        temp_end_x = 0
        temp_end_y = distance

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

        time_SOA = generate_SOA(duration, vib_duration)
        try:
            _thread.start_new_thread(generate_atm_arduino_without_single_vibration, (start_vib_list, end_vib_list, time_SOA))
        except:
            print('Infrared ATM error')

        print('Start Vib List: ')
        print(start_vib_list)
        print('End Vib List: ')
        print(end_vib_list)


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
        temp_start_x = distance
        temp_start_y = distance
        temp_end_x = 0
        temp_end_y = distance
    elif no_direction == 2:
        temp_start_x = 0
        temp_start_y = 0
        temp_end_x = 0
        temp_end_y = distance
    elif no_direction == -1:
        temp_start_x = 0
        temp_start_y = distance
        temp_end_x = distance
        temp_end_y = distance
    elif no_direction == -2:
        temp_start_x = 0
        temp_start_y = distance
        temp_end_x = 0
        temp_end_y = 0
    elif no_direction == 3:
        temp_start_x = 0
        temp_start_y = 0
        temp_end_x = distance
        temp_end_y = distance
    elif no_direction == -3:
        temp_start_x = distance
        temp_start_y = distance
        temp_end_x = 0
        temp_end_y = 0
    elif no_direction == 4:
        temp_start_x = 0
        temp_start_y = distance
        temp_end_x = distance
        temp_end_y = 0
    elif no_direction == -4:
        temp_start_x = distance
        temp_start_y = 0
        temp_end_x = 0
        temp_end_y = distance

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
            _thread.start_new_thread(generate_atm_arduino_without_single_vibration, (start_vib_list, end_vib_list, time_SOA))
        except:
            print('Infrared ATM error')

        print('Start Vib List: ')
        print(start_vib_list)
        print('End Vib List: ')
        print(end_vib_list)


def receive_from_android():
    BUFSIZE = 4096
    tcpServerSocket = socket.socket()
    hostname = socket.gethostname()
    sysinfo = socket.gethostbyname_ex(hostname)
    hostip = sysinfo[2][0]
    port = 19000
    tcpServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpServerSocket.bind((hostip, port))
    tcpServerSocket.listen(5)

    global str_x_global
    global str_y_global
    flag_direction = 0

    while True:
        clientSocket, addr = tcpServerSocket.accept()
        while True:
            data = clientSocket.recv(BUFSIZE).decode()
            if not data:
                break
            data_arr_str = data.split(' ')
            str_x_global = float(data_arr_str[0])
            str_y_global = float(data_arr_str[1])
            if str_x_global >= 0 and str_y_global >= 0:
                flag_get = compare_pixel_atm(str_x_global, str_y_global, flag_direction)
                flag_direction = flag_get

        clientSocket.close()
        #tcpServerSocket.close()

def convert_coord(x_origin, y_origin, image_height, image_width):
    x = image_width * x_origin
    y = image_height * y_origin
    return x, y

def image_ui():
    root = tk.Tk()
    root.minsize(800, 600)
    root.maxsize(800, 600)
    root.title('Simple Shape Perception Using Tactile Illusions by Android')
    main_frame = tk.Frame(root, bg='white')
    main_frame.pack(fill=tk.X)

    v_shape = tk.IntVar()
    label_shape_text = tk.Label(main_frame, text='Shape', bg='white').grid(row=0, column=0)
    tk.Radiobutton(main_frame, text='Horizontal', variable=v_shape, value=1, bg='white').grid(row=0, column=1, ipadx=25)
    tk.Radiobutton(main_frame, text='Vertical', variable=v_shape, value=2, bg='white').grid(row=0, column=2, ipadx=25)
    tk.Radiobutton(main_frame, text='Slash', variable=v_shape, value=3, bg='white').grid(row=0, column=3, ipadx=25)
    tk.Radiobutton(main_frame, text='Backslash', variable=v_shape, value=4, bg='white').grid(row=0, column=4, ipadx=25)
    tk.Radiobutton(main_frame, text='ZigZag', variable=v_shape, value=6, bg='white').grid(row=0, column=6, ipadx=25)

    tk.Radiobutton(main_frame, text='Square', variable=v_shape, value=7, bg='white').grid(row=2, column=1, ipadx=25)
    tk.Radiobutton(main_frame, text='Rectangle', variable=v_shape, value=8, bg='white').grid(row=2, column=2, ipadx=25)
    tk.Radiobutton(main_frame, text='Triangle', variable=v_shape, value=9, bg='white').grid(row=2, column=3, ipadx=25)

    def choose_shape_click():
        no_shape = v_shape.get()
        global shape_path
        global str_x_global, str_y_global
        global int_direction
        global flag_list
        if no_shape == 1:
            shape_path = './shapeandroid/horizontalMobile.png'
        elif no_shape == 2:
            shape_path = './shapeandroid/verticalMobile.png'
        elif no_shape == 3:
            shape_path = './shapeandroid/slashMobile.png'
        elif no_shape == 4:
            shape_path = './shapeandroid/backslashMobile.png'
        elif no_shape == 6:
            shape_path = './shapeandroid/zigzagMobile.png'
        elif no_shape == 7:
            shape_path = './shapeandroid/squareMobile.png'
        elif no_shape == 8:
            shape_path = './shapeandroid/rectangleMobile.png'
        elif no_shape == 9:
            shape_path = './shapeandroid/triangleMobile.png'

        img = cv2.imread(shape_path)
        height, width = img.shape[:2]
        img_resize = cv2.resize(img, ((int)(width / 3), (int)(height / 3)))
        height_resize, width_resize = img_resize.shape[:2]

        while True:
            cv2.imshow('image', img_resize)
            key = cv2.waitKey(1)
            x, y = convert_coord(str_x_global, str_y_global, height_resize, width_resize)
            x_final = round(x)
            y_final = round(y)
            if x_final != 0 and y_final != 0:
                cv2.circle(img_resize, (x_final, y_final), 5, (0, 0, 0), -1)
            if key == 27:
                cv2.destroyAllWindows()
                str_x_global = 0.0
                str_y_global = 0.0
                shape_path = ''
                int_direction = 0
                flag_list = []
                return 0

    button_frame = tk.Frame(root, bg='white')
    button_frame.pack(fill=tk.X)
    btn_shape = tk.Button(button_frame, text='Choose Shape', command=choose_shape_click, width=42, height=5, bg='green')
    btn_shape.pack()

    root.mainloop()

def main_process():
    threads = []
    t1 = threading.Thread(target=receive_from_android)
    threads.append(t1)
    t2 = threading.Thread(target=image_ui)
    threads.append(t2)
    for t in threads:
        t.start()
    for t in threads:
        t.join()

main_process()