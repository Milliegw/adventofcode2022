from string import ascii_letters

# Getting data
with open('input3.txt') as file:
    data = [i for i in file.read().strip().split("\n")]
    print(data)


# ==== PART 1 ====

# # Iterate through out dataset
totalSum = 0
for entry in data:
    # Get the half way mark
    half = len(entry)//2
    print(half)

    # Split up the string
    # remove repetition using set
    leftSide = set(entry[:half])
    rightSide = set(entry[half:])

    # print(leftSide, rightSide)
    for value, character in enumerate(ascii_letters):
        if character in leftSide and character in rightSide:
            totalSum += value + 1
            print(totalSum)

print("Answer to part 1: ", totalSum)

