import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    formula = input()
    left, right = formula.split('=')
    if eval(left) == int(right):
        print('correct')
    else:
        print('wrong answer')