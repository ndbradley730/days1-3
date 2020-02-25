def count_characters(box_id):
    char_counts = {}
    for char in box_id:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    return char_counts

def part1():
    with open('day2-input.txt', 'r') as f:
        pairs, triplets = 0, 0
        for box_id in f:
            found_pair, found_triplet = False, False
            char_counts = count_characters(box_id)

            # Check the counts for 2s and 3s
            if any([count == 2 for count in char_counts.values()]):
                pairs += 1
            if any([count == 3 for count in char_counts.values()]):
                triplets += 1

        return pairs * triplets

def part2():
    with open('day2-input.txt', 'r') as f:
        id_permutations = {}
        for box_id in f:
            # For each char in box_id, replace with * and look for it in the hashtable
            for i, char in enumerate(box_id):
                wildcard_str = box_id[0:i] + '*' + box_id[i+1:-1]
                if wildcard_str in id_permutations:
                    # Found our answer
                    return wildcard_str.replace('*', '')
                else:
                    id_permutations[wildcard_str] = True
