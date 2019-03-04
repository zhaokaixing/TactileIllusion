import tkinter as tk
import cv2
import socket
import threading
from ardui.arduino_connect import generate_single_vibration_arduino
from ardui.arduino_connect import stop_single_vibration_arduino
from ardui.arduino_connect import stop_all_vibration_arduino
from illusion.four_tactors_tactile_brush import generate_tactile_brush_results
from illusion.four_tactors_tactile_brush import generate_SOA
from ardui.arduino_connect import generate_atm_arduino
import _thread
import numpy as np
import time
import math

str_x_global = 0.0
str_y_global = 0.0
shape_path = ''
int_direction = 0
flag_list = []


def set_coor_global(x, y):
    global str_x_global
    global str_y_global
    str_x_global = x
    str_y_global = y

def convert_coord(x_origin, y_origin, image_height, image_width):
    x = image_width * x_origin
    y = image_height * y_origin
    return x, y

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
            _thread.start_new_thread(generate_single_vibration_arduino, ())
        except:
            print('Infrared Single Vibration error')
    else:
        try:
            _thread.start_new_thread(stop_single_vibration_arduino, ())
        except:
            print('Infrared Single Vibration error')


'''def calculate_eucli(x_1, y_1, x_2, y_2):
    return math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)'''


def compare_pixel_distance_atm(rec_x, rec_y, flag):
    global flag_list
    flag_list.append(flag)

    img = cv2.imread(shape_path)
    height, width = img.shape[:2]
    x, y = convert_coord(rec_x, rec_y, height, width)
    x_final = round(x)
    y_final = round(y)
    color_pixel = img[y_final][x_final]

    global int_direction
    if shape_path == './shapes/horizontal.png':
        horizontal_arr = [0, 0, 255]
        np_horizontal_arr = np.array(horizontal_arr)

        if x_final < width/2 and (color_pixel == np_horizontal_arr).all():
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
        elif x_final >= width/2 and (color_pixel == np_horizontal_arr).all():
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
                flag = int_direction

    elif shape_path == './shapes/vertical.png':
        vertical_arr = [0, 255, 0]
        np_vertical_arr = np.array(vertical_arr)

        if y_final < height / 2 and (color_pixel == np_vertical_arr).all():
            if flag_list[-1] == 0:
                int_direction = -2
                if flag != int_direction:
                    start_atm_duration(int_direction, 500)
                    flag = int_direction
            if flag_list[-1] == 2:
                int_direction = -2
                if flag != int_direction:
                    start_atm_duration(-int_direction, 300)
                    flag = int_direction
        elif y_final >= height / 2 and (color_pixel == np_vertical_arr).all():
            if flag_list[-1] == 0:
                int_direction = 2
                if flag != int_direction:
                    start_atm_duration(int_direction, 500)
                    flag = int_direction
            if flag_list[-1] == -2:
                int_direction = 2
                if flag != int_direction:
                    start_atm_duration(-int_direction, 300)
                    flag = int_direction
        else:
            int_direction = 0
            if flag != int_direction:
                start_atm(int_direction)
                flag = int_direction

    elif shape_path == './shapes/slash.png':
        slash_arr = [255, 0, 0]
        np_slash_arr = np.array(slash_arr)

        if x_final < width / 2 and (color_pixel == np_slash_arr).all():
            if flag_list[-1] == 0:
                int_direction = 3
                if flag != int_direction:
                    start_atm_duration(int_direction, 500)
                    flag = int_direction
            if flag_list[-1] == -3:
                int_direction = 3
                if flag != int_direction:
                    start_atm_duration(-int_direction, 300)
                    flag = int_direction
        elif x_final >= width / 2 and (color_pixel == np_slash_arr).all():
            if flag_list[-1] == 0:
                int_direction = -3
                if flag != int_direction:
                    start_atm_duration(int_direction, 500)
                    flag = int_direction
            if flag_list[-1] == 3:
                int_direction = -3
                if flag != int_direction:
                    start_atm_duration(-int_direction, 300)
                    flag = int_direction
        else:
            int_direction = 0
            if flag != int_direction:
                start_atm(int_direction)
                flag = int_direction

    elif shape_path == './shapes/backslash.png':
        backslash_arr = [0, 255, 255]
        np_backslash_arr = np.array(backslash_arr)

        if x_final < width / 2 and (color_pixel == np_backslash_arr).all():
            if flag_list[-1] == 0:
                int_direction = 4
                if flag != int_direction:
                    start_atm_duration(int_direction, 500)
                    flag = int_direction
            if flag_list[-1] == -4:
                int_direction = 4
                if flag != int_direction:
                    start_atm_duration(-int_direction, 300)
                    flag = int_direction
        elif x_final >= width / 2 and (color_pixel == np_backslash_arr).all():
            if flag_list[-1] == 0:
                int_direction = -4
                if flag != int_direction:
                    start_atm_duration(int_direction, 500)
                    flag = int_direction
            if flag_list[-1] == 4:
                int_direction = -4
                if flag != int_direction:
                    start_atm_duration(-int_direction, 300)
                    flag = int_direction
        else:
            int_direction = 0
            if flag != int_direction:
                start_atm(int_direction)
                flag = int_direction


    return flag


