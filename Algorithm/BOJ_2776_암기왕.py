import sys
input = sys.stdin.readline

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
    for i in range(m):
        print(binary_search(0, n-1, note2[i]))