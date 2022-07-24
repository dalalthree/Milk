"""
ID: ryanada1
LANG: PYTHON3
TASK: milk2
"""


fin = open('milk2.in', 'r')
fout = open('milk2.out', 'w')

words = fin.read().split()

n = int(words[0])
start = list(map(int, words[1::2]))
end = list(map(int, words[2::2]))

maxidle = 0
maxcontinuous = 0
ranges = [] #add each one to a range
ranges.append((start[0], end[0]))

for i in range(1, n):
    print(i)
    for j in range(len(ranges)):
        if ranges[j][0] <= end[i] and ranges[j][1] >= end[i] or ranges[j][0] <= start[i] and ranges[j][1] >= start[i]:
            ranges[j] = (min(start[i], ranges[j][0]), max(ranges[j][1], end[i]))
            continue
        elif start[i] >= ranges[j][0] and end[i] <= ranges[j][1]:
            continue
        else:
            add = True
            for k in range(len(ranges)):
                if start[i] == ranges[k][0] and end[i] == ranges[k][1]:
                    add = False
            if add: ranges.append((start[i], end[i]))

finalranges = []
for i in range(len(ranges)):
    add = True
    for j in range(len(ranges)):
        if i != j and ranges[i][0] > ranges[j][0] and ranges[i][1] < ranges[j][1]:
            add = False
    if add: finalranges.append(ranges[i])


for i in range(len(finalranges)):
    if finalranges[i][1] - finalranges[i][0] > maxcontinuous:
        maxcontinuous = finalranges[i][1] - finalranges[i][0]
    if i + 1 < len(finalranges) and finalranges[i + 1][0] - finalranges[i][1] > maxidle:
        maxidle = finalranges[i + 1][0] - finalranges[i][1]

fout.write(str(maxcontinuous) + ' ' + str(maxidle) + '\n')

fout.close()

#912 184