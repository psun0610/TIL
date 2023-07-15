import sys

input = sys.stdin.readline

stack1 = list(input().strip())
stack2 = []
m = int(input())

for i in range(m):
    command = input().strip()
    if command == "L":
        if stack1:
            stack2.append(stack1.pop())

    elif command == "D":
        if stack2:
            stack1.append(stack2.pop())

    elif command == "B":
        if stack1:
            stack1.pop()

    else:
        stack1.append(command[2])

stack1.extend(reversed(stack2))
print("".join(stack1))

""" 시간 초과 코드
letter = input().strip()
m = int(input())
cursor = len(letter)

for i in range(m):
    command = input().strip()
    if command == "L":
        if cursor > 0:
            cursor -= 1

    elif command == "D":
        if cursor < len(letter):
            cursor += 1

    elif command == "B":
        if cursor > 0:
            letter = letter[: cursor - 1] + letter[cursor:]
            cursor -= 1
    else:
        letter = letter[:cursor] + command[-1] + letter[cursor:]
        cursor += 1

print(letter)
"""
