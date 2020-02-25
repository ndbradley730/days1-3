class Claim:
    def __init__(self, claim_id, x, y, width, height):
        self.claim_id = claim_id
        self.x = x
        self.y = y
        self.width = width
        self.height = height

def parse_claim(claim):
    parts = claim.split(' ')

    claim_id = parts[0][1:]

    x_y_parts = parts[2].split(',')
    x = int(x_y_parts[0])
    y = int(x_y_parts[1][:-1])

    width_height_parts = parts[3].split('x')
    width = int(width_height_parts[0])
    height = int(width_height_parts[1])

    return Claim(claim_id, x, y, width, height)

def get_claims():
    with open('day3-input.txt', 'r') as f:
        for claim in f:
            yield parse_claim(claim)

def get_fabric_with_claims():
    fabric = []
    for claim in get_claims():
        # Adjust fabric size
        if len(fabric) < claim.x + claim.width:
            for _ in range(claim.x + claim.width - len(fabric)):
                fabric.append([])

        # At each x point, adjust fabric size
        for ix in range(claim.x, claim.x + claim.width):
            if len(fabric[ix]) < claim.y + claim.height:
                for _ in range(claim.y + claim.height - len(fabric[ix])):
                    fabric[ix].append(0)

        # Add in claims
        for ix in range(claim.x, claim.x + claim.width):
            for iy in range(claim.y, claim.y + claim.height):
                fabric[ix][iy] += 1

    return fabric

def part1():
    fabric = get_fabric_with_claims()
    overlapping = 0
    for ix in range(len(fabric)):
        for iy in range(len(fabric[ix])):
            if fabric[ix][iy] > 1:
                overlapping += 1
    return overlapping

def part2():
    fabric = get_fabric_with_claims()
    for claim in get_claims():
        found_overlap = False

        for ix in range(claim.x, claim.x + claim.width):
            if found_overlap:
                break
            for iy in range(claim.y, claim.y + claim.height):
                if fabric[ix][iy] > 1:
                    found_overlap = True
                    break

        if not found_overlap:
            return claim.claim_id
