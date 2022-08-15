# 리스트로 문제풀이 -> 시간초과
'''
T = int(input())
for test_case in range(T):
    n = int(input())
    note1 = list(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))

    for num in note2:
        if num in note1:
            print(1)
        else:
            print(0)
'''

T = int(input())
for test_case in range(T):
    n = int(input())
    note1 = list(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))

    number1 = {}
    for i in note1:
        number1[i] = number1.get(i, 0) + 1
    
    for i in note2:
        if i in number1:
            print(1)
        else:
            print(0)
        