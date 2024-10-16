
import numpy

def mynorm(arr):
    tt = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            tt += arr[i][j]
    return float(tt / (len(arr[0]) * len(arr)))

def frobenius(arr):
    tt = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            tt += (arr[i][j]) * (arr[i][j])
    return numpy.sqrt(tt)

#number of students
n = int(input('please enter number of students: '))
print('please enter students: ')
list_of_students = []
list_of_avg = []
for i in range(n):
    #creating grade matrix
    grades = []
    #generating input
    for j in range(4):
        inp = input()
        lst = inp.split(' ')
        lst1 = []
        for a in lst:
            lst1.append(float(a))
        grades.append(lst1)
    arr = numpy.array(grades)
    list_of_students.append([frobenius(arr), f'student_{i + 1}'])
    list_of_avg.append([mynorm(list(arr)), f'student_{i + 1}'])

#student ranking
ranking = sorted(list_of_students, key=lambda x: x[0])
ranking1 = sorted(list_of_avg, key=lambda x: x[0])
#output
print('frobenius ranking: ')
for a in ranking:
    strg = str(a[0])
    strg += ' -> '
    strg += a[1]
    print(strg)

print('average ranking')
for a in ranking1:
    strg = str(a[0])
    strg += ' -> '
    strg += a[1]
    print(strg)
