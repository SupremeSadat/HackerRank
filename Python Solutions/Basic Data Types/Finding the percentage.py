if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

total = 0
for mark in student_marks.get(query_name):
    total = total + mark

total = total/len(student_marks.get(query_name))

print(f'{total:.2f}')

