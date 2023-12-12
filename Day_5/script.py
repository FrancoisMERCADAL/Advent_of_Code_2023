FILE_NAME = "almanac.txt"

class Node:
    def __init__(self, mapping_list):
        self.mapping = mapping_list

    def give_mapping(self, value):
        for array in self.mapping:
            destination_range_start = array[0]
            source_range_start = array[1]
            range_len = array[2]
            if value >= source_range_start and value <= source_range_start + range_len - 1:
                return value + destination_range_start - source_range_start
        return value

def file_to_mapping(file):
    array = list()
    line = file.readline().strip()
    while line != "":
        array.append(list(map(int, line.split(" "))))
        line = file.readline().strip()
    return Node(array)

# PART 1
def get_min_location(file):
    for line in file:
        line = line.strip()
        if line == "seed-to-soil map:":
            seeds_mapping = file_to_mapping(file)
        elif line == "soil-to-fertilizer map:":
            soil_mapping = file_to_mapping(file)
        elif line == "fertilizer-to-water map:":
            fertilizer_mapping = file_to_mapping(file)
        elif line == "water-to-light map:":
            water_mapping = file_to_mapping(file)
        elif line == "light-to-temperature map:":
            light_mapping = file_to_mapping(file)
        elif line == "temperature-to-humidity map:":
            temperature_mapping = file_to_mapping(file)
        elif line == "humidity-to-location map:":
            humidity_mapping = file_to_mapping(file)
        elif line == "":
            pass
        else:
            seeds = list(map(int, line.split(': ')[1].split(' ')))

    locations = list()
    for seed in seeds:
        value = seeds_mapping.give_mapping(seed)
        value = soil_mapping.give_mapping(value)
        value = fertilizer_mapping.give_mapping(value)
        value = water_mapping.give_mapping(value)
        value = light_mapping.give_mapping(value)
        value = temperature_mapping.give_mapping(value)
        value = humidity_mapping.give_mapping(value)
        locations.append(value)
    return min(locations)

def If_you_give_a_seed_a_fertilizer_part1():
    file = open(FILE_NAME, "r")
    min_location = get_min_location(file)
    file.close()
    return min_location

# PART 2

### TEST AREA
# Part 1
#print(If_you_give_a_seed_a_fertilizer_part1())
# Output: 389056265

# Part 2
#print(If_you_give_a_seed_a_fertilizer_part2())
# Output: 