def start_atm_duration(int_direction, duration):
    distance = 20
    no_direction = int_direction
    phantom_res_list, vib_duration = generate_tactile_brush_results(1.0, distance, duration)
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
            _thread.start_new_thread(generate_atm_arduino, (start_vib_list, end_vib_list, time_SOA))
        except:
            print('Infrared ATM error')

        print('Start Vib List: ')
        print(start_vib_list)
        print('End Vib List: ')
        print(end_vib_list)

    else:
        try:
            _thread.start_new_thread(stop_single_vibration_arduino, ())
        except:
            print('Infrared Single Vibration error')


def compare_pixel_atm(rec_x, rec_y, flag):
    global flag_list
    flag_list.append(flag)

    img = cv2.imread(shape_path)
    height, width = img.shape[:2]
    x, y = convert_coord(rec_x, rec_y, height, width)
    x_final = round(x)
    y_final = round(y)
    color_pixel = img[y_final][x_final]

    global int_direction
    if shape_path == './shapes/triangle.png':
        horizontal_arr = [0, 0, 255]
        np_horizontal_arr = np.array(horizontal_arr)
        slash_arr = [255, 0, 0]
        np_slash_arr = np.array(slash_arr)
        backslash_arr = [0, 255, 255]
        np_backslash_arr = np.array(backslash_arr)

        tri_red_yellow_arr = [0, 0, 0]
        np_tri_red_yellow_arr = np.array(tri_red_yellow_arr)
        tri_yellow_blue_arr = [0, 0, 100]
        np_tri_yellow_blue_arr = np.array(tri_yellow_blue_arr)
        tri_blue_red_arr = [0, 0, 200]
        np_tri_blue_red_arr = np.array(tri_blue_red_arr)

        if (color_pixel == np_horizontal_arr).all():
            int_direction = 1
        elif (color_pixel == np_slash_arr).all():
            int_direction = 3
        elif (color_pixel == np_backslash_arr).all():
            int_direction = 4
        elif (color_pixel == np_tri_red_yellow_arr).all():
            int_direction = 1
        elif (color_pixel == np_tri_yellow_blue_arr).all():
            int_direction = 4
        elif (color_pixel == np_tri_blue_red_arr).all():
            int_direction = 3
        else:
            int_direction = 0
        if flag != int_direction:
            start_atm(int_direction)
            flag = int_direction

    elif shape_path == './shapes/rectangle.png' or shape_path == './shapes/square.png':
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

    elif shape_path == './shapes/zig.png':
        slash_arr = [255, 0, 0]
        np_slash_arr = np.array(slash_arr)
        backslash_arr = [0, 255, 255]
        np_backslash_arr = np.array(backslash_arr)

        if (color_pixel == np_slash_arr).all():
            int_direction = 3
        elif (color_pixel == np_backslash_arr).all():
            int_direction = 4
        else:
            int_direction = 0
        if flag != int_direction:
            start_atm(int_direction)
            flag = int_direction

    elif shape_path == './shapes/horizontal.png':
        horizontal_arr = [0, 0, 255]
        np_horizontal_arr = np.array(horizontal_arr)

        if x_final < width/2 and (color_pixel == np_horizontal_arr).all():
            if flag_list[-1] == 0:
                int_direction = -1
            if flag_list[-1] == 1:
                int_direction = 1
        elif x_final >= width/2 and (color_pixel == np_horizontal_arr).all():
            if flag_list[-1] == 0:
                int_direction = 1
            if flag_list[-1] == -1:
                int_direction = -1
        else:
            int_direction = 0

        if flag != int_direction:
            start_atm(int_direction)
            flag = int_direction

    elif shape_path == './shapes/vertical.png':
        vertical_arr = [0, 255, 0]
        np_vertical_arr = np.array(vertical_arr)

        if y_final >= height/2 and (color_pixel == np_vertical_arr).all():
            if flag_list[-1] == 0:
                int_direction = 2
            if flag_list[-1] == -2:
                int_direction = -2
        elif y_final < height/2 and (color_pixel == np_vertical_arr).all():
            if flag_list[-1] == 0:
                int_direction = -2
            if flag_list[-1] == 2:
                int_direction = 2
        else:
            int_direction = 0

        if flag != int_direction:
            start_atm(int_direction)
            flag = int_direction

    elif shape_path == './shapes/slash.png':
        slash_arr = [255, 0, 0]
        np_slash_arr = np.array(slash_arr)

        if x_final < width/2 and (color_pixel == np_slash_arr).all():
            if flag_list[-1] == 0:
                int_direction = 3
            if flag_list[-1] == -3:
                int_direction = -3
        elif x_final >= width/2 and (color_pixel == np_slash_arr).all():
            if flag_list[-1] == 0:
                int_direction = -3
            if flag_list[-1] == 3:
                int_direction = 3
        else:
            int_direction = 0

        if flag != int_direction:
            start_atm(int_direction)
            flag = int_direction

    elif shape_path == './shapes/backslash.png':
        back_slash_arr = [0, 255, 255]
        np_back_slash_arr = np.array(back_slash_arr)

        if x_final < width/2 and (color_pixel == np_back_slash_arr).all():
            if flag_list[-1] == 0:
                int_direction = 4
            if flag_list[-1] == -4:
                int_direction = -4
        elif x_final >= width/2 and (color_pixel == np_back_slash_arr).all():
            if flag_list[-1] == 0:
                int_direction = -4
            if flag_list[-1] == 4:
                int_direction = 4
        else:
            int_direction = 0

        if flag != int_direction:
            start_atm(int_direction)
            flag = int_direction

    return flag


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
            _thread.start_new_thread(generate_atm_arduino, (start_vib_list, end_vib_list, time_SOA))
        except:
            print('Infrared ATM error')

        print('Start Vib List: ')
        print(start_vib_list)
        print('End Vib List: ')
        print(end_vib_list)

    else:
        try:
            _thread.start_new_thread(stop_single_vibration_arduino, ())
        except:
            print('Infrared Single Vibration error')


