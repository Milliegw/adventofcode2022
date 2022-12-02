
count = 1
values = []
newlist = []
amount = 0
total_calories = 0

with open ('input.txt', 'r') as file:
    lines = file.read().split('\n\n')
    file = [line.split() for line in lines]
    x = [[int(j) for j in i] for i in file]
    # print(x)

# print(type(x))

for l in x:
    total_calories = sum(l)
    print(f'{l} = {total_calories}')

for l in x:
    total_calories = sum(l)
    if total_calories > amount:
        amount = total_calories
        total_calories = 0

print(amount)
