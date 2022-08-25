from day_4_data import clean_the_fucking_data, selected_nums, raw_data
from pprint import pprint

# convert all data points to tuples, for flags



# Need checks for each row, all indexes.

def play_bingo(bingo_data, chosen_numbers):
    # gets each board container

    for number in chosen_numbers:
        for table in bingo_data:
            table_number = 1
            for row in table:
                for number_flag in row:
                    if number_flag[0] == number:
                        number_flag[1] = 1

            winner = check_for_winner(table)

            # If there is a winner, return the table that is winning
            if winner:
                # print('Winner!', number)
                return table, table_number, number
            table_number += 1

def last_winner_bingo(bingo_data, chosen_numbers):
    # gets each board container

    boards_that_won = []

    for number in chosen_numbers:
        print(number)
        for table in bingo_data:
            table_number = 1
            for row in table:
                for number_flag in row:
                    if number_flag[0] == number:
                        number_flag[1] = 1

            print('checking', number, table_number)
            winner = check_for_winner(table)

            # If there is a winner, return the table that is winning
            if winner:
                if table in boards_that_won:
                   pass
                else:
                    boards_that_won.append(table)
                if len(bingo_data) == len(boards_that_won):

                    return boards_that_won[-1], table_number, number

            table_number += 1

def check_for_winner(table):
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
            pprint(table)
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

    # Commented out because apparently Diagonals Don't matter.. Beacuse bingo.
    # # win by diagonal
    # if table[0][0][1] != 0 and \
    #         table[1][1][1] != 0 and \
    #         table[2][2][1] != 0 and \
    #         table[3][3][1] != 0 and \
    #         table[4][4][1] != 0:
    #     print('Win by Diagonal (starting at top left')
    #     return True
    #
    # # win by other diagonal
    # if table[0][4][1] != 0 and \
    #         table[1][3][1] != 0 and \
    #         table[2][2][1] != 0 and \
    #         table[3][1][1] != 0 and \
    #         table[4][0][1] != 0:
    #     print('Won by other Diagonal')
    #     return True

    # print('Nothing happened')
    return False


def calc_score(table, last_number):

    running_score= 0

    for row in table:
        for number in row:
            if number[1] == 0:
                running_score += number[0]

    return (running_score * last_number)


cleaned_data = clean_the_fucking_data(raw_data)
[winning_table, table_number, winning_number] = play_bingo(cleaned_data, selected_nums)
winning_score = calc_score(winning_table, winning_number)
#
# pprint(winning_table)
# print(f'Table Number: {table_number} wins with a score of {winning_score}')


[last_table, last_table_num, last_num] = last_winner_bingo(cleaned_data, selected_nums)
print('Last Table!', last_table, last_num)
last_score = calc_score(last_table, last_num)
#
print(f'The last winner was: {last_table_num} with a score of {last_score}')