def receive_from_infra():
    def start_infra(no_type):
        HOST = '127.0.0.1'
        PORT = 19000
        BUFSIZE = 1024
        ADDR = (HOST, PORT)
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind(ADDR)
        serversocket.listen(5)

        while True:
            clientsocket, addr = serversocket.accept()
            if no_type == 1:
                while True:
                    data = clientsocket.recv(BUFSIZE)
                    rec_data_str = data.decode('utf-8')
                    data_arr = rec_data_str.split(':')
                    if len(data_arr) > 2 and data_arr[0] == '1':
                        x_float = float(data_arr[1])
                        y_float = float(data_arr[2])
                        if x_float > 0 and y_float > 0:
                            set_coor_global(x_float, y_float)
                            compare_pixel(x_float, y_float)
            elif no_type == 2:
                flag_direction = 0 #Outside the while???
                while True:
                    data = clientsocket.recv(BUFSIZE)
                    rec_data_str = data.decode('utf-8')
                    data_arr = rec_data_str.split(':')
                    if len(data_arr) > 2 and data_arr[0] == '1':
                        x_float = float(data_arr[1])
                        y_float = float(data_arr[2])
                        if x_float > 0 and y_float > 0:
                            set_coor_global(x_float, y_float)
                            flag_get = compare_pixel_atm(x_float, y_float, flag_direction)
                            flag_direction = flag_get
            elif no_type == 3:
                flag_direction = 0
                while True:
                    data = clientsocket.recv(BUFSIZE)
                    rec_data_str = data.decode('utf-8')
                    data_arr = rec_data_str.split(':')
                    if len(data_arr) > 2 and data_arr[0] == '1':
                        x_float = float(data_arr[1])
                        y_float = float(data_arr[2])
                        if x_float > 0 and y_float > 0:
                            set_coor_global(x_float, y_float)
                            flag_get = compare_pixel_distance_atm(x_float, y_float, flag_direction)
                            flag_direction = flag_get
            clientsocket.close()


    print('Please input the vibration type: 1: Single Vibration, 2: ATM Vibration, 3: ATM Distance Vibration')
    no_type = input()
    start_infra(int(no_type))


