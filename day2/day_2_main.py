from day_2_data import parsed_data


# Problem 1
def motion_tracker(data):
    horizontal = 0
    vertical = 0
    for data_point in data:
        direction = data_point[0]
        movement_value = data_point[1]

        match direction:
            case 'forward':
                horizontal += movement_value
            case 'down':
                vertical += movement_value
            case 'up':
                vertical -= movement_value

    return horizontal, vertical


[horizontal, vertical] = motion_tracker(parsed_data)

print(horizontal, vertical)
print(horizontal * vertical)


#Problem 2
def motion_tracker_aim(data):
    horizontal = 0
    depth = 0
    aim = 0
    for data_point in data:
        direction = data_point[0]
        movement_value = data_point[1]

        match direction:
            case 'forward':
                horizontal += movement_value
                depth += (aim * movement_value)
            case 'down':
                aim += movement_value

            case 'up':
                aim -= movement_value

    return horizontal, depth


[horizontal, depth] = motion_tracker_aim(parsed_data)

print(horizontal, depth)
print(horizontal*depth)