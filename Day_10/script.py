FILE_NAME = "pipes_maze.txt"

RIGHT_MOVE = (0,1)
LEFT_MOVE = (0,-1)
UP_MOVE = (-1,0)
DOWN_MOVE = (1,0)

DIRECTIONS_DICT = {
    "-":{
        "RIGHT": RIGHT_MOVE,
        "LEFT": LEFT_MOVE
    },
    "|":{
        "UP": UP_MOVE,
        "DOWN": DOWN_MOVE
    },
    "L":{
        "UP": UP_MOVE,
        "RIGHT": RIGHT_MOVE
    },
    "J":{
        "LEFT": LEFT_MOVE,
        "UP": UP_MOVE
    },
    "7":{
        "DOWN": DOWN_MOVE,
        "LEFT": LEFT_MOVE
    },
    "F":{
        "DOWN": DOWN_MOVE,
        "RIGHT": RIGHT_MOVE
    }
}

def parse_file(file):
    start_position = [0,0]
    line_number = 0
    lines_array = []
    for line in file:
        line = [x for x in line.strip()]
        if 'S' in line:
            start_position = [line_number, line.index('S')]
        lines_array.append(line)
        line_number += 1
    return lines_array, start_position

def get_new_position(lines_array, position, last_location):
    dict_position = DIRECTIONS_DICT[lines_array[position[0]][position[1]]]
    for way in dict_position.keys():
        if position[0] + dict_position[way][0] == last_location[0] and position[1] + dict_position[way][1] == last_location[1]:
            continue
        else:
            new_position = [position[0] + dict_position[way][0], position[1] + dict_position[way][1]]
    return new_position, position

def iterate_maze(file):
    lines_array, start_position = parse_file(file)

    returned_to_start = False
    lines_array[start_position[0]][start_position[1]] = "F"
    last_location = start_position
    current_position = start_position

    nb_steps = 0
    while returned_to_start == False:
        nb_steps += 1
        current_position, last_location = get_new_position(lines_array,current_position,last_location)
        if current_position == start_position:
            returned_to_start = True
    return int(nb_steps/2)

def pipe_maze_part1():
    file = open(FILE_NAME, "r")
    nb_steps = iterate_maze(file)
    file.close()
    return nb_steps

### TEST AREA
# Part 1
print(pipe_maze_part1())
# Output: 6931

# Part 2
#print(pipe_maze_part2())
# Output: 
