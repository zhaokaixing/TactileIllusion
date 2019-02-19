from pyfirmata import Arduino, util
import time
import _thread
'''
Author: Kaixing ZHAO
This file is used to connect and send commands to Arduino
'''

'''
Default port is COM5, default output: 3, 5, 9, 11
'''
board = Arduino('COM5')
#board = Arduino('COM6')
ana_out_1 = board.get_pin('d:3:p')
ana_out_2 = board.get_pin('d:5:p')
ana_out_3 = board.get_pin('d:9:p')
ana_out_4 = board.get_pin('d:11:p')
print('Arduino ready!')

'''
Function to generate vibration on port 3
'''
def generate_single_vibration_arduino():
    print('Single Vibration')
    ana_out_4.write(1)

def generate_all_vibration_arduino():
    print('All Vibration')
    ana_out_1.write(0.75)
    ana_out_2.write(0.75)
    ana_out_3.write(0.75)
    ana_out_4.write(0.75)

def stop_all_vibration_arduino():
    print('Stop All Vibration')
    ana_out_1.write(0)
    ana_out_2.write(0)
    ana_out_3.write(0)
    ana_out_4.write(0)

'''
Function to stop vibration on port 3
'''
def stop_single_vibration_arduino():
    print('Stop Single Vibration')
    ana_out_4.write(0)

'''
Function used to generate Phantom Sensation, parameter phantom_result is used to receive 
calculation result of Phantom Sensation
'''
def generate_phantom_arduino(phantom_result):
    print('Phantom Sensation')
    print(phantom_result)
    duration = phantom_result[6]
    #print('66666    ' + str(phantom_result[2]))
    ana_out_1.write(phantom_result[2])
    ana_out_2.write(phantom_result[3])
    ana_out_3.write(phantom_result[4])
    ana_out_4.write(phantom_result[5])
    time.sleep(duration/1000)

    ana_out_1.write(0)
    ana_out_2.write(0)
    ana_out_3.write(0)
    ana_out_4.write(0)

'''
Function used to generate Apparent Tactile Motion, parameter atm_result_start represents
initial state of actuators, atm_result_end represents end state, SOA represents the SOA value
to preserve ATM
'''
def generate_atm_arduino(atm_result_start, atm_result_end, SOA):
    print('Apparent Tactile Motion')

    duration = atm_result_end[6]
    final_vib = []
    start_position = 1
    for i in [2, 3, 4, 5]:
        if atm_result_start[i] > 0:
            final_vib.append(atm_result_start[i])
            start_position = i - 1
        else:
            final_vib.append(atm_result_end[i])
    print(final_vib)
    print('-----------------------------------------')

    if start_position == 1:
        for times in range(0, 2):
            if SOA <= duration:
                ana_out_1.write(final_vib[0])
                time.sleep(SOA / 1000)
                # ana_out_1.write(final_vib[0])
                ana_out_2.write(final_vib[1])
                ana_out_3.write(final_vib[2])
                ana_out_4.write(final_vib[3])
                time.sleep((duration - SOA) / 1000)
                ana_out_1.write(0)
                ana_out_2.write(final_vib[1])
                ana_out_3.write(final_vib[2])
                ana_out_4.write(final_vib[3])
                time.sleep(SOA / 1000)
                ana_out_2.write(0)
                ana_out_3.write(0)
                ana_out_4.write(0)
            else:
                ana_out_1.write(final_vib[0])
                time.sleep(duration / 1000)
                ana_out_1.write(0)
                time.sleep((SOA - duration) / 1000)
                # ana_out_1.write(final_vib[0])
                ana_out_2.write(final_vib[1])
                ana_out_3.write(final_vib[2])
                ana_out_4.write(final_vib[3])
                time.sleep(duration / 1000)
                ana_out_2.write(0)
                ana_out_3.write(0)
                ana_out_4.write(0)

            time.sleep(0.5)

    if start_position == 2:
        for times in range(0, 2):
            if SOA <= duration:
                ana_out_2.write(final_vib[1])
                time.sleep(SOA / 1000)
                # ana_out_1.write(final_vib[0])
                ana_out_1.write(final_vib[0])
                ana_out_3.write(final_vib[2])
                ana_out_4.write(final_vib[3])
                time.sleep((duration - SOA) / 1000)
                ana_out_2.write(0)
                ana_out_1.write(final_vib[0])
                ana_out_3.write(final_vib[2])
                ana_out_4.write(final_vib[3])
                time.sleep(SOA / 1000)
                ana_out_1.write(0)
                ana_out_3.write(0)
                ana_out_4.write(0)
            else:
                ana_out_2.write(final_vib[0])
                time.sleep(duration / 1000)
                ana_out_2.write(0)
                time.sleep((SOA - duration) / 1000)
                # ana_out_1.write(final_vib[0])
                ana_out_1.write(final_vib[0])
                ana_out_3.write(final_vib[2])
                ana_out_4.write(final_vib[3])
                time.sleep(duration / 1000)
                ana_out_1.write(0)
                ana_out_3.write(0)
                ana_out_4.write(0)

            time.sleep(0.5)

    if start_position == 3:
        for times in range(0, 2):
            if SOA <= duration:
                ana_out_3.write(final_vib[2])
                time.sleep(SOA / 1000)
                # ana_out_1.write(final_vib[0])
                ana_out_1.write(final_vib[0])
                ana_out_2.write(final_vib[1])
                ana_out_4.write(final_vib[3])
                time.sleep((duration - SOA) / 1000)
                ana_out_3.write(0)
                ana_out_1.write(final_vib[0])
                ana_out_2.write(final_vib[1])
                ana_out_4.write(final_vib[3])
                time.sleep(SOA / 1000)
                ana_out_1.write(0)
                ana_out_2.write(0)
                ana_out_4.write(0)
            else:
                ana_out_3.write(final_vib[0])
                time.sleep(duration / 1000)
                ana_out_3.write(0)
                time.sleep((SOA - duration) / 1000)
                # ana_out_1.write(final_vib[0])
                ana_out_1.write(final_vib[0])
                ana_out_2.write(final_vib[1])
                ana_out_4.write(final_vib[3])
                time.sleep(duration / 1000)
                ana_out_1.write(0)
                ana_out_2.write(0)
                ana_out_4.write(0)

            time.sleep(0.5)

    if start_position == 4:
        for times in range(0, 2):
            if SOA <= duration:
                ana_out_4.write(final_vib[3])
                time.sleep(SOA / 1000)
                # ana_out_1.write(final_vib[0])
                ana_out_1.write(final_vib[0])
                ana_out_2.write(final_vib[1])
                ana_out_3.write(final_vib[2])
                time.sleep((duration - SOA) / 1000)
                ana_out_4.write(0)
                ana_out_1.write(final_vib[0])
                ana_out_2.write(final_vib[1])
                ana_out_3.write(final_vib[2])
                time.sleep(SOA / 1000)
                ana_out_1.write(0)
                ana_out_2.write(0)
                ana_out_3.write(0)
            else:
                ana_out_4.write(final_vib[0])
                time.sleep(duration / 1000)
                ana_out_4.write(0)
                time.sleep((SOA - duration) / 1000)
                # ana_out_1.write(final_vib[0])
                ana_out_1.write(final_vib[0])
                ana_out_2.write(final_vib[1])
                ana_out_3.write(final_vib[2])
                time.sleep(duration / 1000)
                ana_out_1.write(0)
                ana_out_2.write(0)
                ana_out_3.write(0)

            time.sleep(0.5)

    generate_single_vibration_arduino()

def stop_arduino():
    board.exit()