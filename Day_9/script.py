FILE_NAME = "history.txt"

# PART 1
def calculate_mirage_sum_part1(file):
    sum = 0
    for line in file:
        line = [int(x) for x in line.strip().split(' ')]
        list_line = [line]
        while len(set(list_line[-1])) > 1:
            new_list = []
            for i in range(len(list_line[-1])-1):
                new_list.append(list_line[-1][i+1] - list_line[-1][i])
            list_line.append(new_list)
        while len(list_line) > 1:
            nb = list_line[-1][-1]
            list_line.pop()
            list_line[-1].append(nb + list_line[-1][-1])
        sum += list_line[0][-1]
    return sum

def mirage_maintenance_part1():
    file = open(FILE_NAME, "r")
    sum = calculate_mirage_sum_part1(file)
    file.close()
    return sum

# PART 2
def calculate_mirage_sum_part2(file):
    sum = 0
    for line in file:
        line = [int(x) for x in line.strip().split(' ')]
        list_line = [line]
        while len(set(list_line[-1])) > 1:
            new_list = []
            for i in range(len(list_line[-1])-1):
                new_list.append(list_line[-1][i+1] - list_line[-1][i])
            list_line.append(new_list)
        while len(list_line) > 1:
            nb = list_line[-1][0]
            list_line.pop()
            list_line[-1].insert(0, list_line[-1][0] - nb)
        sum += list_line[0][0]
    return sum

def mirage_maintenance_part2():
    file = open(FILE_NAME, "r")
    sum = calculate_mirage_sum_part2(file)
    file.close()
    return sum

### TEST AREA
# Part 1
#print(mirage_maintenance_part1())
# Output: 1806615041

# Part 2
#print(mirage_maintenance_part2())
# Output: 1211
