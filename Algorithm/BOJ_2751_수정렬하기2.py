import sys

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
print(*sorted(nums), sep="\n")
