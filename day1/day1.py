f = open("input.txt", "r")
count = 0
li = []
li2 = []
for x in f:
    li.append(int(x.replace('\n', '')))

for n in range(0, len(li)-2):
    li2.append(li[n] + li[n+1] + li[n+2])

for n in range(len(li2)):
    if li2[n] > li2[n-1]:
        count += 1

print(count)
