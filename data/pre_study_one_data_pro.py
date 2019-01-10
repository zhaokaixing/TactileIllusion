import os

def read_data_file(data_file_path):
    with open(data_file_path) as f:
        res = []
        for line in f:
            res.append(int(line.strip()))
        return res

def generate_file_path_list(file_path):
    file_name_list = []
    res_list = []
    for root, dirs, files in os.walk(file_path):
        file_name_list = files
    for file_name in file_name_list:
        complete_file_path = file_path + file_name
        res_file = read_data_file(complete_file_path)
        res_list.append(res_file)
    return res_list

def calculate_precision(list1, list2):
    res_bool_list = []
    for i in range(0, 10):
        if list1[i] == list2[i]:
            res_bool_list.append(1)
        else:
            res_bool_list.append(0)
    count = 0
    for i_bool in res_bool_list:
        if i_bool == 1:
            count = count + 1
    return count/len(res_bool_list)

user_1_order_hand = generate_file_path_list('C:\\Users\\kzhao\\Desktop\\ProjectTactileIllusion\\PreStudy\\DataPreStudy1\\Hand\\User1\\Order\\')
user_1_res_hand = generate_file_path_list('C:\\Users\\kzhao\\Desktop\\ProjectTactileIllusion\\PreStudy\\DataPreStudy1\\Hand\\User1\\Res\\')

precision_list = []
for i in range(0, 8):
    precision = calculate_precision(user_1_order_hand[i], user_1_res_hand[i])
    precision_list.append(precision)
print(precision_list)

user_1_order_forearm = generate_file_path_list('C:\\Users\\kzhao\\Desktop\\ProjectTactileIllusion\\PreStudy\\DataPreStudy1\\Forearm\\User1\\Order\\')
user_1_res_forearm = generate_file_path_list('C:\\Users\\kzhao\\Desktop\\ProjectTactileIllusion\\PreStudy\\DataPreStudy1\\Forearm\\User1\\Res\\')

precision_list = []
for i in range(0, 8):
    precision = calculate_precision(user_1_order_forearm[i], user_1_res_forearm[i])
    precision_list.append(precision)
print(precision_list)

