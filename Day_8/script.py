from math import gcd

FILE_NAME = "camel_way.txt"

def open_parse_file(file):
    instructions = list(file.readline().strip())
    maps = {}
    file.readline()
    for line in file:
        line = line.strip().split(" = ")
        key = line[0]
        value = line[1][1:-1].split(", ")
        maps[key] = value
    return instructions, maps

# PART 1
def get_nb_steps_part1(file, start, end):
    instructions, maps = open_parse_file(file)

    nb_steps = 0
    instructions_index = 0

    while start != end:
        nb_steps += 1
        if instructions_index >= len(instructions):
            instructions_index = 0
        if instructions[instructions_index] == "L":
            start = maps[start][0]
        elif instructions[instructions_index] == "R":
            start = maps[start][1]
        instructions_index += 1
    return nb_steps

def haunted_wasteland_part1():
    file = open(FILE_NAME, "r")
    nb_steps = get_nb_steps_part1(file, "AAA", "ZZZ")
    file.close()
    return nb_steps

# PART 2
def calculate_lcm(array):
    lcm = 1
    for i in array:
        lcm = lcm*i//gcd(lcm, i)
    return lcm

def get_nb_steps_part2(file):
    instructions, maps = open_parse_file(file)

    start_keys = [x for x in maps.keys() if x[2] == 'A']
    first_time_hit_Z = [0] * len(start_keys)
    exit_loop = False
    index_instruction = 0
    nb_steps = 0

    while exit_loop == False:
        nb_steps += 1
        if instructions[index_instruction] == "L":
            index_to_follow = 0
        elif instructions[index_instruction] == "R":
            index_to_follow = 1
        for i in range(len(start_keys)):
            start_keys[i] = maps[start_keys[i]][index_to_follow]
            if start_keys[i][2] == 'Z' and first_time_hit_Z[i] == 0:
                first_time_hit_Z[i] = nb_steps

        if 0 not in first_time_hit_Z:
            exit_loop = True
        else:
            index_instruction += 1
            if index_instruction == len(instructions):
                index_instruction = 0
    return calculate_lcm(first_time_hit_Z)

def haunted_wasteland_part2():
    file = open(FILE_NAME, "r")
    nb_steps = get_nb_steps_part2(file)
    file.close()
    return nb_steps

### TEST AREA
# Part 1
#print(haunted_wasteland_part1())
# Output: 12169

# Part 2
#print(haunted_wasteland_part2())
# Output: 12030780859469
