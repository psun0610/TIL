# 방법1 - 시간초과 뜸
'''
import sys
input = sys.stdin.readline
n = int(input())
participant = [input() for _ in range(n)]
complete = [input() for _ in range(n-1)]
for part in participant:
    if part not in complete:
        print(part)
        break
'''

import sys
input = sys.stdin.readline
n = int(input())
participant = {}

for _ in range(n):
    name = input()
    participant[name] = participant.get(name, 0) + 1

for _ in range(n-1):
    name = input()
    participant[name] -= 1

for key, value in participant.items():
    if value >= 1:
        print(key)