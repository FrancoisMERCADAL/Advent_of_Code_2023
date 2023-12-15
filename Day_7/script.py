FILE_NAME = "card_hands.txt"

# PART 1
CARDS_STRENGTH_PART1 = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]

def _4same_or_fullhouse(hand):
    count_dict = {}
    for i in hand:
        if i not in count_dict.keys():
            count_dict[i] = 1
        else:
            count_dict[i] += 1
            if count_dict[i] == 4:
                return "4_same"
    return "full_house"

def _3same_or_2pairs(hand):
    count_dict = {}
    for i in hand:
        if i not in count_dict.keys():
            count_dict[i] = 1
        else:
            count_dict[i] += 1
            if count_dict[i] == 3:
                return "3_same"
    return "2_pairs"

def custom_sort(arr):
    return sorted(arr, key=lambda x: [CARDS_STRENGTH_PART1.index(c) if c in CARDS_STRENGTH_PART1 else len(CARDS_STRENGTH_PART1) for c in x[0]])

def calculate_sum_bids(file):
    results = {
        "all_different":[],
        "1_pair":[],
        "2_pairs":[],
        "3_same":[],
        "full_house":[],
        "4_same":[],
        "5_same":[]
    }

    for line in file:
        line = line.strip().split(" ")
        hand = line[0]
        bid = int(line[1])
        if len(set(hand)) == 1:
            results["5_same"].append((hand,bid))
        elif len(set(hand)) == 2: # "4_same" or "full_house"
            key = _4same_or_fullhouse(hand)
            results[key].append((hand,bid))
        elif len(set(hand)) == 3: # "3_same" or "2_pairs"
            key = _3same_or_2pairs(hand)
            results[key].append((hand,bid))
        elif len(set(hand)) == 4:
            results["1_pair"].append((hand,bid))
        else:
            results["all_different"].append((hand,bid))

    rank = 0
    sum_bid = 0
    for key in results.keys():
        results[key] = custom_sort(results[key])
        rank += len(results[key])
        for i in range(len(results[key])):
            sum_bid += results[key][i][1] * (rank - i)
    return sum_bid

def camel_cards_part1():
    file = open(FILE_NAME, "r")
    sum_bids = calculate_sum_bids(file)
    file.close()
    return sum_bids

# PART 2

### TEST AREA
# Part 1
#print(camel_cards_part1())
# Output: 251927063

# Part 2
#print(camel_cards_part2())
# Output:
