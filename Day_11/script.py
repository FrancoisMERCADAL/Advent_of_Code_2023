FILE_NAME = "galaxies.txt"
MULTIPLY_NB = 1000000

def find_empty_vertical_lines(space):
    empty_vertical_lines = []
    for i in range(len(space[0])):
        line = [space[index][i] for index in range(len(space))]
        if line == list("." * len(space)):
            empty_vertical_lines.append(i)
    return empty_vertical_lines

def find_galaxies(space):
    galaxies = []
    for line_index in range(len(space)):
        for column_index in range(len(space[line_index])):
            if space[line_index][column_index] == "#":
                galaxies.append((line_index,column_index))
    return galaxies

# PART 1
def add_vertical_empty_line(space,empty_vertical_lines):
    empty_vertical_lines = [index + empty_vertical_lines.index(index) for index in empty_vertical_lines]
    for i in range(len(space)):
        for index in empty_vertical_lines:
            space[i].insert(index,".")
    return space

def calculate_sum_paths(galaxies):
    sum = 0
    for i in range(len(galaxies)):
        for k in range(i+1,len(galaxies)):
            sum += abs(galaxies[i][0] - galaxies[k][0]) + abs(galaxies[i][1] - galaxies[k][1])
    return sum

def get_sum_shortest_paths_p1(file):
    space = []
    for line in file:
        line = line.strip()
        space.append([char for char in line])
        if line == "." * len(line):
            space.append([char for char in line])
    empty_vertical_lines = find_empty_vertical_lines(space)
    space = add_vertical_empty_line(space,empty_vertical_lines)
    galaxies = find_galaxies(space)
    return calculate_sum_paths(galaxies)

def cosmic_expansion_part1():
    file = open(FILE_NAME, "r")
    sum_paths = get_sum_shortest_paths_p1(file)
    file.close()
    return sum_paths

# PART 2
def get_sum_shortest_paths_p2(file):
    space = []
    index_line = 0
    empty_lines = []

    for line in file:
        line = line.strip()
        space.append([char for char in line])
        if line == "." * len(line):
            empty_lines.append(index_line)
        index_line += 1

    empty_columns = find_empty_vertical_lines(space)
    galaxies = find_galaxies(space)

    sum = 0
    for i in range(len(galaxies)):
        for k in range(i+1,len(galaxies)):
            visited_lines = [j for j in range(min(galaxies[i][0],galaxies[k][0]),max(galaxies[i][0],galaxies[k][0]+1))]
            visited_lines.remove(galaxies[i][0])
            visited_columns = [j for j in range(min(galaxies[i][1],galaxies[k][1]),max(galaxies[i][1],galaxies[k][1])+1)]
            visited_columns.remove(galaxies[i][1])

            for line_nb in visited_lines:
                if line_nb in empty_lines:
                    sum += MULTIPLY_NB
                else:
                    sum += 1
            for col_nb in visited_columns:
                if col_nb in empty_columns:
                    sum += MULTIPLY_NB
                else:
                    sum += 1
    return sum

def cosmic_expansion_part2():
    file = open(FILE_NAME, "r")
    sum_paths = get_sum_shortest_paths_p2(file)
    file.close()
    return sum_paths

### TEST AREA
# Part 1: Naive approach
print(cosmic_expansion_part1())
# Output: 9627977

# Part 2: Scientific approach
print(cosmic_expansion_part2())
# Output: 644248339497
