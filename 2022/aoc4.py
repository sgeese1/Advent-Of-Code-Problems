
full_contain = 0

def check_ranges(r1l, r1u, r2l, r2u):
    if r1l <= r2u and r1u >= r2l:
        return True
    elif r2l <= r1u and r2u >= r1l:
        return True
    else:
        return False

def get_ranges(ranges):
    range_list = ranges.split(",")
    range1 = range_list[0].split("-")
    range2 = range_list[1].split("-")
    r1l = range1[0]
    r1u = range1[1]
    r2l = range2[0]
    r2u = range2[1]
    return check_ranges(int(r1l), int(r1u), int(r2l), int(r2u))

with open("Inputs/day4_input.txt", "r") as f:
    for line in f:
        if get_ranges(line.strip()) is True:
            full_contain += 1
        else:
            pass
    
print(full_contain)