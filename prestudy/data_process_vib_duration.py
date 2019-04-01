import csv


# Function to count the number of correct answers and then calculate the accuracy
def calculate_precision(data_list):
    len_list = len(data_list)
    count = 0
    for item in data_list:
        if item[-1] == '1':
            count = count + 1
    return count/len_list


# Main function for data processing
def process_data_participant():
    final_svp_results_50 = []
    final_atm_results_50 = []
    final_svp_results_150 = []
    final_atm_results_150 = []
    final_svp_results_200 = []
    final_atm_results_200 = []
    final_svp_results_250 = []
    final_atm_results_250 = []
    final_svp_results_350 = []
    final_atm_results_350 = []

    with open('C:\\Users\\kzhao\\PycharmProjects\\TactileIllusion\\prestudy\\vibration_duration_results_square.csv', 'r') as data_file:
        lines = csv.reader(data_file)
        data_list = list(lines)
        duration_350_SVP_list_p1 = []
        duration_350_ATM_list_p1 = []
        duration_250_SVP_list_p1 = []
        duration_250_ATM_list_p1 = []
        duration_200_SVP_list_p1 = []
        duration_200_ATM_list_p1 = []
        duration_150_SVP_list_p1 = []
        duration_150_ATM_list_p1 = []
        duration_50_SVP_list_p1 = []
        duration_50_ATM_list_p1 = []

        duration_350_SVP_list_p2 = []
        duration_350_ATM_list_p2 = []
        duration_250_SVP_list_p2 = []
        duration_250_ATM_list_p2 = []
        duration_200_SVP_list_p2 = []
        duration_200_ATM_list_p2 = []
        duration_150_SVP_list_p2 = []
        duration_150_ATM_list_p2 = []
        duration_50_SVP_list_p2 = []
        duration_50_ATM_list_p2 = []

        duration_350_SVP_list_p3 = []
        duration_350_ATM_list_p3 = []
        duration_250_SVP_list_p3 = []
        duration_250_ATM_list_p3 = []
        duration_200_SVP_list_p3 = []
        duration_200_ATM_list_p3 = []
        duration_150_SVP_list_p3 = []
        duration_150_ATM_list_p3 = []
        duration_50_SVP_list_p3 = []
        duration_50_ATM_list_p3 = []

        duration_350_SVP_list_p4 = []
        duration_350_ATM_list_p4 = []
        duration_250_SVP_list_p4 = []
        duration_250_ATM_list_p4 = []
        duration_200_SVP_list_p4 = []
        duration_200_ATM_list_p4 = []
        duration_150_SVP_list_p4 = []
        duration_150_ATM_list_p4 = []
        duration_50_SVP_list_p4 = []
        duration_50_ATM_list_p4 = []

        for item in data_list:
            if item[1] == '350' and item[2] == 'SVP' and item[0] == 'P1':
                duration_350_SVP_list_p1.append(item)
            if item[1] == '350' and item[2] == 'ATM' and item[0] == 'P1':
                duration_350_ATM_list_p1.append(item)
            if item[1] == '250' and item[2] == 'SVP' and item[0] == 'P1':
                duration_250_SVP_list_p1.append(item)
            if item[1] == '250' and item[2] == 'ATM' and item[0] == 'P1':
                duration_250_ATM_list_p1.append(item)
            if item[1] == '200' and item[2] == 'SVP' and item[0] == 'P1':
                duration_200_SVP_list_p1.append(item)
            if item[1] == '200' and item[2] == 'ATM' and item[0] == 'P1':
                duration_200_ATM_list_p1.append(item)
            if item[1] == '150' and item[2] == 'SVP' and item[0] == 'P1':
                duration_150_SVP_list_p1.append(item)
            if item[1] == '150' and item[2] == 'ATM' and item[0] == 'P1':
                duration_150_ATM_list_p1.append(item)
            if item[1] == '50' and item[2] == 'SVP' and item[0] == 'P1':
                duration_50_SVP_list_p1.append(item)
            if item[1] == '50' and item[2] == 'ATM' and item[0] == 'P1':
                duration_50_ATM_list_p1.append(item)

            if item[1] == '350' and item[2] == 'SVP' and item[0] == 'P2':
                duration_350_SVP_list_p2.append(item)
            if item[1] == '350' and item[2] == 'ATM' and item[0] == 'P2':
                duration_350_ATM_list_p2.append(item)
            if item[1] == '250' and item[2] == 'SVP' and item[0] == 'P2':
                duration_250_SVP_list_p2.append(item)
            if item[1] == '250' and item[2] == 'ATM' and item[0] == 'P2':
                duration_250_ATM_list_p2.append(item)
            if item[1] == '200' and item[2] == 'SVP' and item[0] == 'P2':
                duration_200_SVP_list_p2.append(item)
            if item[1] == '200' and item[2] == 'ATM' and item[0] == 'P2':
                duration_200_ATM_list_p2.append(item)
            if item[1] == '150' and item[2] == 'SVP' and item[0] == 'P2':
                duration_150_SVP_list_p2.append(item)
            if item[1] == '150' and item[2] == 'ATM' and item[0] == 'P2':
                duration_150_ATM_list_p2.append(item)
            if item[1] == '50' and item[2] == 'SVP' and item[0] == 'P2':
                duration_50_SVP_list_p2.append(item)
            if item[1] == '50' and item[2] == 'ATM' and item[0] == 'P2':
                duration_50_ATM_list_p2.append(item)

            if item[1] == '350' and item[2] == 'SVP' and item[0] == 'P3':
                duration_350_SVP_list_p3.append(item)
            if item[1] == '350' and item[2] == 'ATM' and item[0] == 'P3':
                duration_350_ATM_list_p3.append(item)
            if item[1] == '250' and item[2] == 'SVP' and item[0] == 'P3':
                duration_250_SVP_list_p3.append(item)
            if item[1] == '250' and item[2] == 'ATM' and item[0] == 'P3':
                duration_250_ATM_list_p3.append(item)
            if item[1] == '200' and item[2] == 'SVP' and item[0] == 'P3':
                duration_200_SVP_list_p3.append(item)
            if item[1] == '200' and item[2] == 'ATM' and item[0] == 'P3':
                duration_200_ATM_list_p3.append(item)
            if item[1] == '150' and item[2] == 'SVP' and item[0] == 'P3':
                duration_150_SVP_list_p3.append(item)
            if item[1] == '150' and item[2] == 'ATM' and item[0] == 'P3':
                duration_150_ATM_list_p3.append(item)
            if item[1] == '50' and item[2] == 'SVP' and item[0] == 'P3':
                duration_50_SVP_list_p3.append(item)
            if item[1] == '50' and item[2] == 'ATM' and item[0] == 'P3':
                duration_50_ATM_list_p3.append(item)

            if item[1] == '350' and item[2] == 'SVP' and item[0] == 'P4':
                duration_350_SVP_list_p4.append(item)
            if item[1] == '350' and item[2] == 'ATM' and item[0] == 'P4':
                duration_350_ATM_list_p4.append(item)
            if item[1] == '250' and item[2] == 'SVP' and item[0] == 'P4':
                duration_250_SVP_list_p4.append(item)
            if item[1] == '250' and item[2] == 'ATM' and item[0] == 'P4':
                duration_250_ATM_list_p4.append(item)
            if item[1] == '200' and item[2] == 'SVP' and item[0] == 'P4':
                duration_200_SVP_list_p4.append(item)
            if item[1] == '200' and item[2] == 'ATM' and item[0] == 'P4':
                duration_200_ATM_list_p4.append(item)
            if item[1] == '150' and item[2] == 'SVP' and item[0] == 'P4':
                duration_150_SVP_list_p4.append(item)
            if item[1] == '150' and item[2] == 'ATM' and item[0] == 'P4':
                duration_150_ATM_list_p4.append(item)
            if item[1] == '50' and item[2] == 'SVP' and item[0] == 'P4':
                duration_50_SVP_list_p4.append(item)
            if item[1] == '50' and item[2] == 'ATM' and item[0] == 'P4':
                duration_50_ATM_list_p4.append(item)

        final_svp_results_50.append(calculate_precision(duration_50_SVP_list_p1))
        final_svp_results_50.append(calculate_precision(duration_50_SVP_list_p2))
        final_svp_results_50.append(calculate_precision(duration_50_SVP_list_p3))
        final_svp_results_50.append(calculate_precision(duration_50_SVP_list_p4))
        final_atm_results_50.append(calculate_precision(duration_50_ATM_list_p1))
        final_atm_results_50.append(calculate_precision(duration_50_ATM_list_p2))
        final_atm_results_50.append(calculate_precision(duration_50_ATM_list_p3))
        final_atm_results_50.append(calculate_precision(duration_50_ATM_list_p4))

        final_svp_results_150.append(calculate_precision(duration_150_SVP_list_p1))
        final_svp_results_150.append(calculate_precision(duration_150_SVP_list_p2))
        final_svp_results_150.append(calculate_precision(duration_150_SVP_list_p3))
        final_svp_results_150.append(calculate_precision(duration_150_SVP_list_p4))
        final_atm_results_150.append(calculate_precision(duration_150_ATM_list_p1))
        final_atm_results_150.append(calculate_precision(duration_150_ATM_list_p2))
        final_atm_results_150.append(calculate_precision(duration_150_ATM_list_p3))
        final_atm_results_150.append(calculate_precision(duration_150_ATM_list_p4))

        final_svp_results_200.append(calculate_precision(duration_200_SVP_list_p1))
        final_svp_results_200.append(calculate_precision(duration_200_SVP_list_p2))
        final_svp_results_200.append(calculate_precision(duration_200_SVP_list_p3))
        final_svp_results_200.append(calculate_precision(duration_200_SVP_list_p4))
        final_atm_results_200.append(calculate_precision(duration_200_ATM_list_p1))
        final_atm_results_200.append(calculate_precision(duration_200_ATM_list_p2))
        final_atm_results_200.append(calculate_precision(duration_200_ATM_list_p3))
        final_atm_results_200.append(calculate_precision(duration_200_ATM_list_p4))

        final_svp_results_250.append(calculate_precision(duration_250_SVP_list_p1))
        final_svp_results_250.append(calculate_precision(duration_250_SVP_list_p2))
        final_svp_results_250.append(calculate_precision(duration_250_SVP_list_p3))
        final_svp_results_250.append(calculate_precision(duration_250_SVP_list_p4))
        final_atm_results_250.append(calculate_precision(duration_250_ATM_list_p1))
        final_atm_results_250.append(calculate_precision(duration_250_ATM_list_p2))
        final_atm_results_250.append(calculate_precision(duration_250_ATM_list_p3))
        final_atm_results_250.append(calculate_precision(duration_250_ATM_list_p4))

        final_svp_results_350.append(calculate_precision(duration_350_SVP_list_p1))
        final_svp_results_350.append(calculate_precision(duration_350_SVP_list_p2))
        final_svp_results_350.append(calculate_precision(duration_350_SVP_list_p3))
        final_svp_results_350.append(calculate_precision(duration_350_SVP_list_p4))
        final_atm_results_350.append(calculate_precision(duration_350_ATM_list_p1))
        final_atm_results_350.append(calculate_precision(duration_350_ATM_list_p2))
        final_atm_results_350.append(calculate_precision(duration_350_ATM_list_p3))
        final_atm_results_350.append(calculate_precision(duration_350_ATM_list_p4))

    print(50)
    print(final_svp_results_50)
    print(final_atm_results_50)
    print(150)
    print(final_svp_results_150)
    print(final_atm_results_150)
    print(200)
    print(final_svp_results_200)
    print(final_atm_results_200)
    print(250)
    print(final_svp_results_250)
    print(final_atm_results_250)
    print(350)
    print(final_svp_results_350)
    print(final_atm_results_350)


process_data_participant()
