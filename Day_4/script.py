FILE_NAME = "scratchcards.txt"

# PART 1
def calculate_score(nb_winning_numbers):
    return int(2 ** (nb_winning_numbers - 1))

def calculate_total_points(file):
    total_points = 0
    for line in file:
        line = line.rstrip().split(": ")[1].split(" | ")
        winning_numbers = list(filter(None, line[0].split(" ")))
        player_numbers = list(filter(None, line[1].split(" ")))
        nb_winning_numbers = 0
        for num in player_numbers:
            if num in winning_numbers:
                nb_winning_numbers += 1
        total_points += calculate_score(nb_winning_numbers)
    return total_points

def scratchcards_part1():
    file = open(FILE_NAME, "r")
    total_points = calculate_total_points(file)
    file.close()
    return total_points

# PART 2
def calculate_total_cards(file):
    cards = {}
    for line in file:
        card_nb = line.split(":")[0].replace(" ", "")[4:]
        line = line.rstrip().split(": ")[1].split(" | ")
        winning_numbers = list(filter(None, line[0].split(" ")))
        player_numbers = list(filter(None, line[1].split(" ")))
        nb_winning_numbers = 0
        for num in player_numbers:
                if num in winning_numbers:
                    nb_winning_numbers += 1
        cards[card_nb] = (winning_numbers, player_numbers, nb_winning_numbers)
    cards_to_scratch = [1] * len(cards)
    for i in range(len(cards_to_scratch)):
        nb = cards[str(i+1)][2]
        for k in range(nb):
            cards_to_scratch[i+1+k] += cards_to_scratch[i]
    return sum(cards_to_scratch)

def scratchcards_part2():
    file = open(FILE_NAME, "r")
    total_cards_played = calculate_total_cards(file)
    file.close()
    return total_cards_played

### TEST AREA
# Part 1
print(scratchcards_part1())
# Output: 21485

# Part 2
print(scratchcards_part2())
# Output: 11024379
