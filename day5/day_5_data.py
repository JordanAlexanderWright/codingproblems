coordinates = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''

def clean_data(coordinate_data):
    split_data = coordinate_data.split('\n')
    line_data = []

    for coord in split_data:
        # print(coord.split('->'))
        split_string = coord.split('->')
        print(split_string)
        cleaned_coord = []

        for item in split_string:
            cleaned_coord.append(item.strip())

        line_data.append(cleaned_coord)

    print(line_data)
clean_data(coordinates)

