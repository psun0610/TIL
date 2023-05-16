"""
조건
1. 이름의 길이가 짧을수록 앞에
2. 길이가 같으면 사전 순
3. 중복 삭제
"""

import sys

input = sys.stdin.readline

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    name_list = list(set([input().strip() for _ in range(N)]))  # set으로 중복제거
    name_list.sort(key=lambda x: (len(x), x))

    print(f"#{i}")
    print(*name_list, sep="\n")
