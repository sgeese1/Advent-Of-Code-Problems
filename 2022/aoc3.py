import string

values = dict()
priorities = []
top_list = []

def set_priority_values():
    for index, letter in enumerate(string.ascii_lowercase):
        values[letter] = index + 1
    for index, letters in enumerate(string.ascii_uppercase):
        values[letters] = index + 27

set_priority_values()

with open("Inputs/day3_input.txt", "r") as f:
    for line in f:
        top_list.append(line)
        # x = len(line)
        # string1 = slice(0, x//2)
        # string2 = slice(x//2, x)
        # match = set(line[string1]) & set(line[string2])
        # priorities.append(values[match.pop()])
        # for a in line[string1]:
        #     for b in line[string2]:
        #         if a == b:
        #             priorities.append(values[b])
        # if char == string.ascii_lowercase:
        #     for index, letter in enumerate(string.ascii_lowercase):
        #         priorities.append(index + 1)
        # elif char == string.ascii_uppercase:
        #     for index, letter in enumerate(string.ascii_uppercase)
        #     priorities.append(index + 27)

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

groups = list(chunks(top_list, 3))

for group in groups:
    string1 = group[0]
    string2 = group[1]
    string3 = group[2]
    common = set(string1.strip()) & set(string2.strip()) & set(string3.strip())
    priorities.append(values[common.pop()])

print(sum(priorities))