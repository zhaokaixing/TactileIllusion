from pyfirmata import Arduino, util
import time


board = Arduino('COM5')
ana_out_3 = board.get_pin('d:3:p')
ana_out_2 = board.get_pin('d:5:p')
ana_out_1 = board.get_pin('d:9:p')
ana_out_4 = board.get_pin('d:11:p')
print('Arduino ready!')

def generate_vibration_simple(vib_list, duration):
    if vib_list[0] == 1:
        ana_out_1.write(1)
    elif vib_list[0] == 0:
        ana_out_1.write(0)
    if vib_list[1] == 1:
        ana_out_2.write(1)
    elif vib_list[1] == 0:
        ana_out_2.write(0)
    if vib_list[2] == 1:
        ana_out_3.write(1)
    elif vib_list[2] == 0:
        ana_out_3.write(0)
    if vib_list[3] == 1:
        ana_out_4.write(1)
    elif vib_list[3] == 0:
        ana_out_4.write(0)

    time.sleep(duration / 1000)
    ana_out_1.write(0)
    ana_out_2.write(0)
    ana_out_3.write(0)
    ana_out_4.write(0)


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