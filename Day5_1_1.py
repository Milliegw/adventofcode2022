stacks = [["D","M","S","Z","R","F","W","N"], ["W","P","Q","G","S"],
          ["W","R","V","Q","F","N","J","C"], ["F","Z","P","C","G","D","L"], ["T","P","S"],
          ["H","D","F","W","R","L"], ["Z","N","D","C"], ["W","N","R","F","V","S","J","Q"],
          ["R","M","S","G","Z","W","V"]]

with open("input5.txt") as instructions:
    for line in instructions:
        moves = [int(x) for x in line.split() if x.isdigit()]
        print(moves)

        for i in range(moves[0]):
            print(i)
            moving = stacks[moves[0]].pop()
#             stacks[moves[2]-1].append(moving)
#
#     topCrates = ""
#     for stack in stacks:
#         topCrates += str(stack.pop())
#
# print(topCrates)