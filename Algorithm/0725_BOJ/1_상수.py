# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

# A, B를 문자열로 받음
A, B = input().split()
# A, B를 문자열 슬라이싱을 이용하여 뒤집어 준 후 int()함수로 형변환함
A = int(A[::-1])
B = int(B[::-1])
# 더 큰 값을 result에 저장하여 출력함
result = A if A > B else B
print(result)