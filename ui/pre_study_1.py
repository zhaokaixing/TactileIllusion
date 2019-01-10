import tkinter as tk
import csv
import random
import time
import numpy as np
from illusion.four_tactors_tactile_brush import generate_tactile_brush_results
from ardui.arduino_connect import generate_phantom_arduino
import _thread
'''
@author: zhaokaixing
@time: 10/01/2019
@version: main user interface for pre-study 1 -- study users' sensibility on phantom sensation
'''

'''
Function used to generate random order of 10 trials
'''
def generate_random_order():
    initial_order = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    random.shuffle(initial_order)
    return initial_order

'''
Function used to split one integer distance to 5 different intervals
'''
def splitInteger(m, n):
    assert n > 0
    quotient = m / n
    remainder = m % n
    if remainder > 0:
        return [quotient] * (n - remainder) + [quotient + 1] * remainder
    if remainder < 0:
        return [quotient - 1] * -remainder + [quotient] * (n + remainder)
    return [quotient] * n

'''
Function used to match the interval coordinates to the zone no.
'''
def generate_vib_point(distance):
    equal_list = splitInteger(distance, 3)
    flag_equal_list = []
    i = 0
    flag_equal_list.append(i)
    flag_equal_list.append(i + equal_list[0])
    flag_equal_list.append(i + equal_list[0] + equal_list[1])
    flag_equal_list.append(distance)

    res_list = []
    res_list.append(flag_equal_list[0])

    interval_1 = []
    interval_1.append(0)
    interval_1.append(flag_equal_list[1])
    res_list.append(np.mean(interval_1))

    interval_2 = []
    interval_2.append(flag_equal_list[1])
    interval_2.append(flag_equal_list[2])
    res_list.append(np.mean(interval_2))

    interval_3 = []
    interval_3.append(flag_equal_list[2])
    interval_3.append(flag_equal_list[3])
    res_list.append(np.mean(interval_3))

    res_list.append(flag_equal_list[3])

    final_res_list = []
    for num_item in res_list:
        final_res_list.append(int(round(num_item)))

    return final_res_list

'''
Function used to write the results to csv file
'''
def write_csv(list):
    csv_file = open('records.csv', 'a+')
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    csv_writer.writerow(list)
    csv_file.close()

