import matplotlib.pyplot as plt
import numpy as np
'''
This file realize the Tactile Brush algorithm
'''

def calculate_eucli_distance(x_1, y_1, x_2, y_2):
    return np.sqrt(np.square(x_1 - x_2) + np.square(y_1 - y_2))

'''
Function used to calculate related vibrations to generate Phantom Sensation
Parameter intensity_v represents the expected intensity of PS
x_1, y_1 is the coordinates of the first real actuator
x_2, y_2 is the coordinates of the second real actuator
x_v, y_v is the coordinates of PS
'''
def generate_phantom_vib(intensity_v, x_1, y_1, x_2, y_2, x_v, y_v):
    d_1 = calculate_eucli_distance(x_1, y_1, x_v, y_v)
    d_2 = calculate_eucli_distance(x_2, y_2, x_v, y_v)
    intensity_1 = np.sqrt(d_2 / (d_1 + d_2)) * intensity_v
    intensity_2 = np.sqrt(d_1 / (d_1 + d_2)) * intensity_v
    return intensity_1, intensity_2

'''
Function to calculate the SOA value, this value is calculated according to the 2-actuator layout algo
Parameter T is the total time to finish ATM
duration is the vibration time of each actuator
'''
def generate_SOA(T, duration):
    SOA = T - duration
    return SOA

'''
Function to pre-calculate all possibilities of a PS which can be used to as PS directly or to construct ATM
Parameter inten is the expected intensity of vibration, distance is the distance between 2 actuators and T is
the total time to finish one operation
'''
def generate_tactile_brush_results(inten, distance, T):
    tactile_record = []

    duration = (T - 47.3) / 1.32

    for y_end in (0, distance):
        if y_end == distance:
            x_end = 1
            while x_end < distance:
                record_temp = []
                inten_1, inten_2 = generate_phantom_vib(inten, 0, distance, distance, distance, x_end, y_end)
                record_temp.append(x_end)
                record_temp.append(y_end)
                record_temp.append(inten_1)
                record_temp.append(inten_2)
                tactile_record.append(record_temp)
                x_end = x_end + 1

        if y_end == 0:
            x_end = 1
            while x_end < distance:
                record_temp = []
                inten_1, inten_2 = generate_phantom_vib(inten, 0, 0, distance, 0, x_end, y_end)
                record_temp.append(x_end)
                record_temp.append(y_end)
                record_temp.append(inten_1)
                record_temp.append(inten_2)
                tactile_record.append(record_temp)
                x_end = x_end + 1

    for x_end in (0, distance):
        if x_end == distance:
            y_end = 1
            while y_end < distance:
                record_temp = []
                inten_1, inten_2 = generate_phantom_vib(inten, distance, distance, distance, 0, x_end, y_end)
                record_temp.append(x_end)
                record_temp.append(y_end)
                record_temp.append(inten_1)
                record_temp.append(inten_2)
                tactile_record.append(record_temp)
                y_end = y_end + 1

        if x_end == 0:
            y_end = 1
            while y_end < distance:
                record_temp = []
                inten_1, inten_2 = generate_phantom_vib(inten, 0, distance, 0, 0, x_end, y_end)
                record_temp.append(x_end)
                record_temp.append(y_end)
                record_temp.append(inten_1)
                record_temp.append(inten_2)
                tactile_record.append(record_temp)
                y_end = y_end + 1

    final_vib_res = []

    '''
    The data structure of final results -- x, y, intensity_vib1, intensity_vib2, intensity_vib3, intensity_vib4
    '''
    for i in tactile_record:
        if i[0] >= 0 and i[0] <= distance and i[1] == 0:
            temp_list_1 = []
            temp_list_1.append(i[0])
            temp_list_1.append(i[1])
            temp_list_1.append(i[2])
            temp_list_1.append(i[3])
            temp_list_1.append(0)
            temp_list_1.append(0)
            final_vib_res.append(temp_list_1)

        if i[0] >= 0 and i[0] <= distance and i[1] == distance:
            temp_list_2 = []
            temp_list_2.append(i[0])
            temp_list_2.append(i[1])
            temp_list_2.append(0)
            temp_list_2.append(0)
            temp_list_2.append(i[3])
            temp_list_2.append(i[2])
            final_vib_res.append(temp_list_2)

        if i[1] >= 0 and i[1] <= distance and i[0] == 0:
            temp_list_3 = []
            temp_list_3.append(i[0])
            temp_list_3.append(i[1])
            temp_list_3.append(i[3])
            temp_list_3.append(0)
            temp_list_3.append(0)
            temp_list_3.append(i[2])
            final_vib_res.append(temp_list_3)

        if i[1] >= 0 and i[1] <= distance and i[0] == distance:
            temp_list_4 = []
            temp_list_4.append(i[0])
            temp_list_4.append(i[1])
            temp_list_4.append(0)
            temp_list_4.append(i[3])
            temp_list_4.append(i[2])
            temp_list_4.append(0)
            final_vib_res.append(temp_list_4)

    '''
    Add 4 real vibrator which can be also used as end points
    '''
    vib1_end = [0, 0, inten, 0, 0, 0]
    vib2_end = [distance, 0, 0, inten, 0, 0]
    vib3_end = [distance, distance, 0, 0, inten, 0]
    vib4_end = [0, distance, 0, 0, 0, inten]
    final_vib_res.append(vib1_end)
    final_vib_res.append(vib2_end)
    final_vib_res.append(vib3_end)
    final_vib_res.append(vib4_end)

    return final_vib_res, duration