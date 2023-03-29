import sys
input = sys.stdin.readline
# sys.stdin = open("swea_input.txt", "r")

opens = ['[', '{', '<', '(']
close = [']', '}', '>', ')']

for test_case in range(10):
    ans = 0
    n = int(input())
    stack = []
    brackets = input().strip()
    for i in range(n):
        # 여는 괄호면 stack에 append
        if brackets[i] in opens:
            stack.append(brackets[i])
        # 닫는 괄호면
        # stack 길이가 0이 아닌지 확인하고
        # 남은 stack중에 close의 인덱스랑 일치하는 숫자가 있는지 확인한 후 pop
        else:
            if close.index(brackets[i]) == opens.index(stack[-1]):
                stack.pop()
            else:
                break
    else:
        if len(stack) == 0:
            ans = 1

    print(f'#{test_case+1} {ans}')