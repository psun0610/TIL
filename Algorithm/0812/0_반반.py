import sys

sys.stdin = open("_반반.txt")

T = int(input())
for test_case in range(1, T+1):
    word = list(input())
    word.sort()
    if word[0] == word[1] and word[2] == word[3] and word[0] != word[2]:
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')