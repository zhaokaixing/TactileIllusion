import socket
import cv2
import threading
import tkinter as tk
import numpy as np
#from illusion.four_tactors_tactile_brush import generate_tactile_brush_results
#from illusion.four_tactors_tactile_brush import generate_SOA
#from ardui.arduino_connect import generate_atm_arduino_without_single_vibration
import _thread
from ardui.arduino_connect import generate_single_vibration_arduino
from ardui.arduino_connect import stop_single_vibration_arduino

str_x_global = 0.0
str_y_global = 0.0
shape_path = ''
int_direction = 0
flag_list = []


def traverse_list(list):
    for i in list:
        if (i != 0) and (not ( i is None)):
            return i


def convert_coord(x_origin, y_origin, image_height, image_width):
    x = image_width * x_origin
    y = image_height * y_origin
    return x, y


def compare_pixel_normal(rec_x, rec_y):
    img = cv2.imread(shape_path)
    height, width = img.shape[:2]
    img_resize = cv2.resize(img, (int(width / 3), int(height / 3)))
    height_resize, width_resize = img_resize.shape[:2]

    x, y = convert_coord(rec_x, rec_y, height_resize, width_resize)
    x_final = round(x)
    y_final = round(y)
    color_pixel = img_resize[y_final][x_final]

    horizontal_arr = [0, 0, 255]
    np_horizontal_arr = np.array(horizontal_arr)

    if (color_pixel == np_horizontal_arr).all():
        try:
            _thread.start_new_thread(generate_single_vibration_arduino, (0.75,))
        except:
            print('Infrared Single Vibration error')
    else:
        try:
            _thread.start_new_thread(stop_single_vibration_arduino, ())
        except:
            print('Infrared Single Vibration error')


def compare_pixel_two_classes(rec_x, rec_y, flag):
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
    if shape_path == '../ui/shapeandroid/horizontalMobile.png':
        horizontal_arr = [0, 0, 255]
        np_horizontal_arr = np.array(horizontal_arr)
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

        if initial_direction == -1:
            if x_final < width_resize * 0.75 and (color_pixel == np_horizontal_arr).all():
                try:
                    _thread.start_new_thread(generate_single_vibration_arduino, (0.4,))
                except:
                    print('Infrared Single Vibration error')
            elif x_final >= width_resize * 0.75 and (color_pixel == np_horizontal_arr).all():
                try:
                    _thread.start_new_thread(generate_single_vibration_arduino, (0.75,))
                except:
                    print('Infrared Single Vibration error')
            else:
                try:
                    _thread.start_new_thread(stop_single_vibration_arduino, ())
                except:
                    print('Infrared Single Vibration error')
        elif initial_direction == 1:
            if x_final >= width_resize * 0.25 and (color_pixel == np_horizontal_arr).all():
                try:
                    _thread.start_new_thread(generate_single_vibration_arduino, (0.4,))
                except:
                    print('Infrared Single Vibration error')
            elif x_final < width_resize * 0.25 and (color_pixel == np_horizontal_arr).all():
                try:
                    _thread.start_new_thread(generate_single_vibration_arduino, (0.75,))
                except:
                    print('Infrared Single Vibration error')
            else:
                try:
                    _thread.start_new_thread(stop_single_vibration_arduino, ())
                except:
                    print('Infrared Single Vibration error')

        if flag != int_direction:
            flag = int_direction
        return flag


def compare_pixel_continuous(rec_x, rec_y, flag):
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
    if shape_path == '../ui/shapeandroid/horizontalMobile.png':
        horizontal_arr = [0, 0, 255]
        np_horizontal_arr = np.array(horizontal_arr)
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

        if initial_direction == -1:
            if x_final < width_resize * 0.2 and (color_pixel == np_horizontal_arr).all():
                try:
                    _thread.start_new_thread(generate_single_vibration_arduino, (0.25,))
                except:
                    print('Infrared Single Vibration error')
            elif x_final >= width_resize * 0.2 and x_final < width_resize * 0.4 and (color_pixel == np_horizontal_arr).all():
                try:
                    _thread.start_new_thread(generate_single_vibration_arduino, (0.35,))
                except:
                    print('Infrared Single Vibration error')
            elif x_final >= width_resize * 0.4 and x_final < width_resize * 0.6 and (color_pixel == np_horizontal_arr).all():
                try:
                    _thread.start_new_thread(generate_single_vibration_arduino, (0.45,))
                except:
                    print('Infrared Single Vibration error')
            elif x_final >= width_resize * 0.6 and x_final < width_resize * 0.8 and (color_pixel == np_horizontal_arr).all():
                try:
                    _thread.start_new_thread(generate_single_vibration_arduino, (0.55,))
                except:
                    print('Infrared Single Vibration error')
            elif x_final >= width_resize * 0.8 and (color_pixel == np_horizontal_arr).all():
                try:
                    _thread.start_new_thread(generate_single_vibration_arduino, (0.75,))
                except:
                    print('Infrared Single Vibration error')
            else:
                try:
                    _thread.start_new_thread(stop_single_vibration_arduino, ())
                except:
                    print('Infrared Single Vibration error')
        elif initial_direction == 1:
            if x_final >= width_resize * 0.25 and (color_pixel == np_horizontal_arr).all():
                try:
                    _thread.start_new_thread(generate_single_vibration_arduino, (0.4,))
                except:
                    print('Infrared Single Vibration error')
            elif x_final < width_resize * 0.25 and (color_pixel == np_horizontal_arr).all():
                try:
                    _thread.start_new_thread(generate_single_vibration_arduino, (0.75,))
                except:
                    print('Infrared Single Vibration error')
            else:
                try:
                    _thread.start_new_thread(stop_single_vibration_arduino, ())
                except:
                    print('Infrared Single Vibration error')

        if flag != int_direction:
            flag = int_direction
        return flag


def receive_from_android():
    def start_android_distance_vib(no_type):
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
            if no_type == 1:
                while True:
                    data = clientSocket.recv(BUFSIZE).decode()
                    if not data:
                        break
                    data_arr_str = data.split(' ')
                    str_x_global = float(data_arr_str[0])
                    str_y_global = float(data_arr_str[1])
                    if str_x_global >= 0 and str_y_global >= 0:
                        compare_pixel_normal(str_x_global, str_y_global)
            elif no_type == 2:
                while True:
                    data = clientSocket.recv(BUFSIZE).decode()
                    if not data:
                        break
                    data_arr_str = data.split(' ')
                    str_x_global = float(data_arr_str[0])
                    str_y_global = float(data_arr_str[1])
                    if str_x_global >= 0 and str_y_global >= 0:
                        flag_get = compare_pixel_two_classes(str_x_global, str_y_global, flag_direction)
                        flag_direction = flag_get
            elif no_type == 3:
                while True:
                    data = clientSocket.recv(BUFSIZE).decode()
                    if not data:
                        break
                    data_arr_str = data.split(' ')
                    str_x_global = float(data_arr_str[0])
                    str_y_global = float(data_arr_str[1])
                    if str_x_global >= 0 and str_y_global >= 0:
                        flag_get = compare_pixel_continuous(str_x_global, str_y_global, flag_direction)
                        flag_direction = flag_get
            clientSocket.close()
            #tcpServerSocket.close()

    print('Please input the distance type: 1: Normal, 2: Two classes, 3: Continuous')
    no_type = input()
    start_android_distance_vib(int(no_type))


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
            shape_path = '../ui/shapeandroid/horizontalMobile.png'

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