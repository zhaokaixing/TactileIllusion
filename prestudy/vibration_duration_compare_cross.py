import random
import tkinter as tk
import csv
import _thread
from ardui.arduino_formal import generate_vibration_simple
from illusion.four_tactors_tactile_brush import generate_tactile_brush_results
from illusion.four_tactors_tactile_brush import generate_SOA
from ardui.arduino_formal import generate_atm_arduino

'''
File used to study the effect of vibration durations on recognition accuracy -- Cross Layout 
'''

flag_svp = 0
flag_atm = 0

flag_train_svp = 0
flag_train_atm = 0


# Function to generate random order
def generate_random_order():
    initial_order = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]
    random.shuffle(initial_order)
    return initial_order


# Function to write results to CSV file
def write_csv(list):
    csv_file = open('vibration_duration_results_cross.csv', 'a+')
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    csv_writer.writerow(list)
    csv_file.close()


# Main UI function
def vibration_duration_compare_ui():
    root = tk.Tk()
    root.minsize(600, 500)
    root.maxsize(600, 500)
    root.title('Vibration Duration Comparison Cross Layout')

    demography_frame = tk.Frame(root)
    demography_frame.pack(fill=tk.X)
    label_participant = tk.Label(demography_frame, text='Participant: ', font=("Helvetica", 11))
    label_participant.grid(row=0, column=0)
    txt_participant = tk.Entry(demography_frame, fg='black', width=20)
    txt_participant.grid(row=0, column=1)

    config_frame = tk.Frame(root)
    config_frame.pack(fill=tk.X)
    label_duration = tk.Label(config_frame, text='Duration(ms): ', font=("Helvetica", 11))
    label_duration.grid(row=0, column=0)

    v_duration = tk.IntVar()
    v_duration.set(50)
    tk.Radiobutton(config_frame, text='50', variable=v_duration, value=50, font=("Helvetica", 11)).grid(row=0, column=1,
                                                                                                        ipadx=10)
    tk.Radiobutton(config_frame, text='150', variable=v_duration, value=150, font=("Helvetica", 11)).grid(row=0,
                                                                                                          column=2,
                                                                                                          ipadx=10)
    tk.Radiobutton(config_frame, text='200', variable=v_duration, value=200, font=("Helvetica", 11)).grid(row=0,
                                                                                                          column=3,
                                                                                                          ipadx=10)
    tk.Radiobutton(config_frame, text='250', variable=v_duration, value=250, font=("Helvetica", 11)).grid(row=0,
                                                                                                          column=4,
                                                                                                          ipadx=10)
    tk.Radiobutton(config_frame, text='350', variable=v_duration, value=350, font=("Helvetica", 11)).grid(row=0,
                                                                                                          column=5,
                                                                                                          ipadx=10)

    label_technique = tk.Label(config_frame, text='Interaction Technique: ', font=("Helvetica", 11))
    label_technique.grid(row=1, column=0)
    v_technique = tk.StringVar()
    v_technique.set('SVP')
    tk.Radiobutton(config_frame, text='SVP', variable=v_technique, value='SVP', font=("Helvetica", 11)).grid(row=1,
                                                                                                             column=1,
                                                                                                             ipadx=10)
    tk.Radiobutton(config_frame, text='ATM', variable=v_technique, value='ATM', font=("Helvetica", 11)).grid(row=1,
                                                                                                             column=2,
                                                                                                             ipadx=10)

    def click_btn_train_svp():
        int_direction_list = [1, 2, 3, 4, 5, 6, 7, 8]
        global flag_train_svp
        if flag_train_svp <= 7:
            direction_item = int_direction_list[flag_train_svp]
            svp_vib_list = []
            if direction_item == 1:
                print('Up')
                svp_vib_list.append(0)
                svp_vib_list.append(0)
                svp_vib_list.append(0)
                svp_vib_list.append(1)
            elif direction_item == 2:
                print('Top Right')
                svp_vib_list.append(0)
                svp_vib_list.append(0)
                svp_vib_list.append(1)
                svp_vib_list.append(1)
            elif direction_item == 3:
                print('Right')
                svp_vib_list.append(0)
                svp_vib_list.append(0)
                svp_vib_list.append(1)
                svp_vib_list.append(0)
            elif direction_item == 4:
                print('Bottom Right')
                svp_vib_list.append(0)
                svp_vib_list.append(1)
                svp_vib_list.append(1)
                svp_vib_list.append(0)
            elif direction_item == 5:
                print('Down')
                svp_vib_list.append(0)
                svp_vib_list.append(1)
                svp_vib_list.append(0)
                svp_vib_list.append(0)
            elif direction_item == 6:
                print('Bottom Left')
                svp_vib_list.append(1)
                svp_vib_list.append(1)
                svp_vib_list.append(0)
                svp_vib_list.append(0)
            elif direction_item == 7:
                print('Left')
                svp_vib_list.append(1)
                svp_vib_list.append(0)
                svp_vib_list.append(0)
                svp_vib_list.append(0)
            else:
                print('Top Left')
                svp_vib_list.append(1)
                svp_vib_list.append(0)
                svp_vib_list.append(0)
                svp_vib_list.append(1)
            try:
                _thread.start_new_thread(generate_vibration_simple, (svp_vib_list, int(v_duration.get())))
            except:
                print('SVP Train Error')

            flag_train_svp = flag_train_svp + 1
        else:
            flag_train_svp = 0

    def click_btn_train_atm():
        int_distance_value = 40
        int_direction_list = [1, 2, 3, 4, 5, 6, 7, 8]
        global flag_train_atm
        if flag_train_atm <= 7:
            direction_item = int_direction_list[flag_train_atm]
            phantom_res_list, vib_duration = generate_tactile_brush_results(1.0, int_distance_value, int(v_duration.get()))
            start_vib_list = []
            end_vib_list = []
            if direction_item == 1:
                print('ATM Up')
                start_x = int_distance_value
                start_y = 0
                print('ATM Up END')
                end_x = 0
                end_y = int_distance_value
            elif direction_item == 2:
                print('ATM Top Right')
                start_x = 0
                start_y = 0
                print('ATM Top Right END')
                end_x = 0
                end_y = int_distance_value
            elif direction_item == 3:
                print('ATM Right')
                start_x = 0
                start_y = 0
                print('ATM Right END')
                end_x = int_distance_value
                end_y = int_distance_value
            elif direction_item == 4:
                print('ATM Bottom Right')
                start_x = 0
                start_y = 0
                print('ATM Bottom Right END')
                end_x = int_distance_value
                end_y = 0
            elif direction_item == 5:
                print('ATM Down')
                start_x = 0
                start_y = int_distance_value
                print('ATM Down END')
                end_x = int_distance_value
                end_y = 0
            elif direction_item == 6:
                print('ATM Bottom Left')
                start_x = int_distance_value
                start_y = int_distance_value
                print('ATM Bottom Left END')
                end_x = int_distance_value
                end_y = 0
            elif direction_item == 7:
                print('ATM Left')
                start_x = int_distance_value
                start_y = int_distance_value
                print('ATM Left END')
                end_x = 0
                end_y = 0
            else:
                print('ATM Top Left')
                start_x = int_distance_value
                start_y = int_distance_value
                print('ATM Top Left END')
                end_x = 0
                end_y = int_distance_value
            for phantom_item in phantom_res_list:
                if int(start_x) == phantom_item[0] and int(start_y) == phantom_item[1]:
                    start_vib_list.append(int(start_x))
                    start_vib_list.append(int(start_y))
                    start_vib_list.append(phantom_item[2])
                    start_vib_list.append(phantom_item[3])
                    start_vib_list.append(phantom_item[4])
                    start_vib_list.append(phantom_item[5])
            start_vib_list.append(vib_duration)
            for phantom_item in phantom_res_list:
                if int(end_x) == phantom_item[0] and int(end_y) == phantom_item[1]:
                    end_vib_list.append(int(end_x))
                    end_vib_list.append(int(end_y))
                    end_vib_list.append(phantom_item[2])
                    end_vib_list.append(phantom_item[3])
                    end_vib_list.append(phantom_item[4])
                    end_vib_list.append(phantom_item[5])
            end_vib_list.append(vib_duration)

            time_SOA = generate_SOA(int(v_duration.get()), vib_duration)

            try:
                _thread.start_new_thread(generate_atm_arduino, (start_vib_list, end_vib_list, time_SOA))
            except:
                print('ATM Train Error!')

            flag_train_atm = flag_train_atm + 1
        else:
            flag_train_atm = 0

    training_frame = tk.Frame(root)
    training_frame.pack(fill=tk.X)
    btn_train_svp = tk.Button(training_frame, text='Train SVP', width=30, height=3,
                              font=("Helvetica", 11), command=click_btn_train_svp)
    btn_train_svp.grid(row=0, column=0)
    btn_train_atm = tk.Button(training_frame, text='Train ATM', width=30, height=3,
                              font=("Helvetica", 11), command=click_btn_train_atm)
    btn_train_atm.grid(row=0, column=1)

    order_frame = tk.Frame(root)
    order_frame.pack(fill=tk.X)

    def click_btn_generate_order():
        v_label_order.set(generate_random_order())
    btn_generate_order = tk.Button(order_frame, text='Generate Random Order', width=30, height=3, font=("Helvetica", 11), command=click_btn_generate_order)
    btn_generate_order.grid(row=0, column=0)

    v_label_order = tk.StringVar()
    label_order = tk.Label(order_frame, textvariable=v_label_order, width=30, height=3, font=("Helvetica", 11))
    label_order.grid(row=0, column=1)

    # Function to start the vibration
    def click_btn_start_vib():
        duration_value = v_duration.get()
        order_value = v_label_order.get()
        technique_value = v_technique.get()
        order_arr = order_value.strip('(').strip(')').split(', ')
        global flag_svp
        global flag_atm
        if technique_value == 'SVP':
            if flag_svp <= 15:
                direction_value = order_arr[flag_svp]
                result_list = []
                result_list.append(str(duration_value))
                result_list.append(technique_value)
                result_list.append(direction_value)
                v_result.set(result_list)

                int_direction_value = int(direction_value)

                svp_vib_list = []
                if int_direction_value == 1:
                    print('Up')
                    svp_vib_list.append(0)
                    svp_vib_list.append(0)
                    svp_vib_list.append(0)
                    svp_vib_list.append(1)
                elif int_direction_value == 2:
                    print('Top Right')
                    svp_vib_list.append(0)
                    svp_vib_list.append(0)
                    svp_vib_list.append(1)
                    svp_vib_list.append(1)
                elif int_direction_value == 3:
                    print('Right')
                    svp_vib_list.append(0)
                    svp_vib_list.append(0)
                    svp_vib_list.append(1)
                    svp_vib_list.append(0)
                elif int_direction_value == 4:
                    print('Bottom Right')
                    svp_vib_list.append(0)
                    svp_vib_list.append(1)
                    svp_vib_list.append(1)
                    svp_vib_list.append(0)
                elif int_direction_value == 5:
                    print('Down')
                    svp_vib_list.append(0)
                    svp_vib_list.append(1)
                    svp_vib_list.append(0)
                    svp_vib_list.append(0)
                elif int_direction_value == 6:
                    print('Bottom Left')
                    svp_vib_list.append(1)
                    svp_vib_list.append(1)
                    svp_vib_list.append(0)
                    svp_vib_list.append(0)
                elif int_direction_value == 7:
                    print('Left')
                    svp_vib_list.append(1)
                    svp_vib_list.append(0)
                    svp_vib_list.append(0)
                    svp_vib_list.append(0)
                else:
                    print('Top Left')
                    svp_vib_list.append(1)
                    svp_vib_list.append(0)
                    svp_vib_list.append(0)
                    svp_vib_list.append(1)
                try:
                    _thread.start_new_thread(generate_vibration_simple, (svp_vib_list, int(duration_value)))
                except:
                    print('SVP Error')

                flag_svp = flag_svp + 1
            else:
                print('Max SVP Value')
        else:
            if flag_atm <= 15:
                int_distance_value = 40
                direction_value = order_arr[flag_atm]
                result_list = []
                result_list.append(duration_value)
                result_list.append(technique_value)
                result_list.append(direction_value)
                v_result.set(result_list)

                int_direction_value = int(direction_value)
                phantom_res_list, vib_duration = generate_tactile_brush_results(1.0, int_distance_value, int(duration_value))
                start_vib_list = []
                end_vib_list = []
                if int_direction_value == 1:
                    print('ATM Up')
                    start_x = int_distance_value
                    start_y = 0
                    print('ATM Up END')
                    end_x = 0
                    end_y = int_distance_value
                elif int_direction_value == 2:
                    print('ATM Top Right')
                    start_x = 0
                    start_y = 0
                    print('ATM Top Right END')
                    end_x = 0
                    end_y = int_distance_value
                elif int_direction_value == 3:
                    print('ATM Right')
                    start_x = 0
                    start_y = 0
                    print('ATM Right END')
                    end_x = int_distance_value
                    end_y = int_distance_value
                elif int_direction_value == 4:
                    print('ATM Bottom Right')
                    start_x = 0
                    start_y = 0
                    print('ATM Bottom Right END')
                    end_x = int_distance_value
                    end_y = 0
                elif int_direction_value == 5:
                    print('ATM Down')
                    start_x = 0
                    start_y = int_distance_value
                    print('ATM Down END')
                    end_x = int_distance_value
                    end_y = 0
                elif int_direction_value == 6:
                    print('ATM Bottom Left')
                    start_x = int_distance_value
                    start_y = int_distance_value
                    print('ATM Bottom Left END')
                    end_x = int_distance_value
                    end_y = 0
                elif int_direction_value == 7:
                    print('ATM Left')
                    start_x = int_distance_value
                    start_y = int_distance_value
                    print('ATM Left END')
                    end_x = 0
                    end_y = 0
                else:
                    print('ATM Top Left')
                    start_x = int_distance_value
                    start_y = int_distance_value
                    print('ATM Top Left END')
                    end_x = 0
                    end_y = int_distance_value
                for phantom_item in phantom_res_list:
                    if int(start_x) == phantom_item[0] and int(start_y) == phantom_item[1]:
                        start_vib_list.append(int(start_x))
                        start_vib_list.append(int(start_y))
                        start_vib_list.append(phantom_item[2])
                        start_vib_list.append(phantom_item[3])
                        start_vib_list.append(phantom_item[4])
                        start_vib_list.append(phantom_item[5])
                start_vib_list.append(vib_duration)
                for phantom_item in phantom_res_list:
                    if int(end_x) == phantom_item[0] and int(end_y) == phantom_item[1]:
                        end_vib_list.append(int(end_x))
                        end_vib_list.append(int(end_y))
                        end_vib_list.append(phantom_item[2])
                        end_vib_list.append(phantom_item[3])
                        end_vib_list.append(phantom_item[4])
                        end_vib_list.append(phantom_item[5])
                end_vib_list.append(vib_duration)

                time_SOA = generate_SOA(int(duration_value), vib_duration)

                try:
                    _thread.start_new_thread(generate_atm_arduino, (start_vib_list, end_vib_list, time_SOA))
                except:
                    print('ATM Error!')

                flag_atm = flag_atm + 1
            else:
                print('Max ATM Value')

    btn_technique_frame = tk.Frame(root)
    btn_technique_frame.pack(fill=tk.X)
    btn_start_vib = tk.Button(btn_technique_frame, text='Start Vibration', width=32, height=3, fg='white', bg='green',
                              font=("Helvetica", 11), command=click_btn_start_vib)
    btn_start_vib.pack()

    result_frame = tk.Frame(root)
    result_frame.pack(fill=tk.X)
    v_result = tk.StringVar()
    label_result = tk.Label(result_frame, textvariable=v_result, width=30, height=3, font=("Helvetica", 11))
    label_result.pack()

    response_frame = tk.Frame(root)
    response_frame.pack(fill=tk.X)
    label_response = tk.Label(response_frame, text='Response: ', font=("Helvetica", 11))
    label_response.grid(row=0, column=0)
    v_response = tk.IntVar()
    v_response.set(1)
    tk.Radiobutton(response_frame, text='1: Up', variable=v_response, value=1, font=("Helvetica", 11)).grid(row=0,
                                                                                                            column=1,
                                                                                                            ipadx=10)
    tk.Radiobutton(response_frame, text='2: Top Right', variable=v_response, value=2, font=("Helvetica", 11)).grid(
        row=0,
        column=2,
        ipadx=10)
    tk.Radiobutton(response_frame, text='3: Right', variable=v_response, value=3, font=("Helvetica", 11)).grid(row=0,
                                                                                                               column=3,
                                                                                                               ipadx=10)
    tk.Radiobutton(response_frame, text='4: Bottom Right', variable=v_response, value=4, font=("Helvetica", 11)).grid(
        row=0,
        column=4,
        ipadx=10)
    tk.Radiobutton(response_frame, text='5: Down', variable=v_response, value=5, font=("Helvetica", 11)).grid(row=2,
                                                                                                              column=1,
                                                                                                              ipadx=10)
    tk.Radiobutton(response_frame, text='6: Bottom Left', variable=v_response, value=6, font=("Helvetica", 11)).grid(
        row=2,
        column=2,
        ipadx=10)
    tk.Radiobutton(response_frame, text='7: Left', variable=v_response, value=7, font=("Helvetica", 11)).grid(row=2,
                                                                                                              column=3,
                                                                                                              ipadx=10)
    tk.Radiobutton(response_frame, text='8: Top Left', variable=v_response, value=8, font=("Helvetica", 11)).grid(row=2,
                                                                                                                  column=4,
                                                                                                                  ipadx=10)

    def click_save_button():
        final_result = []
        participant_value = txt_participant.get()
        final_result.append(participant_value)
        temp_result_arr = v_result.get().strip('(').strip(')').split(', ')
        for item in temp_result_arr:
            final_result.append(item.strip('\''))
        order_expe_value = int(temp_result_arr[-1].strip('\''))
        order_real_value = int(v_response.get())
        final_result.append(order_real_value)
        if order_expe_value == order_real_value:
            final_result.append(1)
        else:
            final_result.append(0)
        write_csv(final_result)

    response_button_frame = tk.Frame(root)
    response_button_frame.pack(fill=tk.X)
    btn_response = tk.Button(response_button_frame, text='Save Result', width=32, height=3, fg='white', bg='green',
                             font=("Helvetica", 11), command=click_save_button)
    btn_response.pack()

    root.mainloop()


vibration_duration_compare_ui()

