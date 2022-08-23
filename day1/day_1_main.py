from day_1_data import data_list

test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


# Problem 1 solution
def depth(depth_data):
    index = 0
    number_of_increases = 0

    try:
        for data_point in depth_data:

            did_increase = ((depth_data[index+1]) - data_point)
            index += 1
            if did_increase > 0:
                number_of_increases += 1
    except IndexError:
        pass

    return number_of_increases


# Problem 2
def consecutive_depth(depth_data):
    index = 0
    number_of_increases = 0

    try:
        for data_point in depth_data:

            consecutive_data1 = depth_data[index] + depth_data[index+1] + depth_data[index+2]
            consecutive_data2 = depth_data[index+1] + depth_data[index+2] + depth_data[index+3]
            did_increase = consecutive_data2 - consecutive_data1
            index += 1
            if did_increase > 0:
                number_of_increases += 1
    except IndexError:
        pass

    return number_of_increases


print(consecutive_depth(data_list))