'''
Function of the interface and main operations
'''
def resolution_interface():
    root = tk.Tk()
    root.minsize(820, 400)
    root.maxsize(820, 400)
    root.title('Pre-study: Investigate the effect of inter-actuator distance and body position on sensibility of Phantom Sensation')
    main_frame = tk.Frame(root, bg='white')
    main_frame.pack(fill=tk.X)

    label_user_id = tk.Label(main_frame, text='User ID: ', bg='white').grid(row=0, column=0)
    txt_user_id = tk.Entry(main_frame, fg='black', bg='white', width=10)
    txt_user_id.grid(row=0, column=1)
    label_body_position = tk.Label(main_frame, text='Body Position: ', bg='white').grid(row=0, column=2)
    v_body_position = tk.StringVar()
    v_body_position.set('Hand')
    tk.Radiobutton(main_frame, text='Hand', variable=v_body_position, value='Hand', bg='white').grid(row=0, column=3)
    tk.Radiobutton(main_frame, text='Arm', variable=v_body_position, value='Arm', bg='white').grid(row=0, column=4)

    v_distance_inter_actu = tk.IntVar()
    v_distance_inter_actu.set(10)
    label_distance_inter_actu = tk.Label(main_frame, text='Inter-actuator Distance(mm): ', bg='white').grid(row=1, column=0)
    tk.Radiobutton(main_frame, text='10', variable=v_distance_inter_actu, value=10, bg='white').grid(row=1, column=1,
                                                                                                     ipadx=20)
    tk.Radiobutton(main_frame, text='20', variable=v_distance_inter_actu, value=20, bg='white').grid(row=1, column=2,
                                                                                                     ipadx=20)
    tk.Radiobutton(main_frame, text='30', variable=v_distance_inter_actu, value=30, bg='white').grid(row=1, column=3,
                                                                                                     ipadx=20)
    tk.Radiobutton(main_frame, text='40', variable=v_distance_inter_actu, value=40, bg='white').grid(row=1, column=4,
                                                                                                     ipadx=20)
    tk.Radiobutton(main_frame, text='50', variable=v_distance_inter_actu, value=50, bg='white').grid(row=1, column=5,
                                                                                                     ipadx=20)
    tk.Radiobutton(main_frame, text='60', variable=v_distance_inter_actu, value=60, bg='white').grid(row=1, column=6,
                                                                                                     ipadx=20)
    tk.Radiobutton(main_frame, text='70', variable=v_distance_inter_actu, value=70, bg='white').grid(row=1, column=7,
                                                                                                     ipadx=20)
    tk.Radiobutton(main_frame, text='80', variable=v_distance_inter_actu, value=80, bg='white').grid(row=1, column=8,
                                                                                                     ipadx=20)
    '''
    Event listener of the Phantom Sensation Coordiante button -- used to calculate vibration order
    '''
    def cal_coordinate_order():
        total_distance = v_distance_inter_actu.get()
        random_order_list = generate_random_order()
        flag_point_list = generate_vib_point(total_distance)

        vib_order_list = []
        for item in random_order_list:
            if item == 1:
                vib_order_list.append(flag_point_list[0])
            elif item == 2:
                vib_order_list.append(flag_point_list[1])
            elif item == 3:
                vib_order_list.append(flag_point_list[2])
            elif item == 4:
                vib_order_list.append(flag_point_list[3])
            elif item == 5:
                vib_order_list.append(flag_point_list[4])
        v_coordinate_list.set(vib_order_list)
        v_proposed_order.set(random_order_list)

    coordinate_frame = tk.Frame(root, bg='white')
    coordinate_frame.pack(fill=tk.X)
    btn_cal_coordinate = tk.Button(coordinate_frame, text='Phantom Sensation Coordinate', bg='white', command=cal_coordinate_order)
    btn_cal_coordinate.grid(row=0, column=0)
    v_coordinate_list_show = tk.StringVar()
    v_coordinate_list = tk.StringVar()
    v_coordinate_list.set('* * * * * * * * * *')
    label_order_coordinate = tk.Label(coordinate_frame, textvariable=v_coordinate_list, bg='white').grid(row=0, column=1)
    label_text_order = tk.Label(coordinate_frame, text='Proposed Zone Order: ', bg='gray').grid(row=0, column=2)
    v_proposed_order = tk.StringVar()
    v_proposed_order.set('* * * * * * * * * *')
    label_order = tk.Label(coordinate_frame, textvariable=v_proposed_order, bg='gray').grid(row=0, column=3)

    info_coord_frame = tk.Frame(root, bg='white')
    info_coord_frame.pack(fill=tk.X)
    label_trial = tk.Label(info_coord_frame, text='Trial: ', bg='white').grid(row=0, column=0)
    v_trial_no = tk.IntVar()
    label_text_trial = tk.Label(info_coord_frame, textvariable=v_trial_no, bg='white').grid(row=0, column=1)
    label_current_coord = tk.Label(info_coord_frame, text='Current Coord: ', bg='white').grid(row=0, column=2)
    v_current_coord = tk.IntVar()
    label_text_current_coord = tk.Label(info_coord_frame, textvariable=v_current_coord, bg='white').grid(row=0, column=3)
    label_current_zone = tk.Label(info_coord_frame, text='Current Zone: ', bg='white').grid(row=0, column=4)
    v_current_zone = tk.IntVar()
    label_text_current_zone = tk.Label(info_coord_frame, textvariable=v_current_zone, bg='white').grid(row=0,
                                                                                                          column=5)

    '''
    Function used to communicate with Arduino
    '''
    def start_ps():
        phantom_res_list, vib_duration = generate_tactile_brush_results(1,
                                                                        v_distance_inter_actu.get(),
                                                                        2000)

        phantom_list = []
        for phantom_item in phantom_res_list:
            if v_current_coord.get() == phantom_item[0] and phantom_item[1] == 0:
                phantom_list.append(v_current_coord.get())
                phantom_list.append(0)
                phantom_list.append(phantom_item[2])
                phantom_list.append(phantom_item[3])
                phantom_list.append(phantom_item[4])
                phantom_list.append(phantom_item[5])
        phantom_list.append(2000)

        #print(phantom_list)
        try:
            _thread.start_new_thread(generate_phantom_arduino, (phantom_list,))
        except:
            print('Start thread exception')
    '''
    Event listener of the Start Phantom Sensation button -- used to create phantom sensation one by one according to the
    calculated order and coordinates
    '''
    def click_start_phantom_sensation():
        no_trial = v_trial_no.get()
        str_coord_list = v_coordinate_list.get()
        str_coord_list = str_coord_list.strip('(').strip(')')
        list_coord = str_coord_list.split(', ')
        str_pro_order = v_proposed_order.get()
        str_pro_order = str_pro_order.strip('(').strip(')')
        list_pro_order = str_pro_order.split(', ')
        #print(list_coord[no_trial])
        #print(list_pro_order[no_trial])
        v_current_coord.set(list_coord[no_trial])
        v_current_zone.set(list_pro_order[no_trial])
        start_ps()
        no_trial = no_trial + 1
        v_trial_no.set(no_trial)

    launch_frame = tk.Frame(root, bg='white')
    launch_frame.pack(fill=tk.X)
    btn_launch = tk.Button(launch_frame, text='Start Phantom Sensation', width=42, height=5, bg='green', command=click_start_phantom_sensation)
    btn_launch.pack()

    figure_frame = tk.Frame(root, bg='white')
    figure_frame.pack(fill=tk.X)
    image_path = tk.PhotoImage(file='C:\\Users\\kzhao\\PycharmProjects\\TactileIllusion\\zone_resolution.png')
    fig_image = tk.Label(figure_frame, image=image_path, bg='white').pack()

    result_frame = tk.Frame(root, bg='white')
    result_frame.pack(fill=tk.X)
    v_response = tk.IntVar()
    v_response.set(1)
    label_response = tk.Label(result_frame, text='Response: ', bg='white').grid(row=0, column=0)
    tk.Radiobutton(result_frame, text='1', variable=v_response, value=1, bg='white').grid(row=0, column=1, ipadx=20)
    tk.Radiobutton(result_frame, text='2', variable=v_response, value=2, bg='white').grid(row=0, column=2, ipadx=20)
    tk.Radiobutton(result_frame, text='3', variable=v_response, value=3, bg='white').grid(row=0, column=3, ipadx=20)
    tk.Radiobutton(result_frame, text='4', variable=v_response, value=4, bg='white').grid(row=0, column=4, ipadx=20)
    tk.Radiobutton(result_frame, text='5', variable=v_response, value=5, bg='white').grid(row=0, column=5, ipadx=20)

    '''
    Function used to save all of information related to a trial
    Date UserID TrialNo BodyPosition Inter-actuatorDistance CurrentZone ResponseZone T/F
    '''
    def click_btn_save_result():
        list_registres = []
        list_registres.append(time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()))
        list_registres.append(txt_user_id.get())
        list_registres.append(v_trial_no.get())
        list_registres.append(v_body_position.get())
        list_registres.append(v_distance_inter_actu.get())
        list_registres.append(v_current_zone.get())
        list_registres.append(v_response.get())
        if v_current_zone.get() == v_response.get():
            list_registres.append(1)
        else:
            list_registres.append(0)
        #print(list_registres)
        write_csv(list_registres)
    btn_save_result = tk.Button(result_frame, text='Save Result', width=25, bg='white', command=click_btn_save_result)
    btn_save_result.grid(row=0, column=6)

    root.mainloop()

resolution_interface()