import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def calculate_precision_dis(data_list):
    len_list = len(data_list)
    #print(len_list)
    count = 0
    for item in data_list:
        if item[-1] == '1':
            count = count + 1
    #print(count)
    print(count/len_list)

def calculate_precision_dis_per_user(data_list):
    pre_list = []
    count_1 = 0
    count_2 = 0
    count_3 = 0
    for item in data_list:
        if item[-1] == '1' and item[1] == '1':
            count_1 = count_1 + 1
        if item[-1] == '1' and item[1] == '2':
            count_2 = count_2 + 1
        if item[-1] == '1' and item[1] == '3':
            count_3 = count_3 + 1
    pre_list.append(count_1 / 10)
    pre_list.append(count_2 / 10)
    pre_list.append(count_3 / 10)

    return pre_list

def calculate_precision_zone_per_user(data_list):
    pre_list = []
    count_1 = 0
    count_2 = 0
    count_3 = 0
    for item in data_list:
        if item[-1] == '1' and item[1] == '1':
            count_1 = count_1 + 1
        if item[-1] == '1' and item[1] == '2':
            count_2 = count_2 + 1
        if item[-1] == '1' and item[1] == '3':
            count_3 = count_3 + 1
    pre_list.append(count_1 / 16)
    pre_list.append(count_2 / 16)
    pre_list.append(count_3 / 16)

    return pre_list

def write_csv(list, file_name):
    csv_file = open(file_name, 'a+')
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    csv_writer.writerow(list)
    csv_file.close()

