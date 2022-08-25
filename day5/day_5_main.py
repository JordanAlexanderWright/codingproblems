from pprint import pprint

def make_board(x_dimension, y_dimension):
    x = 0
    y = 0

    matrix = []
    row = []

    while y <= y_dimension:

        while x <= x_dimension:
            coordinate = [[x, y], 0]
            row.append(coordinate)
            x += 1

        matrix.append(row)
        row = []
        y += 1
        x = 0
    return matrix


for row in (make_board(9, 9)):
    print(row)


def check_vents(matrix, coordinates):
    # for each coordinate, if coord[0][0] and coord [1][0] are the same, x axis

    for coord in coordinates:
        if coord[0][0][0] == coord[0][1][0]:
            y_start = coord[0][0][1]
            y_end = coord[0][1][1]

            x_coordinate = coord[0][0][0]

            while y_start <= y_end:
                matrix[y_start][x_coordinate][1] += 1
                y_start += 1

            # The Y axis is changing
        if coord[0][0][1] == coord[0][1][1]:

            if coord[0][0][0] == coord[0][1][0]:
                x_start = coord[0][0][0]
                x_end = coord[0][1][0]

                y_coordinate = coord[0][0][1]

                while x_start <= x_end:
                    matrix[y_coordinate][x_start][1] += 1
                    x_start += 1

            # The X axis is changing
        else:
            pass
    return matrix
