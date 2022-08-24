from pprint import pprint

selected_nums = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]


raw_data = '''22 13 17 11 0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''


def clean_the_fucking_data(bingo_data):
    split_data = bingo_data.split('\n')

    final_data = []
    current_table = []
    current_row = []

    # while my current board is incomplete, continue the loop.

    for row in split_data:
        split_row = row.split(' ')
        for number in split_row:
            try:
                flagged_number = [int(number), 0]

                current_row.append(flagged_number)

            except ValueError:
                pass

        if len(current_row) == 5:

            current_table.append(current_row)
            current_row = []

        if len(current_table) == 5:
            final_data.append(current_table)
            current_table = []

    return final_data


cleaned_data = clean_the_fucking_data(raw_data)