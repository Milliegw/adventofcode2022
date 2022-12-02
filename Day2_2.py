score_player_1 = 0
score_player_2 = 0
count = 0
j_item = ""

with open('input2.txt', 'r') as file:
    lines = file.read().split('\n')
    file = [line.split() for line in lines]
    print(file)
    print(len(file))

for i, j in file:
    # X: loose
    # Y: draw
    # Z: win

    if j == 'X':
        score_player_1 += 6
        score_player_2 += 0
        if i == 'A':
            score_player_1 += 1
            j_item = "Scissor"
            score_player_2 += 3

        if i == 'B':
            score_player_1 += 2
            j_item = "Rock"
            score_player_2 += 1

        if i == 'C':
            score_player_1 += 3
            j_item = "Paper"
            score_player_2 += 2

    if j == 'Y':
        score_player_1 += 3
        score_player_2 += 3
        if i == 'A':
            score_player_1 += 1
            j_item = "Rock"
            score_player_2 += 1

        if i == 'B':
            score_player_1 += 2
            j_item = "Paper"
            score_player_2 += 2

        if i == 'C':
            score_player_1 += 3
            j_item = "Scissor"
            score_player_2 += 3

    if j == 'Z':
        score_player_1 += 0
        score_player_2 += 6
        if i == 'A':
            score_player_1 += 1
            j_item = "Paper"
            score_player_2 += 2

        if i == 'B':
            score_player_1 += 2
            j_item = "Scissor"
            score_player_2 += 3

        if i == 'C':
            score_player_1 += 3
            j_item = "Rock"
            score_player_2 += 1

print(f'Score player 1: {score_player_1}')
print(f'Score player 2: {score_player_2}')
