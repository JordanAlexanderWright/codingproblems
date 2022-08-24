from day_4_data import data, selected_nums
from pprint import pprint

# convert all data points to tuples, for flags


def prep_data(unclean_data):

    cleaned_data = []

    for bingo_row in unclean_data:
        new_list = []
        for number in bingo_row:
            flagged_number = [number, 0]
            new_list.append(flagged_number)

        cleaned_data.append(new_list)

    return cleaned_data


# Need checks for each row, all indexes.

def play_bingo(bingo_data, chosen_numbers):
    # gets each board container

    for number in chosen_numbers:
        for row in bingo_data:
            for number_flag in row:
                if number_flag[0] == number:
                    number_flag[1] = 1

        winner = check_for_winner(bingo_data)
        if winner:
            break

    print('Winner!')
    pprint(bingo_data)


def check_for_winner(table):
    print('checking')
    row = 0
    index = 0

    # Win by column
    while True:

        if table[0][index][1] != 0 and \
                table[1][index][1] != 0 and \
                table[2][index][1] != 0 and \
                table[3][index][1] != 0 and \
                table[4][index][1] != 0:
            print('won by column')
            return True
        index += 1
        if index == 5:
            index = 0
            break

    while True:

        if table[row][0][1] != 0 and \
                table[row][1][1] != 0 and \
                table[row][2][1] != 0 and \
                table[row][3][1] != 0 and \
                table[row][4][1] != 0:

            print('won by row')
            print(table[row])
            return True
        row += 1
        if row == 5:
            row = 0
            break

    # win by diagonal
    if table[0][0][1] != 0 and \
            table[1][1][1] != 0 and \
            table[2][2][1] != 0 and \
            table[3][3][1] != 0 and \
            table[4][4][1] != 0:
        print('Win by Diagonal (starting at top left')
        return True

    # win by other diagonal
    if table[0][4][1] != 0 and \
            table[1][3][1] != 0 and \
            table[2][2][1] != 0 and \
            table[3][1][1] != 0 and \
            table[4][0][1] != 0:
        print('Won by other Diagonal')
        return True

    print('Nothing happened')
    return False


bingo_board = prep_data(data)

pprint(bingo_board)

print(bingo_board[0][1][0])
play_bingo(bingo_board, selected_nums)

#
# test_data = [
#  [[22, 0], [13, 1], [17, 1], [11, 1], [0, 1]],
#  [[8, 0], [2, 1], [23, 0], [4, 1], [24, 0]],
#  [[21, 1], [9, 1], [14, 1], [16, 1], [7, 0]],
#  [[6, 0], [10, 1], [3,0], [18, 1], [5, 0]],
#  [[1, 1], [12, 0], [20, 0], [15, 0], [19, 1]]
#  ]
#
# check_for_winner(test_data)

