n = int(input())
note1 = list(map(int, input().split()))
m = int(input())
note2 = list(map(int, input().split()))

number1 = {}
for i in note1:
    number1[i] = number1.get(i, 0) + 1

for i in note2:
    if i in number1:
        print(1, end = ' ')
    else:
        print(0, end = ' ')