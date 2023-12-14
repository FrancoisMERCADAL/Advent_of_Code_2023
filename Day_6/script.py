FILE_NAME = "papersheet.txt"

# PART 1
def multiply_winning_races(file):
    times = [int(time) for time in file.readline().strip().split(":")[1].split(" ") if time != ""]
    distances = [int(distance) for distance in file.readline().strip().split(":")[1].split(" ") if distance != ""]
    
    result = 1
    for time, distance in zip(times, distances):
        sum_races_id = 0
        for i in range(1,time):
            d = i * (time - i)
            if d > distance:
                sum_races_id += 1
        result *= sum_races_id
    return result

def wait_for_it_part1():
    file = open(FILE_NAME, "r")
    result = multiply_winning_races(file)
    file.close()
    return result

# PART 2
def get_nb_winning_races(file):
    time = int("".join(file.readline().strip().split(":")[1].split(" ")))
    distance = int("".join(file.readline().strip().split(":")[1].split(" ")))
    sum_races_id = 0
    for i in range(1,time):
        d = i * (time - i)
        if d > distance:
            sum_races_id += 1
    return sum_races_id

def wait_for_it_part2():
    file = open(FILE_NAME, "r")
    result = get_nb_winning_races(file)
    file.close()
    return result
    
### TEST AREA
# Part 1
#print(wait_for_it_part1())
# Output: 1108800

# Part 2
#print(wait_for_it_part2())
# Output: 36919753
