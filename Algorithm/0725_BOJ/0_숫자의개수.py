# https://www.acmicpc.net/problem/2577
from re import L
import sys

sys.stdin = open("0_숫자의개수.txt")

A = int(input())
B = int(input())
C = int(input())
abc = list(str(A*B*C))
# 인덱스 0부터 9까지 모두 0으로 초기화한 result 리스트를 만듬
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in abc:
    result[int(i)] += 1
# 출력부
for i in range(10):
    print(result[i])