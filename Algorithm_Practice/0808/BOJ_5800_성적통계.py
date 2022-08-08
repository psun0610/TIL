k = int(input())
for t in range(1, k+1):
    student = list(map(int, input().split()))
    student.pop(0)

    student.sort()
    largestgap = 0
    for i in range(len(student) - 1):
        if abs(student[i] - student[i+1]) > largestgap:
            largestgap = abs(student[i] - student[i+1])

    print(f'Class {t}\nMax {max(student)}, Min {min(student)}, Largest gap {largestgap}')