class basedesk():
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title('Base UI')
        self.root.geometry('300x250')
        three_vibration_main_ui(self.root)

class three_vibration_main_ui():
    def __init__(self, master):
        self.master = master
        self.master.title('Main UI -- Choose Vibration Type')
        self.three_vibration_main_frame = tk.Frame(self.master, bg='white')
        self.three_vibration_main_frame.pack(fill=tk.X)

        btn_basic_vibration = tk.Button(self.three_vibration_main_frame, text='Basic Vibration', width=42, height=5, bg='white', command=self.change_single_vibration)
        btn_basic_vibration.pack()
        btn_atm_vibration = tk.Button(self.three_vibration_main_frame, text='ATM Vibration', width=42, height=5, bg='white', command=self.change_atm_vibration)
        btn_atm_vibration.pack()
        btn_confirm_vibration = tk.Button(self.three_vibration_main_frame, text='Confirm Vibration', width=42, height=5, bg='white', command=self.change_confirm_vibration)
        btn_confirm_vibration.pack()

    def change_single_vibration(self):
        self.three_vibration_main_frame.destroy()
        single_vibration_ui(self.master)

    def change_atm_vibration(self):
        self.three_vibration_main_frame.destroy()
        atm_vibration_ui(self.master)

    def change_confirm_vibration(self):
        self.three_vibration_main_frame.destroy()
        atm_distance_vibration_ui(self.master)


class single_vibration_ui():
    def __init__(self, master):
        self.master = master
        self.master.geometry('800x140')
        self.master.title('Single Vibration Perception')
        self.single_vibration_main_frame = tk.Frame(self.master, bg='white')
        self.single_vibration_main_frame.pack(fill=tk.X)

        v_shape = tk.IntVar()
        label_shape_text = tk.Label(self.single_vibration_main_frame, text='Shape', bg='white').grid(row=0, column=0)
        tk.Radiobutton(self.single_vibration_main_frame, text='Horizontal', variable=v_shape, value=1, bg='white').grid(row=0, column=1,
                                                                                                  ipadx=25)
        tk.Radiobutton(self.single_vibration_main_frame, text='Vertical', variable=v_shape, value=2, bg='white').grid(row=0, column=2,
                                                                                                ipadx=25)
        tk.Radiobutton(self.single_vibration_main_frame, text='Slash', variable=v_shape, value=3, bg='white').grid(row=0, column=3, ipadx=25)
        tk.Radiobutton(self.single_vibration_main_frame, text='Backslash', variable=v_shape, value=4, bg='white').grid(row=0, column=4,
                                                                                                 ipadx=25)
        tk.Radiobutton(self.single_vibration_main_frame, text='Curve', variable=v_shape, value=5, bg='white').grid(row=0, column=5, ipadx=25)
        tk.Radiobutton(self.single_vibration_main_frame, text='ZigZag', variable=v_shape, value=6, bg='white').grid(row=0, column=6, ipadx=25)

        tk.Radiobutton(self.single_vibration_main_frame, text='Square', variable=v_shape, value=7, bg='white').grid(row=2, column=1, ipadx=25)
        tk.Radiobutton(self.single_vibration_main_frame, text='Rectangle', variable=v_shape, value=8, bg='white').grid(row=2, column=2,
                                                                                                 ipadx=25)
        tk.Radiobutton(self.single_vibration_main_frame, text='Triangle', variable=v_shape, value=9, bg='white').grid(row=2, column=3,
                                                                                                ipadx=25)
        tk.Radiobutton(self.single_vibration_main_frame, text='Circle', variable=v_shape, value=10, bg='white').grid(row=2, column=4,
                                                                                               ipadx=25)

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
                cv2.circle(img, (x_final, y_final), 1, (0, 0, 0), -1)
                if key == 27:
                    cv2.destroyAllWindows()
                    return 0

        self.button_frame = tk.Frame(self.master, bg='white')
        self.button_frame.pack(fill=tk.X)
        btn_shape = tk.Button(self.button_frame, text='Choose Shape', command=choose_shape_click, width=42, height=5, bg='green')
        btn_shape.pack()

