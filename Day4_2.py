with open('input4.txt') as file:
    data = [i for i in file.read().strip().split("\n")]
    # print(data)
    # print(type(data))

count = 0
for entry in data:
    # print(entry)
    # print(type(entry))
    x = entry.split(",")
    print(x)
    a = x[0].replace("-", ",").split(",")
    b = x[1].replace("-", ",").split(",")
    # print(int(a[0]))
    # print(int(a[1]))
    #
    elf1 = set(range(int(a[0]), int(a[1])+1))
    elf2 = set(range(int(b[0]), int(b[1])+1))

    print(elf1)
    print(elf2)


    if elf1.intersection(elf2):
        count += 1

print(count)

