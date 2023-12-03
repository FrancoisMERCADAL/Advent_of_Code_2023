FILE_NAME = "games.txt"
CUBES = {
    "blue": 14,
    "green": 13,
    "red": 12
}

# PART 1
def get_sum_possible_games_ids(file):
    possible_games = []
    bool_game_possible = True
    for line in file:
        game_id = int(line.split(":")[0].split("Game ")[1])
        cube_sets = line.rstrip().split(": ")[1].split("; ")
        for cubes in cube_sets:
            cubes = cubes.split(', ')
            for cube in cubes:
                num = int(cube.split(' ')[0])
                color = cube.split(' ')[1]
                if num > CUBES[color]:
                    bool_game_possible = False
                    break
        if bool_game_possible:
            possible_games.append(game_id)
        bool_game_possible = True
    return sum(possible_games)

def cube_conundrum_part1():
    file = open(FILE_NAME, "r")
    sum_possible_games = get_sum_possible_games_ids(file)
    file.close()
    return sum_possible_games

# PART 2
def power_set_cubes(game_set):
    power = 1
    for key in game_set.keys():
        power *= max(game_set[key])
    return power

def get_sum_power_cubes(file):
    sum_power_cubes = 0
    for line in file:
        cube_sets = line.rstrip().split(": ")[1].split("; ")
        game_set = {
            "blue": [],
            "green": [],
            "red": []
        }
        for cubes in cube_sets:
            cubes = cubes.split(', ')
            for cube in cubes:
                num = int(cube.split(' ')[0])
                color = cube.split(' ')[1]
                game_set[color].append(num)
        sum_power_cubes += power_set_cubes(game_set)
    return sum_power_cubes

def cube_conundrum_part2():
    file = open(FILE_NAME, "r")
    sum_power_cubes = get_sum_power_cubes(file)
    file.close()
    return sum_power_cubes

### TEST AREA
# Part 1
print(cube_conundrum_part1())
# Output: 2771

# Part 2
print((cube_conundrum_part2()))
# Output: 
