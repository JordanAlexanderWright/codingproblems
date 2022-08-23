from day_3_data import parsed_data


# Problem 1
# def get_gamma_rate(data):
#
#     bit_0_count = 0
#     bit_1_count = 0
#
#     gamma_rate = []
#     epsilon_rate = []
#     index = 0
#
#     iteration_count = len(data[0])
#
#     while iteration_count > 0:
#         for byte in data:
#             bit = byte[index]
#             if bit == '0':
#                 bit_0_count += 1
#             else:
#                 bit_1_count += 1
#
#         if bit_0_count > bit_1_count:
#             gamma_rate.append(0)
#             epsilon_rate.append(1)
#         else:
#             gamma_rate.append(1)
#             epsilon_rate.append(0)
#
#         index += 1
#         bit_0_count = 0
#         bit_1_count = 0
#         iteration_count -= 1
#
#     return gamma_rate, epsilon_rate


def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)

    return decimal


# [my_gamma, my_epsilon] = get_gamma_rate(parsed_data)
# power_consumption = (binary_to_decimal(my_gamma) * binary_to_decimal(my_epsilon))
#
# print(power_consumption)
#

# Problem 2
def oxygen_filter(data_set, index, filter_number):

    filtered_list = []

    if len(data_set) == 1:

        return data_set

    for byte in data_set:
        if byte[index] == filter_number:
            filtered_list.append(byte)

    return filtered_list


def co2_filter(data_set, index, filtered_number):
    filtered_list = []

    if len(data_set) == 1:
        # print('its already filtered, dummy')
        return data_set

    for byte in data_set:
        if byte[index] == filtered_number:
            filtered_list.append(byte)

    return filtered_list


def get_gamma_rate(data):

    bit_0_count = 0
    bit_1_count = 0

    gamma_rate = []
    epsilon_rate = []
    index = 0

    iteration_count = len(data[0])

    while iteration_count > 0:
        for byte in data:
            bit = byte[index]

            if bit == '0':
                bit_0_count += 1
            else:
                bit_1_count += 1

        if bit_0_count > bit_1_count:
            gamma_rate.append(0)
            epsilon_rate.append(1)

        if bit_1_count >= bit_0_count:
            gamma_rate.append(1)
            epsilon_rate.append(0)

        index += 1
        bit_0_count = 0
        bit_1_count = 0
        iteration_count -= 1

    return gamma_rate, epsilon_rate


def get_oxygen_rating(data):

    bit_0_count = 0
    bit_1_count = 0

    filtered_list = data
    index = 0

    while len(filtered_list) > 1:
        for byte in filtered_list:

            bit = byte[index]
            if bit == '0':
                bit_0_count += 1
            else:
                bit_1_count += 1

        if bit_0_count > bit_1_count:
            filtered_list = oxygen_filter(filtered_list, index, '0')

        if bit_1_count >= bit_0_count:
            filtered_list = oxygen_filter(filtered_list, index, '1')

        index += 1
        bit_0_count = 0
        bit_1_count = 0

    return filtered_list


def get_co2_rating(data):

    bit_0_count = 0
    bit_1_count = 0

    filtered_list = data
    index = 0

    while len(filtered_list) > 1:
        for byte in filtered_list:

            bit = byte[index]
            if bit == '0':
                bit_0_count += 1
            else:
                bit_1_count += 1

        if bit_0_count > bit_1_count:
            filtered_list = oxygen_filter(filtered_list, index, '1')

        if bit_1_count >= bit_0_count:
            filtered_list = oxygen_filter(filtered_list, index, '0')

        index += 1
        bit_0_count = 0
        bit_1_count = 0

    return filtered_list


oxygen = (get_oxygen_rating(parsed_data))
co2 = (get_co2_rating(parsed_data))

oxygen_array = list(oxygen[0])
co2_array = list(co2[0])

bin_oxygen = binary_to_decimal(oxygen_array)
bin_co2 = binary_to_decimal(co2_array)

print(bin_oxygen*bin_co2)




