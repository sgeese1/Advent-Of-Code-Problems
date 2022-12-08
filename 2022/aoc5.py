
stack1 = ["F", "D", "B", "Z", "T", "J", "R", "N"]
stack2 = ["R", "S", "N", "J", "H"]
stack3 = ["C", "R", "N", "J", "G", "Z", "F", "Q"]
stack4 = ["F", "V", "N", "G", "R", "T", "Q"]
stack5 = ["L", "T", "Q", "F",]
stack6 = ["Q", "C", "W", "Z", "B", "R", "G", "N"]
stack7 = ["F", "C", "L", "S", "N", "H", "M"]
stack8 = ["D", "N", "Q", "M", "T", "J"]
stack9 = ["P", "G", "S"]

super_stack = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

final_stack = []

#Part 1
def issue_commands(move, start_stack, end_stack):
    if move > len(start_stack):
        move = move - (move-len(start_stack))
    while move > 0:
        temp = start_stack.pop()
        end_stack.append(temp)
        move -= 1

#Part 2
def issue_commands_p2(move, start_stack, end_stack):
        temp = []
        while move > 0:
            temp.append(start_stack.pop())
            move -= 1
        # print(temp)
        temp.reverse()
        end_stack.extend(temp)

with open("Inputs/day5_input.txt", "r") as f:
    for line in f:
        input = line.split(",")
        move = int(input[0].strip())
        start_stack = super_stack[int(input[1].strip())-1]
        end_stack = super_stack[int(input[2].strip())-1]
        # print("move " + str(move) + " from " + str(input[1].strip())  + " to " + str(input[2].strip()))
        issue_commands_p2(move, start_stack, end_stack)

final_stack.append(stack1.pop())
final_stack.append(stack2.pop())
final_stack.append(stack3.pop())
final_stack.append(stack4.pop())
final_stack.append(stack5.pop())
final_stack.append(stack6.pop())
final_stack.append(stack7.pop())
final_stack.append(stack8.pop())
final_stack.append(stack9.pop())

print(final_stack)




