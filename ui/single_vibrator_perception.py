import tkinter as tk
import socket
import threading
import cv2
from matplotlib import pyplot as plt
import numpy as np
from ardui.arduino_connect import generate_single_vibration_arduino
from ardui.arduino_connect import stop_single_vibration_arduino
import _thread
'''
Author: Kaixing ZHAO
This file is used to investigate the performance of finger vibration on accessing simple shapes and graphics
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

'''Function to compare current pixel color with designed colors to control the vibration'''
def compare_pixel(rec_x, rec_y):
    img = cv2.imread(shape_path)
    height, width = img.shape[:2]
    x, y = convert_coord(rec_x, rec_y, height, width)
    x_final = round(x)
    y_final = round(y)
    color_pixel = img[y_final][x_final]

    vib_arr = [0, 0, 0]
    np_vib_arr = np.array(vib_arr)
    if (color_pixel == np_vib_arr).all():
        try:
            _thread.start_new_thread(generate_single_vibration_arduino, (1,))
        except:
            print('Infrared Single Vibration error')
    else:
        try:
            _thread.start_new_thread(stop_single_vibration_arduino, ())
        except:
            print('Infrared Single Vibration error')

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
                    compare_pixel(x_float, y_float)
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
    tk.Radiobutton(main_frame, text='Horizontal', variable=v_shape, value=1, bg='white').grid(row=0, column=1, ipadx=25)
    tk.Radiobutton(main_frame, text='Vertical', variable=v_shape, value=2, bg='white').grid(row=0, column=2, ipadx=25)
    tk.Radiobutton(main_frame, text='Slash', variable=v_shape, value=3, bg='white').grid(row=0, column=3, ipadx=25)
    tk.Radiobutton(main_frame, text='Backslash', variable=v_shape, value=4, bg='white').grid(row=0, column=4, ipadx=25)
    tk.Radiobutton(main_frame, text='Curve', variable=v_shape, value=5, bg='white').grid(row=0, column=5, ipadx=25)
    tk.Radiobutton(main_frame, text='ZigZag', variable=v_shape, value=6, bg='white').grid(row=0, column=6, ipadx=25)

    tk.Radiobutton(main_frame, text='Square', variable=v_shape, value=7, bg='white').grid(row=2, column=1, ipadx=25)
    tk.Radiobutton(main_frame, text='Rectangle', variable=v_shape, value=8, bg='white').grid(row=2, column=2, ipadx=25)
    tk.Radiobutton(main_frame, text='Triangle', variable=v_shape, value=9, bg='white').grid(row=2, column=3, ipadx=25)
    tk.Radiobutton(main_frame, text='Circle', variable=v_shape, value=10, bg='white').grid(row=2, column=4, ipadx=25)
    def choose_shape_click():
        no_shape = v_shape.get()
        global shape_path
        if no_shape == 1:
            shape_path = './shapes/HorizontalLineBlack.png'
        elif no_shape == 2:
            shape_path = './shapes/VerticalLineBlack.png'
        elif no_shape == 3:
            shape_path = './shapes/SlashLineBlack.png'
        elif no_shape == 4:
            shape_path = './shapes/BackslashLineBlack.png'
        elif no_shape == 5:
            shape_path = './shapes/CurveLineBlack.png'
        elif no_shape == 6:
            shape_path = './shapes/ZigLineBlack.png'
        elif no_shape == 7:
            shape_path = './shapes/SquareBlack.png'
        elif no_shape == 8:
            shape_path = './shapes/RectangleBlack.png'
        elif no_shape == 9:
            shape_path = './shapes/TriangleBlack.png'
        elif no_shape == 10:
            shape_path = './shapes/CircleBlack.png'

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

    button_frame = tk.Frame(root, bg='white')
    button_frame.pack(fill=tk.X)
    btn_shape = tk.Button(button_frame, text='Choose Shape', command=choose_shape_click, width=42, height=5, bg='green')
    btn_shape.pack()

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