
results = []
opponent_rock_draw = 'A Y'
opponent_paper_draw = 'B Y'
opponent_scissors_draw = 'C Y'
opponent_rock_win = 'A Z'
opponent_paper_win = 'B Z'
opponent_scissors_win = 'C Z'
opponent_rock_lose = 'A X'
opponent_paper_lose = 'B X'
opponent_scissors_lose = 'C X'

with open("Inputs/day2_input.txt", "r") as f:
    for line in f:
        if line.strip() == opponent_rock_draw:
            results.append(4)
        elif line.strip() == opponent_paper_draw:
            results.append(5)
        elif line.strip() == opponent_scissors_draw:
            results.append(6)
        elif line.strip() == opponent_rock_win:
            results.append(8)
        elif line.strip() == opponent_paper_win:
            results.append(9)
        elif line.strip() == opponent_scissors_win:
            results.append(7)
        elif line.strip() == opponent_rock_lose:
            results.append(3)
        elif line.strip() == opponent_paper_lose:
            results.append(1)
        elif line.strip() == opponent_scissors_lose:
            results.append(2)

print(sum(results))