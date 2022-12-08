
totals_array = []
subtotal = 0
group = []
with open("Inputs/day1_input.txt", "r") as f:
    for line in f:
        if line != '\n':
            subtotal += int(line)
        else:
            totals_array.append(subtotal)
            subtotal = 0
            continue

totals_array.sort()
print(totals_array)