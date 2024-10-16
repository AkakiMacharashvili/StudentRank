import numpy

def frobenius(arr):
    tt = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            tt += (arr[i][j]) * (arr[i][j])
    return numpy.sqrt(tt)

n = int(input('please enter number of students: '))
k = int(input('please enter number of groups: '))
print('please enter student scores: ')
lst = []
studentScores = []
students = dict()
for i in range(n):
    str = input()
    list = str.split(' ')
    temp = []
    for j in list:
        temp.append(float(j))

    point = temp[0] + temp[1] + temp[2]*1.5

    arr = numpy.array(temp)
    studentScores.append(temp)
    s = f'student_{i + 1}'
    students[f'student_{i + 1}'] = arr
    lst.append([point, s])

array = sorted(lst, key=lambda x: x[0])

groups = []

for i in range(n - 15, n):
    grp = [i % 15]
    for r in array[i]:
        grp.append(r)
    groups.append(grp)

t = int(n / 15)
for i in range(t - 1):
    temp = sorted(groups, key=lambda x: x[1])
    temp.reverse()
    cur = []
    for e in range(15*i, 15*(i + 1)):
        cur.append(array[e])
    for a in range(15):
        point = cur[a][0]
        stud = cur[a][1]
        avg = (temp[a][1] + point) / (i + 2)
        ind = temp[a][0]
        groups[ind][1] = avg
        groups[ind].append(stud)

groupsRank = []
for i in range(k):
    groupsRank.append([f'group_{i + 1}', groups[i][1]])

for i in range(k):
    print(f'--->group_{i + 1}')
    for j in range(2, int(n/k) + 2):
       print(groups[i][j])

print(groupsRank)

group_id = []
for i in range(k):
    group_id.append(0)


for i in range(k):
    lst = []
    for j in range(2, int(n/k) + 2):
       lst.append(students[groups[i][j]])
    arr = numpy.array(lst)
    group_id[i] = frobenius(arr)

for i in range(k):
    print(f'rank_of_group_{i}' + ' -> ' + f'{group_id[i]}')
