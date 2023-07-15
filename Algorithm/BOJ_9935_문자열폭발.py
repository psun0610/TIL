import sys

input = sys.stdin.readline

string = input().strip()
explore = input().strip()

stack = []

for i in range(len(string)):
    stack.append(string[i])
    if "".join(stack[-len(explore) :]) == explore:
        for j in range(len(explore)):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")
