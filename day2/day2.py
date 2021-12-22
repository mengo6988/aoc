f = open("input2.txt", "r")
li = []
d1 = {'forward': [], 'up': [], 'down': []}
horizontal = 0
depth = 0
aim = 0


def get_data():
    f = open("input2.txt", "r")
    data = [i.split() for i in f.read().splitlines()]
    return data


data = get_data()


for i, d in enumerate(data):
    h = d[0]
    v = d[1]
    if h == "forward":
        horizontal += int(v)
        temp = aim * int(v)
        depth += temp
    if h == "down":
        # depth += int(v)
        aim += int(v)
    if h == "up":
        # depth -= int(v)
        aim -= int(v)

print(horizontal * depth)
