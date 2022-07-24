"""
ID: ryanada1
LANG: PYTHON3
TASK: milk2
"""


fin = open('milk2.in', 'r')
fout = open('milk2.out', 'w')

words = list(map(int, fin.read().split()))

n = int(words[0])
starts = [words[1]]
ends = [words[2]]
for i in range(3, len(words) - 1, 2):
    for j in range(len(starts)):
        if words[i] < starts[j]:
            starts.insert(j, words[i])
            ends.insert(j, words[i + 1])
            break
        elif j == len(starts) - 1:
            starts.append(words[i])
            ends.append(words[i + 1])

print(starts)
print(ends)

removes = []
removee = []
for i in range(len(starts)):
    for j in range(i + 1, len(starts)):
        if ends[i] >= starts[j]:
            print('removing', min(ends[i], ends[j]),starts[j])
            print('i,j', i,j)
            removee.append(min(ends[i], ends[j]))
            removes.append(starts[j])

print(removes)
print(removee)

for i in range(len(removes)):
    starts.remove(removes[i])
    ends.remove(removee[i])

print(starts)
print(ends)

maxidle = 0
maxcontinuous = 0


for i in range(len(starts)):
    if ends[i] - starts[i] > maxcontinuous:
        maxcontinuous = ends[i] - starts[i]
    if i + 1 < len(starts) and starts[i + 1] - ends[i] > maxidle:
        maxidle = starts[i + 1] - ends[i]

fout.write(str(maxcontinuous) + ' ' + str(maxidle) + '\n')

fout.close()

#912 184