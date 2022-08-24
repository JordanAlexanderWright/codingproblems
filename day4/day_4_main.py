from day_4_data import data, selected_nums

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
    winner = False

    while not winner:

        for number in chosen_numbers:
            print(number)
            print(bingo_data)
            row = 0
            index = 0
            if bingo_data[row][index][1] != 0 &\
                    bingo_data[row + 1][index][1] != 0 & \
                    bingo_data[row + 2][index][1] != 0 & \
                    bingo_data[row + 3][index][1] != 0 & \
                    bingo_data[row + 4][index][1] != 0:
                winner = True
                print('won by column')
                break

            # win by row
            if bingo_data[row][index][1] != 0 &\
                    bingo_data[row][index + 1][1] != 0 & \
                    bingo_data[row][index + 2][1] != 0 & \
                    bingo_data[row][index + 3][1] != 0 & \
                    bingo_data[row][index + 4][1] != 0 :
                winner = True
                print('won by row')
                break

            # win by diagonal
            if bingo_data[row][index][1] != 0 &\
                    bingo_data[row + 1][index + 1][1] != 0 & \
                    bingo_data[row + 2][index + 2][1] != 0 & \
                    bingo_data[row + 3][index + 3][1] != 0 & \
                    bingo_data[row + 4][index + 4][1] != 0:
                print('Win by Column (starting at top left')
                break

            # win by other diagonal
            if bingo_data[row + 4][index + 4][1] != 0 &\
                    bingo_data[row + 3][index + 3][1] != 0 & \
                    bingo_data[row + 2][index + 2][1] != 0 & \
                    bingo_data[row + 1][index + 1][1] != 0 & \
                    bingo_data[row][index][1] != 0:
                print('Win by Column (starting at top right')
                break

            for row in bingo_data:
                for number_flag in row:
                    if number_flag[0] == number:
                        number_flag[1] = 1
        # win by column
        print(bingo_data[row][index][1])


bingo_board = prep_data(data)

print(bingo_board)

print(bingo_board[0][1][0])
play_bingo(bingo_board, selected_nums)
