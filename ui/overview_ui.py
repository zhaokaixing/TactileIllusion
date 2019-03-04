import tkinter as tk
from ardui.arduino_connect import generate_atm_arduino_without_single_vibration_overview
import _thread
from illusion.four_tactors_tactile_brush import generate_tactile_brush_results
from illusion.four_tactors_tactile_brush import generate_SOA
import time


def square_click():
    for i in range(0, 3):
        start_atm_duration(1, 500)
        time.sleep(1)
        start_atm_duration(2, 500)
        time.sleep(1)
        start_atm_duration(3, 500)
        time.sleep(1)
        start_atm_duration(4, 500)
        time.sleep(1.5)


def triangle_normal_click():
    for i in range(0, 3):
        start_atm_duration(3, 500)
        time.sleep(1)
        start_atm_duration(6, 350)
        time.sleep(1)
        start_atm_duration(5, 350)
        time.sleep(1.5)


def triangle_right_click():
    for i in range(0, 3):
        start_atm_duration(5, 500)
        time.sleep(1)
        start_atm_duration(3, 350)
        time.sleep(1)
        start_atm_duration(4, 350)
        time.sleep(1.5)


def rectangle_click():
    for i in range(0, 3):
        start_atm_duration(1, 500)
        time.sleep(1)
        start_atm_duration(2, 300)
        time.sleep(1)
        start_atm_duration(3, 500)
        time.sleep(1)
        start_atm_duration(4, 300)
        time.sleep(1.5)


def overview_ui_main():
    root = tk.Tk()
    root.minsize(600, 350)
    root.maxsize(600, 350)
    root.title('Overview Test UI')

    main_frame = tk.Frame(root, bg='white')
    main_frame.pack(fill=tk.X)

    btn_square = tk.Button(main_frame, text='Square', width=42, height=5, bg='white', command=square_click)
    btn_square.pack()
    btn_triangle_normal = tk.Button(main_frame, text='Triangle Normal', width=42, height=5, bg='white', command=triangle_normal_click)
    btn_triangle_normal.pack()
    btn_triangle_right = tk.Button(main_frame, text='Triangle Right', width=42, height=5, bg='white',
                             command=triangle_right_click)
    btn_triangle_right.pack()
    btn_rectangle = tk.Button(main_frame, text='Rectangle', width=42, height=5, bg='white', command=rectangle_click)
    btn_rectangle.pack()
    btn_line = tk.Button(main_frame, text='Line', width=42, height=5, bg='white')
    btn_line.pack()

    root.mainloop()


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
        temp_start_x = 0
        temp_start_y = distance
        temp_end_x = distance
        temp_end_y = distance
    elif no_direction == 2:
        temp_start_x = distance
        temp_start_y = distance
        temp_end_x = distance
        temp_end_y = 0
    elif no_direction == 3:
        temp_start_x = distance
        temp_start_y = 0
        temp_end_x = 0
        temp_end_y = 0
    elif no_direction == 4:
        temp_start_x = 0
        temp_start_y = 0
        temp_end_x = 0
        temp_end_y = distance
    elif no_direction == 5:
        temp_start_x = 0
        temp_start_y = distance
        temp_end_x = distance
        temp_end_y = 0
    elif no_direction == 6:
        temp_start_x = 0
        temp_start_y = 0
        temp_end_x = distance
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
            _thread.start_new_thread(generate_atm_arduino_without_single_vibration_overview, (start_vib_list, end_vib_list, time_SOA))

        except:
            print('Infrared ATM error')

        print('Start Vib List: ')
        print(start_vib_list)
        print('End Vib List: ')
        print(end_vib_list)


overview_ui_main()