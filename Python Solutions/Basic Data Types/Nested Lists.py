students = []
secondLow = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

students = sorted(students, key=lambda x: x[1])
first = students[0][1]
second = first
i = 0
while first == second:
    i = i + 1
    second = students[i][1]

for _ in students:
    if second == _[1]:
        secondLow.append(_[0])

secondLow.sort()
print(*secondLow, sep="\n")

