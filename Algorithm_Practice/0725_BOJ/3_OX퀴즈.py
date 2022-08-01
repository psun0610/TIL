# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())
for testcase in range(T):
    # record 리스트에 입력받은 문자열을 하나씩 잘라서 넣음
    record = list(input())
    # 연속된 O의 점수를 매겨줄 tmp 변수와 모든 점수의 합을 저장할 ans 변수를 선언함
    tmp = 0
    ans = 0
    # record 리스트를 순회하며 X면 tmp를 0으로, O면 O의 점수(tmp)를 1 높인 후 O의 점수를 더함
    for i in record:
        if i == 'X':
            tmp = 0
        else:
            tmp += 1
            ans += tmp
    print(ans)