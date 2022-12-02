from itertools import islice

amount = 0
total_calories = 0
my_list = []

with open ('input.txt', 'r') as file:
    lines = file.read().split('\n\n')
    file = [line.split() for line in lines]
    x = [[int(j) for j in i] for i in file]
    # print(x)

# print(type(x))

for l in x:
    total_calories = sum(l)
    my_list.append(total_calories)
    print(f'This is the total calories = {total_calories}')

print(my_list)
x = sorted(my_list)
print(x)

last_three = list(islice(reversed(x), 0, 3))
last_three.reverse()
print(sum(last_three))