class atm_vibration_ui():
    def __init__(self, master):
        self.master = master
        self.master.geometry('800x140')
        self.master.title('ATM Vibration Perception')
        self.atm_vibration_main_frame = tk.Frame(self.master, bg='white')
        self.atm_vibration_main_frame.pack(fill=tk.X)

        v_shape = tk.IntVar()
        label_shape_text = tk.Label(self.atm_vibration_main_frame, text='Shape', bg='white').grid(row=0, column=0)
        tk.Radiobutton(self.atm_vibration_main_frame, text='Horizontal', variable=v_shape, value=1, bg='white').grid(row=0, column=1,
                                                                                                  ipadx=25)
        tk.Radiobutton(self.atm_vibration_main_frame, text='Vertical', variable=v_shape, value=2, bg='white').grid(row=0, column=2,
                                                                                                ipadx=25)
        tk.Radiobutton(self.atm_vibration_main_frame, text='Slash', variable=v_shape, value=3, bg='white').grid(row=0, column=3, ipadx=25)
        tk.Radiobutton(self.atm_vibration_main_frame, text='Backslash', variable=v_shape, value=4, bg='white').grid(row=0, column=4,
                                                                                                 ipadx=25)
        tk.Radiobutton(self.atm_vibration_main_frame, text='ZigZag', variable=v_shape, value=6, bg='white').grid(row=0, column=6, ipadx=25)
        tk.Radiobutton(self.atm_vibration_main_frame, text='Square', variable=v_shape, value=7, bg='white').grid(row=2, column=1, ipadx=25)
        tk.Radiobutton(self.atm_vibration_main_frame, text='Rectangle', variable=v_shape, value=8, bg='white').grid(row=2, column=2,
                                                                                                 ipadx=25)
        tk.Radiobutton(self.atm_vibration_main_frame, text='Triangle', variable=v_shape, value=9, bg='white').grid(row=2, column=3,
                                                                                                ipadx=25)

        def choose_shape_click():
            no_shape = v_shape.get()
            global shape_path
            if no_shape == 1:
                shape_path = './shapes/horizontal.png'
            elif no_shape == 2:
                shape_path = './shapes/vertical.png'
            elif no_shape == 3:
                shape_path = './shapes/slash.png'
            elif no_shape == 4:
                shape_path = './shapes/backslash.png'
            elif no_shape == 6:
                shape_path = './shapes/zig.png'
            elif no_shape == 7:
                shape_path = './shapes/square.png'
            elif no_shape == 8:
                shape_path = './shapes/rectangle.png'
            elif no_shape == 9:
                shape_path = './shapes/triangle.png'

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
                cv2.circle(img, (x_final, y_final), 1, (0, 0, 0), -1)
                if key == 27:
                    cv2.destroyAllWindows()
                    return 0

        self.button_frame = tk.Frame(self.master, bg='white')
        self.button_frame.pack(fill=tk.X)
        btn_shape = tk.Button(self.button_frame, text='Choose Shape', command=choose_shape_click, width=42, height=5, bg='green')
        btn_shape.pack()

