import tkinter as tk
from map_image.map_img_operation import receive_from_infra

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
        print('Connection with infrared tool error!')

    btn_start = tk.Button(main_frame, text='Start', bg='green', width=30, height=5, command=start_click_cmd)
    btn_start.grid(row=0, column=4)

    figure_frame = tk.Frame(root, bg='white')
    figure_frame.pack(fill=tk.X)
    image_path = tk.PhotoImage(file='C:\\Users\\kzhao\\PycharmProjects\\TactileIllusion\\map_image\\direc.png')
    fig_image = tk.Label(figure_frame, image=image_path, bg='white').pack()

    root.mainloop()


infra_map_interface()