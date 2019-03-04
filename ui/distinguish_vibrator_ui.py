import tkinter as tk
from ardui.arduino_connect import generate_vibration_simple
import _thread

def distinguish_vibrator_ui_main():
    root = tk.Tk()
    root.minsize(800, 350)
    root.maxsize(800, 350)
    root.title('Overview Test UI')

    main_frame = tk.Frame(root, bg='white')
    main_frame.pack(fill=tk.X)

    tac_1_check_btn = tk.IntVar()
    tac_2_check_btn = tk.IntVar()
    tac_3_check_btn = tk.IntVar()
    tac_4_check_btn = tk.IntVar()

    def click_btn_vib():
        vib_list = []
        vib_list.append(tac_1_check_btn.get())
        vib_list.append(tac_2_check_btn.get())
        vib_list.append(tac_3_check_btn.get())
        vib_list.append(tac_4_check_btn.get())
        print(vib_list)

        try:
            _thread.start_new_thread(generate_vibration_simple, (vib_list,))
        except:
            print('Infrared Single Vibration error')

    vibrator = tk.Label(main_frame, text='Vibrator: ', bg='white').grid(row=0, column=0)
    vib_1 = tk.Checkbutton(main_frame, bg='white', text='Tactor 1', variable=tac_1_check_btn, onvalue=1, offvalue=0, width=20)
    vib_1.grid(row=0, column=1)
    vib_2 = tk.Checkbutton(main_frame, bg='white', text='Tactor 2', variable=tac_2_check_btn, onvalue=1, offvalue=0, width=20)
    vib_2.grid(row=0, column=2)
    vib_3 = tk.Checkbutton(main_frame, bg='white', text='Tactor 3', variable=tac_3_check_btn, onvalue=1, offvalue=0, width=20)
    vib_3.grid(row=0, column=3)
    vib_4 = tk.Checkbutton(main_frame, bg='white', text='Tactor 4', variable=tac_4_check_btn, onvalue=1, offvalue=0, width=20)
    vib_4.grid(row=0, column=4)

    btn_frame = tk.Frame(root, bg='white')
    btn_frame.pack(fill=tk.X)
    btn_vib = tk.Button(btn_frame, text='Start Vibration', width=42, height=5, bg='white', command=click_btn_vib)
    btn_vib.pack()

    root.mainloop()


distinguish_vibrator_ui_main()
