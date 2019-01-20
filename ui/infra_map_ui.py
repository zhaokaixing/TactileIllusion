import tkinter as tk

def infra_map_interface():
    root = tk.Tk()
    root.minsize(800, 600)
    root.maxsize(800, 600)
    root.title('Tactile Illusion VS Vibrotactile Patterns -- Using Infrared Tool')
    main_frame = tk.Frame(root, bg='white')
    main_frame.pack(fill=tk.X)

    label_mode = tk.Label(main_frame, text='Mode: ', bg='white', width=20, height=5).grid(row=0, column=0)
    v_mode = tk.StringVar()
    v_mode.set('Illusion')
    tk.Radiobutton(main_frame, text='Tactile Illusion', variable=v_mode, value='Illusion', bg='white', width=20, height=5).grid(row=0, column=1)
    tk.Radiobutton(main_frame, text='Vibrotactile Pattern', variable=v_mode, value='Pattern', bg='white', width=20, height=5).grid(row=0, column=2)

    def start_click_cmd():
        print(v_mode.get())
    btn_start = tk.Button(main_frame, text='Start', bg='green', width=30, height=5, command=start_click_cmd)
    btn_start.grid(row=0, column=4)

    root.mainloop()


infra_map_interface()