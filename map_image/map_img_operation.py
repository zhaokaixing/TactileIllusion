import cv2
from matplotlib import pyplot as plt
import numpy as np
import socket

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
        clientsocket, addr = serversocket.accept()
        while 1:
            data = clientsocket.recv(BUFSIZE)
            rec_data_str = data.decode('utf-8')
            data_arr = rec_data_str.split(':')
            if len(data_arr) > 2 and data_arr[0] == '1':
                x_float = float(data_arr[1])
                y_float = float(data_arr[2])
                print(x_float)
                print(y_float)
                if x_float > 0 and y_float > 0:
                    compare_pixel(x_float, y_float, 'direc.png')

        clientsocket.close()

def convert_coord(x_origin, y_origin, image_height, image_width):
    x = image_width * x_origin
    y = image_height * y_origin
    return x, y

def compare_pixel(rec_x, rec_y, image_path):
    int_direction = 0

    img = cv2.imread(image_path)
    height, width = img.shape[:2]
    x, y = convert_coord(rec_x, rec_y, height, width)
    x_final = round(x)
    y_final = round(y)
    print(x_final)
    print(y_final)
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

    print(int_direction)
    print('---------------------------------------')
    #color_pixel = img[226, 153]
    #print(color_pixel)
    #plt.imshow(img)
    #plt.show()


#compare_pixel(0.4, 0.6, 'direc.png')
receive_from_infra()