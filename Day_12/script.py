FILE_NAME = "condition_records.txt"

file = open(FILE_NAME, "r")
for line in file:
    line = line.strip().split(" ")
    springs = [char for char in line[0]]
    numerics = [int(char) for char in line[1].split(",")]
    print(springs,numerics)
file.close()
