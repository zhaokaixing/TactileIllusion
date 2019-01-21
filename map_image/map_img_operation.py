import cv2
from matplotlib import pyplot as plt
import numpy as np
import socket
from illusion.four_tactors_tactile_brush import generate_tactile_brush_results
from illusion.four_tactors_tactile_brush import generate_SOA
from ardui.arduino_connect import generate_atm_arduino

import _thread

def receive_from_infra():
    HOST = '127.0.0.1'
    PORT = 19000
    BUFSIZE = 1024
    ADDR = (HOST, PORT)
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
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
                #print(x_float)
                #print(y_float)
                if x_float > 0 and y_float > 0:
                    flag_get = compare_pixel(x_float, y_float, 'direc.png', flag_direction)
                    flag_direction = flag_get

        clientsocket.close()

def convert_coord(x_origin, y_origin, image_height, image_width):
    x = image_width * x_origin
    y = image_height * y_origin
    return x, y

def compare_pixel(rec_x, rec_y, image_path, flag):

    img = cv2.imread(image_path)
    height, width = img.shape[:2]
    x, y = convert_coord(rec_x, rec_y, height, width)
    x_final = round(x)
    y_final = round(y)
    #print(x_final)
    #print(y_final)
    color_pixel = img[y_final][x_final]

    left_top_arr = [255, 255, 126]
    np_left_top_arr = np.array(left_top_arr)
    top_arr = [126, 255, 126]
    np_top_arr = np.array(top_arr)
    right_top_arr = [126, 255, 255]
    np_right_top_arr = np.array(right_top_arr)
    left_arr = [126, 126, 126]
    np_left_arr = np.array(left_arr)
    right_arr = [126, 126, 255]
    np_right_arr = np.array(right_arr)
    left_bottom_arr = [255, 126, 255]
    np_left_bottom_arr = np.array(left_bottom_arr)
    bottom_arr = [255, 126, 126]
    np_bottom_arr = np.array(bottom_arr)
    right_bottom_arr = [179, 179, 179]
    np_right_bottom_arr = np.array(right_bottom_arr)

    if (color_pixel == np_left_top_arr).all():
        int_direction = 1
    elif (color_pixel == np_top_arr).all():
        int_direction = 2
    elif (color_pixel == np_right_top_arr).all():
        int_direction = 3
    elif (color_pixel == np_left_arr).all():
        int_direction = 4
    elif (color_pixel == np_right_arr).all():
        int_direction = 5
    elif (color_pixel == np_left_bottom_arr).all():
        int_direction = 6
    elif (color_pixel == np_bottom_arr).all():
        int_direction = 7
    elif (color_pixel == np_right_bottom_arr).all():
        int_direction = 8
    else:
        int_direction = 0

    if flag != int_direction:
        #print('change')
        flag = int_direction
        print(int_direction)
        start_atm(int_direction)
        #print('---------------------------------------')

    #print(int_direction)
    #print('---------------------------------------')
    #color_pixel = img[226, 153]
    #print(color_pixel)
    #plt.imshow(img)
    #plt.show()
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
        temp_start_y = 0
        temp_end_x = 0
        temp_end_y = distance
    elif no_direction == 2:
        temp_start_x = distance
        temp_start_y = 0
        temp_end_x = distance
        temp_end_y = distance
    elif no_direction == 3:
        temp_start_x = 0
        temp_start_y = 0
        temp_end_x = distance
        temp_end_y = distance
    elif no_direction == 4:
        temp_start_x = distance
        temp_start_y = 0
        temp_end_x = 0
        temp_end_y = 0
    elif no_direction == 5:
        temp_start_x = 0
        temp_start_y = distance
        temp_end_x = distance
        temp_end_y = distance
    elif no_direction == 6:
        temp_start_x = distance
        temp_start_y = distance
        temp_end_x = 0
        temp_end_y = 0
    elif no_direction == 7:
        temp_start_x = 0
        temp_start_y = distance
        temp_end_x = 0
        temp_end_y = 0
    elif no_direction == 8:
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
        except:
            print('Infrared ATM error')

        #print('Time SOA: ' + str(time_SOA))
        print('Start Vib List: ')
        print(start_vib_list)
        print('End Vib List: ')
        print(end_vib_list)



receive_from_infra()
#start_atm(8)