import tkinter as tk
import numpy as np

def SOA_interface_main():
    root = tk.Tk()
    root.minsize(600, 600)
    root.maxsize(600, 600)
    root.title('SOA Experiment Main UI')

    main_frame = tk.Frame(root, bg='white')
    main_frame.pack(fill=tk.X)

    label_duration = tk.Label(main_frame, text='Duration(ms): ', bg='white').grid(row=0, column=0)
    v = tk.IntVar()
    v.set(120)
    tk.Radiobutton(main_frame, text='120', variable=v, value=120, bg='white').grid(row=0, column=1, ipadx=20)
    tk.Radiobutton(main_frame, text='180', variable=v, value=180, bg='white').grid(row=0, column=2, ipadx=20)
    tk.Radiobutton(main_frame, text='240', variable=v, value=240, bg='white').grid(row=0, column=3, ipadx=20)

    label_case = tk.Label(main_frame, text='SOA case: ', bg='white').grid(row=1, column=0)
    v_case = tk.IntVar()
    v_case.set(1)
    tk.Radiobutton(main_frame, text='Upper threshold', variable=v_case, value='1', bg='white').grid(row=1, column=1, ipadx=20)
    tk.Radiobutton(main_frame, text='Lower threshold', variable=v_case, value='2', bg='white').grid(row=1, column=2, ipadx=20)

    reverse_times = tk.IntVar()
    reverse_times.set(0)
    label_reverse_times = tk.Label(main_frame, text='Reverse Times: ', bg='white').grid(row=2, column=0)
    label_reverse_times_value = tk.Label(main_frame, textvariable=reverse_times, bg='white')
    label_reverse_times_value.grid(row=2, column=1)

    def compare_flag(flag_list):
        rever_times_temp = reverse_times.get()
        if len(flag_list) > 1:
            if flag_list[-1] == flag_list[-2]:
                return 1
            else:
                rever_times_temp = rever_times_temp + 1
                reverse_times.set(rever_times_temp)
                return 0

    upper_flag_list = []
    lower_flag_list = []
    upper_soa_value_list = []
    lower_soa_value_list = []

    def yes_button_change_soa():
        case_value = v_case.get()
        soa_value = v_soa.get()
        reverse_value = reverse_times.get()
        if reverse_value < 2:
            stepsize = 16
        else:
            stepsize = 4
        if case_value == 1:
            soa_value = soa_value - stepsize
            upper_flag_list.append('-')
            compared_res = compare_flag(upper_flag_list)
            if compared_res == 0:
                upper_soa_value_list.append(soa_value + stepsize)
            v_soa.set(soa_value)
            if reverse_times.get() == 8:
                v_soa_values.set(upper_soa_value_list)
                #v_soa_avr.set(np.mean(upper_soa_value_list[]))
        else:
            soa_value = soa_value + stepsize
            lower_flag_list.append('+')
            compared_res = compare_flag(lower_flag_list)
            if compared_res == 0:
                lower_soa_value_list.append(soa_value - stepsize)
            v_soa.set(soa_value)
            if reverse_times.get() == 8:
                v_soa_values.set(lower_soa_value_list)

    def no_button_change_soa():
        case_value = v_case.get()
        soa_value = v_soa.get()
        reverse_value = reverse_times.get()
        if reverse_value < 2:
            stepsize = 16
        else:
            stepsize = 4
        if case_value == 1:
            soa_value = soa_value + stepsize
            upper_flag_list.append('+')
            compared_res = compare_flag(upper_flag_list)
            if compared_res == 0:
                upper_soa_value_list.append(soa_value - stepsize)
            v_soa.set(soa_value)
            if reverse_times.get() == 8:
                v_soa_values.set(upper_soa_value_list)
        else:
            soa_value = soa_value - stepsize
            lower_flag_list.append('-')
            compared_res = compare_flag(lower_flag_list)
            if compared_res == 0:
                lower_soa_value_list.append(soa_value + stepsize)
            v_soa.set(soa_value)
            if reverse_times.get() == 8:
                v_soa_values.set(lower_soa_value_list)


    res_frame = tk.Frame(root, bg='white')
    res_frame.pack(fill=tk.X)
    label_res = tk.Label(res_frame, text='', bg='white').grid(row=0, column=0)
    btn_yes = tk.Button(res_frame, text='Yes', width=42, height=5, bg='green', command=yes_button_change_soa)
    btn_yes.grid(row=1, column=0)
    btn_no = tk.Button(res_frame, text='No', width=42, height=5, bg='red', command=no_button_change_soa)
    btn_no.grid(row=1, column=1)

    v_soa = tk.IntVar()
    v_soa.set(120)
    soa_frame = tk.Frame(root, bg='white')
    soa_frame.pack(fill=tk.X)
    label_SOA = tk.Label(soa_frame, textvariable=v_soa, bg='white', height=5)
    label_SOA.config(font=("Courier", 44))
    label_SOA.pack()

    cal_soa_frame = tk.Frame(root, bg='white')
    cal_soa_frame.pack(fill=tk.X)
    v_soa_avr = tk.DoubleVar()
    v_soa_avr.set(0.0)
    v_soa_values = tk.StringVar()
    label_SOA_avr = tk.Label(cal_soa_frame, text='SOA Values: ', bg='white')
    label_SOA_avr.pack()
    #label_SOA_avr.grid(row=0, column=0)
    label_SOA_values = tk.Label(cal_soa_frame, textvariable=v_soa_values, bg='white')
    label_SOA_values.pack()
    #label_SOA_values.grid(row=0, column=1)
    label_SOA_avr_value = tk.Label(cal_soa_frame, textvariable=v_soa_avr, bg='white')
    label_SOA_avr_value.pack()
    #label_SOA_avr_value.grid(row=0, column=2)

    root.mainloop()

SOA_interface_main()