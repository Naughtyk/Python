data = []
with open("input.txt") as f:
    for line in f:
        data.append([int(x) for x in line.split()])
lendata = data[0][0]
data = [0] + data[1]

counter = 0

for i in range(1, int((lendata + 1)/2)):
    if 2 * i <= lendata and 2*i + 1 <= lendata:
        if data[2 * i] >= data[i] and data[2*i + 1] >= data[i]:
            counter += 1

output_f = open('output.txt', 'w')
if counter == int(lendata/2):
    output_f.write('YES')
else:
    output_f.write('NO')