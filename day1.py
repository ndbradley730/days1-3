def load_parse_frequency_list():
    changes = []
    with open('day1-input.txt', 'r') as f:
        for line in f:
            change = int(line[1:])
            if line.startswith('+'):
                changes.append(change)
            else:
                changes.append(-change)
    return changes

def part1():
    frequency = 0
    frequency_changes = load_parse_frequency_list()
    for change in frequency_changes:
        frequency += change
    return frequency

def part2():
    frequency = 0
    frequencies_found = {}
    frequency_changes = load_parse_frequency_list()
    i = 0
    while True:
        frequency += frequency_changes[i]
        if frequency in frequencies_found:
            return frequency
        else:
            frequencies_found[frequency] = True
        i += 1
        if i == len(frequency_changes):
            # Start over at 1st frequency change
            i = 0
