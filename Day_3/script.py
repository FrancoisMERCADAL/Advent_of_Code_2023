FILE_NAME = "engine.txt"

# PART 1
def check_around(array, i, k):
    try:
        if array[i][k-1] != "." and array[i][k-1].isnumeric() == False:
            return True
    except:
        pass

    try:
        if array[i][k+1] != "." and array[i][k+1].isnumeric() == False:
            return True
    except:
        pass

    try:
        if array[i-1][k-1] != "." and array[i-1][k-1].isnumeric() == False:
            return True
    except:
        pass

    try:
        if array[i-1][k] != "." and array[i-1][k].isnumeric() == False:
            return True
    except:
        pass

    try:
        if array[i-1][k+1] != "." and array[i-1][k+1].isnumeric() == False:
            return True
    except:
        pass

    try:
        if array[i+1][k-1] != "." and array[i+1][k-1].isnumeric() == False:
            return True
    except:
        pass

    try:
        if array[i+1][k] != "." and array[i+1][k].isnumeric() == False:
            return True
    except:
        pass

    try:
        if array[i+1][k+1] != "." and array[i+1][k+1].isnumeric() == False:
            return True
    except:
        pass
    return False

def sum_part_numbers(file):
    array = []
    for line in file:
        array.append(line.rstrip())

    sum_nb_near_symbol = 0
    for i in range(len(array)):
        k = 0
        while k < len(array[i]):
            new_nb = []
            is_near_symbol = False
            while array[i][k].isnumeric():
                new_nb.append(array[i][k])
                if is_near_symbol == False:
                    is_near_symbol = check_around(array, i, k)
                k += 1
                if k >= len(array[i]):
                    break
            if is_near_symbol == True:
                sum_nb_near_symbol += int("".join(new_nb))
            k += 1
    return sum_nb_near_symbol

def gear_ratios_part1():
    file = open(FILE_NAME, "r")
    sum_parts = sum_part_numbers(file)
    file.close()
    return sum_parts

# PART 2
def check_two_nb_around(array, i, k):
    upper_line_nb = []
    nb_on_left = []
    nb_on_right = []
    down_line_nb = []

    # nb on upper line
    try:
        if array[i-1][k-1].isnumeric():
            upper_line_nb.append(array[i-1][k-1])
            index = k-2
            while index >= 0:
                if array[i-1][index].isnumeric():
                    upper_line_nb.insert(0, array[i-1][index])
                else:
                    break
                index -= 1
    except:
        pass
    
    try:
        if array[i-1][k].isnumeric():
            upper_line_nb.append(array[i-1][k])
        else:
            upper_line_nb.append(".")
    except:
        pass
    
    try:
        if array[i-1][k+1].isnumeric():
            upper_line_nb.append(array[i-1][k+1])
            index = k+2
            while index < len(array[i-1]):
                if array[i-1][index].isnumeric():
                    upper_line_nb.append(array[i-1][index])
                else:
                    break
                index += 1
    except:
        pass

    # nb on right
    try:
        if array[i][k-1].isnumeric():
            nb_on_right.append(array[i][k-1])
            index = k-2
            while index >= 0:
                if array[i][index].isnumeric():
                    nb_on_right.insert(0, array[i][index])
                else:
                    break
                index -= 1
    except:
        pass

    # nb on left
    try:
        if array[i][k+1].isnumeric():
            nb_on_left.append(array[i][k+1])
            index = k+2
            while index < len(array[i]):
                if array[i][index].isnumeric():
                    nb_on_left.append(array[i][index])
                else:
                    break
                index += 1
    except:
        pass

    # nb on under line
    try:
        if array[i+1][k-1].isnumeric():
            down_line_nb.append(array[i+1][k-1])
            index = k-2
            while index >= 0:
                if array[i+1][index].isnumeric():
                    down_line_nb.insert(0, array[i+1][index])
                else:
                    break
                index -= 1
    except:
        pass

    try:
        if array[i+1][k].isnumeric():
            down_line_nb.append(array[i+1][k])
        else:
            down_line_nb.append(".")
    except:
        pass

    try:
        if array[i+1][k+1].isnumeric():
            down_line_nb.append(array[i+1][k+1])
            index = k+2
            while index < len(array[i+1]):
                if array[i+1][index].isnumeric():
                    down_line_nb.append(array[i+1][index])
                else:
                    break
                index += 1
    except:
        pass

    if upper_line_nb[-1] == ".":
        upper_line_nb = upper_line_nb[:-1]
    elif upper_line_nb[0] == ".":
        upper_line_nb = upper_line_nb[1:]
    elif "." in upper_line_nb:
        upper_line_nb = [upper_line_nb[:upper_line_nb.index(".")], upper_line_nb[upper_line_nb.index(".")+1:]]

    if down_line_nb[-1] == ".":
        down_line_nb = down_line_nb[:-1]
    elif down_line_nb[0] == ".":
        down_line_nb = down_line_nb[1:]
    elif "." in down_line_nb:
        down_line_nb = [down_line_nb[:down_line_nb.index(".")], down_line_nb[down_line_nb.index(".")+1:]]

    return [upper_line_nb, nb_on_left, nb_on_right, down_line_nb]

def unwrap_tabs(list_tabs):
    array = []
    for tab in list_tabs:
        if tab == [] or type(tab[0]) == str:
            array.append(tab)
        elif type(tab[0]) == list:
            for i in range(len(tab)):
                array.append(tab[i])
    return array

def unwrap_numbers_from_tab(list_nb):
    for i in range(len(list_nb)):
        list_nb[i] = int("".join(list_nb[i]))
    return list_nb

def calculate_sum_gear_ratios(file):
    gears_locations = []
    array = []
    nb_line = 0
    sum_gear_ratios = 0

    for line in file:
        array.append(line.rstrip())
        for col in range(len(line)):
            if line[col] == "*":
                gears_locations.append((nb_line, col))
        nb_line += 1

    for gear in gears_locations:
        list_nb = unwrap_tabs(check_two_nb_around(array, gear[0], gear[1]))
        list_nb = [tab for tab in list_nb if len(tab) > 0]
        if len(list_nb) == 2:
            list_nb = unwrap_numbers_from_tab(list_nb)
            sum_gear_ratios += list_nb[0] * list_nb[1]
    return sum_gear_ratios

def gear_ratios_part2():
    file = open(FILE_NAME, "r")
    gears_ratio = calculate_sum_gear_ratios(file)
    file.close()
    return gears_ratio

### TEST AREA
# Part 1
print(gear_ratios_part1())
# Output: 530849

# Part 2
print(gear_ratios_part2())
# Output: 84900879