class atm_distance_vibration_ui():
    def __init__(self, master):
        self.master = master
        self.master.geometry('800x140')
        self.master.title('ATM Distance Vibration Perception')
        self.atm_vibration_main_frame = tk.Frame(self.master, bg='white')
        self.atm_vibration_main_frame.pack(fill=tk.X)

        v_shape = tk.IntVar()
        label_shape_text = tk.Label(self.atm_vibration_main_frame, text='Shape', bg='white').grid(row=0, column=0)
        tk.Radiobutton(self.atm_vibration_main_frame, text='Horizontal', variable=v_shape, value=1, bg='white').grid(row=0, column=1,
                                                                                                  ipadx=25)
        tk.Radiobutton(self.atm_vibration_main_frame, text='Vertical', variable=v_shape, value=2, bg='white').grid(row=0, column=2,
                                                                                                ipadx=25)
        tk.Radiobutton(self.atm_vibration_main_frame, text='Slash', variable=v_shape, value=3, bg='white').grid(row=0, column=3, ipadx=25)
        tk.Radiobutton(self.atm_vibration_main_frame, text='Backslash', variable=v_shape, value=4, bg='white').grid(row=0, column=4,
                                                                                                 ipadx=25)
        tk.Radiobutton(self.atm_vibration_main_frame, text='ZigZag', variable=v_shape, value=6, bg='white').grid(row=0, column=6, ipadx=25)
        tk.Radiobutton(self.atm_vibration_main_frame, text='Square', variable=v_shape, value=7, bg='white').grid(row=2, column=1, ipadx=25)
        tk.Radiobutton(self.atm_vibration_main_frame, text='Rectangle', variable=v_shape, value=8, bg='white').grid(row=2, column=2,
                                                                                                 ipadx=25)
        tk.Radiobutton(self.atm_vibration_main_frame, text='Triangle', variable=v_shape, value=9, bg='white').grid(row=2, column=3,
                                                                                                ipadx=25)

        def choose_shape_click():
            no_shape = v_shape.get()
            global shape_path
            if no_shape == 1:
                shape_path = './shapes/horizontal.png'
            elif no_shape == 2:
                shape_path = './shapes/vertical.png'
            elif no_shape == 3:
                shape_path = './shapes/slash.png'
            elif no_shape == 4:
                shape_path = './shapes/backslash.png'
            elif no_shape == 6:
                shape_path = './shapes/zig.png'
            elif no_shape == 7:
                shape_path = './shapes/square.png'
            elif no_shape == 8:
                shape_path = './shapes/rectangle.png'
            elif no_shape == 9:
                shape_path = './shapes/triangle.png'

            img = cv2.imread(shape_path)
            height, width = img.shape[:2]

            while True:
                cv2.imshow('image', img)
                key = cv2.waitKey(1)
                x, y = convert_coord(str_x_global, str_y_global, height, width)
                x_final = round(x)
                y_final = round(y)
                cv2.circle(img, (x_final, y_final), 1, (0, 0, 0), -1)
                if key == 27:
                    cv2.destroyAllWindows()
                    return 0

        self.button_frame = tk.Frame(self.master, bg='white')
        self.button_frame.pack(fill=tk.X)
        btn_shape = tk.Button(self.button_frame, text='Choose Shape', command=choose_shape_click, width=42, height=5, bg='green')
        btn_shape.pack()

def start_ui():
    root = tk.Tk()
    basedesk(root)
    root.mainloop()

if __name__ == '__main__':
    threads = []
    t1 = threading.Thread(target=receive_from_infra)
    threads.append(t1)
    t2 = threading.Thread(target=start_ui)
    threads.append(t2)
    for t in threads:
        t.start()
    for t in threads:
        t.join()