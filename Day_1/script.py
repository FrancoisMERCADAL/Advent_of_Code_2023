FILE_NAME = "calibration_document.txt"
SPELLED_DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

# PART 1
def calculate_sum(file):
    cumulate_sum = 0
    for line in file:
        array = [x for x in list(line) if x.isnumeric()]
        if len(array) == 1:
            array = array * 2
        else:
            array = [array[0], array[-1]]
        cumulate_sum += int(''.join(array))
    return cumulate_sum

def trebuchet_part1():
    file = open(FILE_NAME, "r")
    cumulate = calculate_sum(file)
    file.close()
    return cumulate

# PART 2
def calculate_sum_with_litteral_digits(file):
    cumulate_sum = 0
    for line in file:
        buffer = ""
        array = []
        for char in line:
            if char.isdigit():
                array.append(char)
                buffer = ""
            else:
                if len(buffer) == 0 and char in ['o','t','f','s','e','n']:
                    buffer = buffer + char
                elif len(buffer) > 0:
                    buffer = buffer + char
                while len(buffer) > 5 and buffer not in SPELLED_DIGITS.keys():
                    buffer = buffer[1:]
                    for key in SPELLED_DIGITS.keys():
                        if key in buffer:
                            array.append(SPELLED_DIGITS[key])
                if buffer in SPELLED_DIGITS.keys():
                    array.append(SPELLED_DIGITS[buffer])
                    buffer = ""

        if len(array) == 1:
            array = array * 2
        else:
            array = [array[0], array[-1]]
        cumulate_sum += int(''.join(array))
    
    return cumulate_sum

def trebuchet_part2():
    file = open(FILE_NAME, "r")
    cumulate_sum = calculate_sum_with_litteral_digits(file)
    file.close()
    return cumulate_sum

### TEST AREA
# Part 1
print(trebuchet_part1())
# Output: 54597

# Part 2
print((trebuchet_part2()))
# Output: 54504
