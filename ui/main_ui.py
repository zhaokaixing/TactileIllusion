import tkinter as tk
from illusion.four_tactors_tactile_brush import generate_tactile_brush_results
from ardui.arduino_connect import generate_phantom_arduino
from ardui.arduino_connect import generate_atm_arduino_without_single_vibration
from illusion.four_tactors_tactile_brush import generate_SOA
from ardui.arduino_connect import stop_arduino
import _thread
'''
Author: Kaixing ZHAO
This file is the main user interface file, users can choose related actuators and parameters to launch
algorithm and Arduino
'''

def main_interface():
    root = tk.Tk()
    root.minsize(750, 500)
    root.maxsize(750, 500)
    root.title('4-tactor Tactile Illusion')

    main_frame = tk.Frame(root, bg='white')
    main_frame.pack(fill=tk.X)

    label_intensity = tk.Label(main_frame, text='Intensity: ', bg='white').grid(row=0)
    label_distance = tk.Label(main_frame, text='Distance(mm): ', bg='white').grid(row=1, column=0)
    label_T = tk.Label(main_frame, text='T(ms): ', bg='white').grid(row=1, column=2)

    v = tk.DoubleVar()
    v.set(1)

    tk.Radiobutton(main_frame, text='0.25', variable=v, value=0.25, bg='white').grid(row=0, column=1, ipadx=20)
    tk.Radiobutton(main_frame, text='0.5', variable=v, value=0.5, bg='white').grid(row=0, column=2, ipadx=20)
    tk.Radiobutton(main_frame, text='0.7', variable=v, value=0.7, bg='white').grid(row=0, column=3, ipadx=20)
    tk.Radiobutton(main_frame, text='1', variable=v, value=1, bg='white').grid(row=0, column=4, ipadx=20)

    txt_distance = tk.Entry(main_frame, fg='black', bg='white', width=20)
    txt_distance.grid(row=1, column=1)
    txt_T = tk.Entry(main_frame, fg='black', bg='white', width=20)
    txt_T.grid(row=1, column=3)

    tac_1_check_btn = tk.IntVar()
    tac_2_check_btn = tk.IntVar()
    tac_3_check_btn = tk.IntVar()
    tac_4_check_btn = tk.IntVar()

    label_start_tactors = tk.Label(main_frame, text='Start Tactors: ', bg='white').grid(row=3, column=0)
    c_btn1 = tk.Checkbutton(main_frame, bg='white', text='Tactor 1', variable=tac_1_check_btn, onvalue=1, offvalue=0)
    c_btn1.grid(row=3, column=1)
    c_btn2 = tk.Checkbutton(main_frame, bg='white', text='Tactor 2', variable=tac_2_check_btn, onvalue=1, offvalue=0)
    c_btn2.grid(row=3, column=2)
    c_btn3 = tk.Checkbutton(main_frame, bg='white', text='Tactor 3', variable=tac_3_check_btn, onvalue=1, offvalue=0)
    c_btn3.grid(row=3, column=3)
    c_btn4 = tk.Checkbutton(main_frame, bg='white', text='Tactor 4', variable=tac_4_check_btn, onvalue=1, offvalue=0)
    c_btn4.grid(row=3, column=4)

    tac_1_check_btn_end = tk.IntVar()
    tac_2_check_btn_end = tk.IntVar()
    tac_3_check_btn_end = tk.IntVar()
    tac_4_check_btn_end = tk.IntVar()

    label_end_tactors = tk.Label(main_frame, text='End Tactors: ', bg='white').grid(row=4, column=0)
    c_btn1_end = tk.Checkbutton(main_frame, bg='white', text='Tactor 1', variable=tac_1_check_btn_end, onvalue=1, offvalue=0)
    c_btn1_end.grid(row=4, column=1)
    c_btn2_end = tk.Checkbutton(main_frame, bg='white', text='Tactor 2', variable=tac_2_check_btn_end, onvalue=1, offvalue=0)
    c_btn2_end.grid(row=4, column=2)
    c_btn3_end = tk.Checkbutton(main_frame, bg='white', text='Tactor 3', variable=tac_3_check_btn_end, onvalue=1, offvalue=0)
    c_btn3_end.grid(row=4, column=3)
    c_btn4_end = tk.Checkbutton(main_frame, bg='white', text='Tactor 4', variable=tac_4_check_btn_end, onvalue=1, offvalue=0)
    c_btn4_end.grid(row=4, column=4)

    label_end_x = tk.Label(main_frame, text='end_x: ', bg='white').grid(row=5, column=0)
    txt_end_x = tk.Entry(main_frame, fg='black', bg='white', width=20)
    txt_end_x.grid(row=5, column=1)
    label_end_y = tk.Label(main_frame, text='end_y: ', bg='white').grid(row=5, column=2)
    txt_end_y = tk.Entry(main_frame, fg='black', bg='white', width=20)
    txt_end_y.grid(row=5, column=3)

    tactor_layout_frame = tk.Frame(root, bg='white')
    tactor_layout_frame.pack(fill=tk.X)

    cv = tk.Canvas(tactor_layout_frame, bg='white')
    circle_4 = cv.create_oval(70, 35, 90, 55, width=1, fill='red')
    circle_3 = cv.create_oval(275, 35, 295, 55, width=1, fill='red')
    circle_1 = cv.create_oval(70, 135, 90, 155, width=1, fill='red')
    circle_2 = cv.create_oval(275, 135, 295, 155, width=1, fill='red')

    lab_t1 = tk.Label(cv, text='Tactor 1 (0,0)', fg='black', bg='white')
    lab_t1.pack()
    cv.create_window(80, 170, window=lab_t1)

    lab_t2 = tk.Label(cv, text='Tactor 2 (Distance,0)', fg='black', bg='white')
    lab_t2.pack()
    cv.create_window(285, 170, window=lab_t2)

    lab_t3 = tk.Label(cv, text='Tactor 3 (Distance,Distance)', fg='black', bg='white')
    lab_t3.pack()
    cv.create_window(285, 70, window=lab_t3)

    lab_t4 = tk.Label(cv, text='Tactor 4 (0,Distance)', fg='black', bg='white')
    lab_t4.pack()
    cv.create_window(80, 70, window=lab_t4)

    cv.pack()

    button_frame = tk.Frame(root, bg='white')
    button_frame.pack(fill=tk.X)

    '''
    Function to change the color of figure
    '''
    def change_color_tactor(temp_list):
        if temp_list[2] > 0:
            cv.itemconfig(circle_1, fill='green')
        if temp_list[3] > 0:
            cv.itemconfig(circle_2, fill='green')
        if temp_list[4] > 0:
            cv.itemconfig(circle_3, fill='green')
        if temp_list[5] > 0:
            cv.itemconfig(circle_4, fill='green')


    def ps():
        c_btn1.config(state=tk.DISABLED)
        c_btn2.config(state=tk.DISABLED)
        c_btn3.config(state=tk.DISABLED)
        c_btn4.config(state=tk.DISABLED)

        c_btn1_end.config(state=tk.DISABLED)
        c_btn2_end.config(state=tk.DISABLED)
        c_btn3_end.config(state=tk.DISABLED)
        c_btn4_end.config(state=tk.DISABLED)

        btn_ATM.config(state=tk.DISABLED)
        btn_choose_end_real.config(state=tk.DISABLED)
        btn_choose_end_virtual.config(state=tk.DISABLED)

    def atm():
        c_btn1.config(state=tk.NORMAL)
        c_btn2.config(state=tk.NORMAL)
        c_btn3.config(state=tk.NORMAL)
        c_btn4.config(state=tk.NORMAL)

        c_btn1_end.config(state=tk.NORMAL)
        c_btn2_end.config(state=tk.NORMAL)
        c_btn3_end.config(state=tk.NORMAL)
        c_btn4_end.config(state=tk.NORMAL)

        btn_PS.config(state=tk.DISABLED)

    '''
    Function to launch Phantom Sensation
    '''
    def start_ps():
        phantom_res_list, vib_duration = generate_tactile_brush_results(float(str(v.get())),
                                                                        int(str(txt_distance.get())),
                                                                        int(str(txt_T.get())))

        phantom_list = []
        for phantom_item in phantom_res_list:
            if int(txt_end_x.get()) == phantom_item[0] and int(txt_end_y.get()) == phantom_item[1]:
                phantom_list.append(int(txt_end_x.get()))
                phantom_list.append(int(txt_end_y.get()))
                phantom_list.append(phantom_item[2])
                phantom_list.append(phantom_item[3])
                phantom_list.append(phantom_item[4])
                phantom_list.append(phantom_item[5])
        phantom_list.append(int(str(txt_T.get())))
        change_color_tactor(phantom_list)

        try:
            _thread.start_new_thread(generate_phantom_arduino, (phantom_list,))
        except:
            print('Start thread exception')

    '''
    Function to launch Apparent Tactile Motion
    '''
    def start_atm():
        phantom_res_list, vib_duration = generate_tactile_brush_results(float(str(v.get())),
                                                                        int(str(txt_distance.get())),
                                                                        int(str(txt_T.get())))
        start_vib_list = []

        temp_start_x = 0
        temp_start_y = 0
        if tac_1_check_btn.get() == 1:
            temp_start_x = 0
            temp_start_y = 0
        elif tac_2_check_btn.get() == 1:
            temp_start_x = int(txt_distance.get())
            temp_start_y = 0
        elif tac_3_check_btn.get() == 1:
            temp_start_x = int(txt_distance.get())
            temp_start_y = int(txt_distance.get())
        elif tac_4_check_btn.get() == 1:
            temp_start_x = 0
            temp_start_y = int(txt_distance.get())

        for phantom_item in phantom_res_list:
            # print(phantom_item)
            if int(temp_start_x) == phantom_item[0] and int(temp_start_y) == phantom_item[1]:
                start_vib_list.append(int(temp_start_x))
                start_vib_list.append(int(temp_start_y))
                start_vib_list.append(phantom_item[2])
                start_vib_list.append(phantom_item[3])
                start_vib_list.append(phantom_item[4])
                start_vib_list.append(phantom_item[5])
        start_vib_list.append(vib_duration)

        print(start_vib_list)

        end_vib_list = []
        if tac_1_check_btn_end.get() == 0 and tac_2_check_btn_end.get() == 0 and tac_3_check_btn_end.get() == 0 and tac_4_check_btn_end.get() == 0:
            if int(txt_end_x.get()) != temp_start_x and int(txt_end_y.get()) != temp_start_y:
                for phantom_item in phantom_res_list:
                    # print(phantom_item)
                    if int(txt_end_x.get()) == phantom_item[0] and int(txt_end_y.get()) == phantom_item[1] :
                        end_vib_list.append(int(txt_end_x.get()))
                        end_vib_list.append(int(txt_end_y.get()))
                        end_vib_list.append(phantom_item[2])
                        end_vib_list.append(phantom_item[3])
                        end_vib_list.append(phantom_item[4])
                        end_vib_list.append(phantom_item[5])
                    #end_vib_list.append(int(str(txt_T.get())))
            else:
                print('Can not choose this point')
                return 0
        else:
            temp_end_x = 0
            temp_end_y = 0
            if tac_1_check_btn_end.get() == 1:
                temp_end_x = 0
                temp_end_y = 0
            elif tac_2_check_btn_end.get() == 1:
                temp_end_x = int(txt_distance.get())
                temp_end_y = 0
            elif tac_3_check_btn_end.get() == 1:
                temp_end_x = int(txt_distance.get())
                temp_end_y = int(txt_distance.get())
            elif tac_4_check_btn_end.get() == 1:
                temp_end_x = 0
                temp_end_y = int(txt_distance.get())

            for phantom_item in phantom_res_list:
                # print(phantom_item)
                if int(temp_end_x) == phantom_item[0] and int(temp_end_y) == phantom_item[1]:
                    end_vib_list.append(int(temp_end_x))
                    end_vib_list.append(int(temp_end_y))
                    end_vib_list.append(phantom_item[2])
                    end_vib_list.append(phantom_item[3])
                    end_vib_list.append(phantom_item[4])
                    end_vib_list.append(phantom_item[5])
        end_vib_list.append(vib_duration)
        change_color_tactor(start_vib_list)
        change_color_tactor(end_vib_list)
        print(end_vib_list)

        time_SOA = generate_SOA(int(str(txt_T.get())), vib_duration)

        try:
            _thread.start_new_thread(generate_atm_arduino_without_single_vibration, (start_vib_list, end_vib_list, time_SOA))
        except:
            print('Start thread exception')

    def choose_action_virtual():
        c_btn1_end.config(state=tk.DISABLED)
        c_btn2_end.config(state=tk.DISABLED)
        c_btn3_end.config(state=tk.DISABLED)
        c_btn4_end.config(state=tk.DISABLED)
        txt_end_x.config(state=tk.NORMAL)
        txt_end_y.config(state=tk.NORMAL)

    def choose_action_real():
        c_btn1_end.config(state=tk.NORMAL)
        c_btn2_end.config(state=tk.NORMAL)
        c_btn3_end.config(state=tk.NORMAL)
        c_btn4_end.config(state=tk.NORMAL)
        txt_end_x.config(state=tk.DISABLED)
        txt_end_y.config(state=tk.DISABLED)

    def clear_action():
        c_btn1.config(state=tk.NORMAL)
        c_btn2.config(state=tk.NORMAL)
        c_btn3.config(state=tk.NORMAL)
        c_btn4.config(state=tk.NORMAL)

        c_btn1_end.config(state=tk.NORMAL)
        c_btn2_end.config(state=tk.NORMAL)
        c_btn3_end.config(state=tk.NORMAL)
        c_btn4_end.config(state=tk.NORMAL)

        txt_end_x.config(state=tk.NORMAL)
        txt_end_x.delete(0, tk.END)
        txt_end_y.config(state=tk.NORMAL)
        txt_end_y.delete(0, tk.END)
        txt_distance.config(state=tk.NORMAL)
        txt_distance.delete(0, tk.END)
        txt_T.config(state=tk.NORMAL)
        txt_T.delete(0, tk.END)

        btn_ATM.config(state=tk.NORMAL)
        btn_choose_end_real.config(state=tk.NORMAL)
        btn_choose_end_virtual.config(state=tk.NORMAL)
        btn_PS.config(state=tk.NORMAL)

        cv.itemconfig(circle_1, fill='red')
        cv.itemconfig(circle_2, fill='red')
        cv.itemconfig(circle_3, fill='red')
        cv.itemconfig(circle_4, fill='red')

    def stop_action():
        stop_arduino()

    btn_PS = tk.Button(main_frame, text='Phantom Sensation', command=ps, width=20)
    btn_PS.grid(row=2, column=0)
    btn_ATM = tk.Button(main_frame, text='Apparent Tactile Motion', command=atm, width=20)
    btn_ATM.grid(row=2, column=1)
    btn_stop = tk.Button(button_frame, text='Stop', width=25, command=stop_action)
    btn_stop.grid(row=0, column=2)
    btn_clear = tk.Button(button_frame, text='Clear', width=25, command=clear_action)
    btn_clear.grid(row=0, column=3)

    btn_start_ps = tk.Button(button_frame, text='Start Phantom', command=start_ps, width=25)
    btn_start_ps.grid(row=0, column=0)
    btn_start_atm = tk.Button(button_frame, text='Start Apparent Motion', command=start_atm, width=25)
    btn_start_atm.grid(row=0, column=1)
    btn_choose_end_virtual = tk.Button(main_frame, text='Choose virtual vibrator', command=choose_action_virtual, width=20)
    btn_choose_end_virtual.grid(row=2, column=2)
    btn_choose_end_real = tk.Button(main_frame, text='Choose real vibrator', command=choose_action_real, width=20)
    btn_choose_end_real.grid(row=2, column=3)

    logo_path = tk.PhotoImage(file='C:\\Users\\kzhao\\PycharmProjects\\TactileIllusion\\elipse.png')
    logo = tk.Label(tactor_layout_frame, image=logo_path, bg='white').pack()

    root.mainloop()

main_interface()