def process_data():
    with open('C:\\Users\\kzhao\\PycharmProjects\\TactileIllusion\\ui\\records.csv', 'r') as data_file:
        lines = csv.reader(data_file)
        data_list = list(lines)
        #print(len(data_list))

        p_1_hand_list = []
        p_2_hand_list = []
        p_3_hand_list = []
        p_1_arm_list = []
        p_2_arm_list = []
        p_3_arm_list = []

        d_10_hand_list = []
        d_20_hand_list = []
        d_30_hand_list = []
        d_40_hand_list = []
        d_50_hand_list = []
        d_60_hand_list = []
        d_70_hand_list = []
        d_80_hand_list = []
        d_10_arm_list = []
        d_20_arm_list = []
        d_30_arm_list = []
        d_40_arm_list = []
        d_50_arm_list = []
        d_60_arm_list = []
        d_70_arm_list = []
        d_80_arm_list = []

        z_1_hand_list = []
        z_2_hand_list = []
        z_3_hand_list = []
        z_4_hand_list = []
        z_5_hand_list = []
        z_1_arm_list = []
        z_2_arm_list = []
        z_3_arm_list = []
        z_4_arm_list = []
        z_5_arm_list = []

        for item in data_list:
            if item[5] == '1' and item[3] == 'Hand':
                z_1_hand_list.append(item)
            if item[5] == '2' and item[3] == 'Hand':
                z_2_hand_list.append(item)
            if item[5] == '3' and item[3] == 'Hand':
                z_3_hand_list.append(item)
            if item[5] == '4' and item[3] == 'Hand':
                z_4_hand_list.append(item)
            if item[5] == '5' and item[3] == 'Hand':
                z_5_hand_list.append(item)
            if item[5] == '1' and item[3] == 'Arm':
                z_1_arm_list.append(item)
            if item[5] == '2' and item[3] == 'Arm':
                z_2_arm_list.append(item)
            if item[5] == '3' and item[3] == 'Arm':
                z_3_arm_list.append(item)
            if item[5] == '4' and item[3] == 'Arm':
                z_4_arm_list.append(item)
            if item[5] == '5' and item[3] == 'Arm':
                z_5_arm_list.append(item)

            if item[1] == '1' and item[3] == 'Hand':
                p_1_hand_list.append(item)
            if item[1] == '2' and item[3] == 'Hand':
                p_2_hand_list.append(item)
            if item[1] == '3' and item[3] == 'Hand':
                p_3_hand_list.append(item)
            if item[1] == '1' and item[3] == 'Arm':
                p_1_arm_list.append(item)
            if item[1] == '2' and item[3] == 'Arm':
                p_2_arm_list.append(item)
            if item[1] == '3' and item[3] == 'Arm':
                p_3_arm_list.append(item)

            if item[3] == 'Hand' and item[4] == '10':
                d_10_hand_list.append(item)
            if item[3] == 'Hand' and item[4] == '20':
                d_20_hand_list.append(item)
            if item[3] == 'Hand' and item[4] == '30':
                d_30_hand_list.append(item)
            if item[3] == 'Hand' and item[4] == '40':
                d_40_hand_list.append(item)
            if item[3] == 'Hand' and item[4] == '50':
                d_50_hand_list.append(item)
            if item[3] == 'Hand' and item[4] == '60':
                d_60_hand_list.append(item)
            if item[3] == 'Hand' and item[4] == '70':
                d_70_hand_list.append(item)
            if item[3] == 'Hand' and item[4] == '80':
                d_80_hand_list.append(item)
            if item[3] == 'Arm' and item[4] == '10':
                d_10_arm_list.append(item)
            if item[3] == 'Arm' and item[4] == '20':
                d_20_arm_list.append(item)
            if item[3] == 'Arm' and item[4] == '30':
                d_30_arm_list.append(item)
            if item[3] == 'Arm' and item[4] == '40':
                d_40_arm_list.append(item)
            if item[3] == 'Arm' and item[4] == '50':
                d_50_arm_list.append(item)
            if item[3] == 'Arm' and item[4] == '60':
                d_60_arm_list.append(item)
            if item[3] == 'Arm' and item[4] == '70':
                d_70_arm_list.append(item)
            if item[3] == 'Arm' and item[4] == '80':
                d_80_arm_list.append(item)

        '''final_pre_list = []
        final_pre_list.append(calculate_precision_dis_per_user(d_10_hand_list))
        final_pre_list.append(calculate_precision_dis_per_user(d_20_hand_list))
        final_pre_list.append(calculate_precision_dis_per_user(d_30_hand_list))
        final_pre_list.append(calculate_precision_dis_per_user(d_40_hand_list))
        final_pre_list.append(calculate_precision_dis_per_user(d_50_hand_list))
        final_pre_list.append(calculate_precision_dis_per_user(d_60_hand_list))
        final_pre_list.append(calculate_precision_dis_per_user(d_70_hand_list))
        final_pre_list.append(calculate_precision_dis_per_user(d_80_hand_list))

        final_pre_list.append(calculate_precision_dis_per_user(d_10_arm_list))
        final_pre_list.append(calculate_precision_dis_per_user(d_20_arm_list))
        final_pre_list.append(calculate_precision_dis_per_user(d_30_arm_list))
        final_pre_list.append(calculate_precision_dis_per_user(d_40_arm_list))
        final_pre_list.append(calculate_precision_dis_per_user(d_50_arm_list))
        final_pre_list.append(calculate_precision_dis_per_user(d_60_arm_list))
        final_pre_list.append(calculate_precision_dis_per_user(d_70_arm_list))
        final_pre_list.append(calculate_precision_dis_per_user(d_80_arm_list))


        for pre_list_item in final_pre_list:
            write_csv(pre_list_item, 'precision_per_distance_user.csv')'''

        final_zone_list = []
        final_zone_list.append(calculate_precision_zone_per_user(z_1_hand_list))
        final_zone_list.append(calculate_precision_zone_per_user(z_2_hand_list))
        final_zone_list.append(calculate_precision_zone_per_user(z_3_hand_list))
        final_zone_list.append(calculate_precision_zone_per_user(z_4_hand_list))
        final_zone_list.append(calculate_precision_zone_per_user(z_5_hand_list))
        final_zone_list.append(calculate_precision_zone_per_user(z_1_arm_list))
        final_zone_list.append(calculate_precision_zone_per_user(z_2_arm_list))
        final_zone_list.append(calculate_precision_zone_per_user(z_3_arm_list))
        final_zone_list.append(calculate_precision_zone_per_user(z_4_arm_list))
        final_zone_list.append(calculate_precision_zone_per_user(z_5_arm_list))

        for zone_list_item in final_zone_list:
            write_csv(zone_list_item, 'precision_per_zone_user.csv')


process_data()
