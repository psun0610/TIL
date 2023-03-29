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
# 딕셔너리
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
'''
    
# 이진 탐색 O(logn)
def binary_search(left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if note1[mid] == target:
            return 1
        elif note1[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0
            
T = int(input())
for test_case in range(T):
    n = int(input())
    note1 = list(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))

    note1.sort()
    for num in note2:
        print(binary_search(0, n-1, num))