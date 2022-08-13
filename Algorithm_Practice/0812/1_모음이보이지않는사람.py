import sys

sys.stdin = open("_모음이보이지않는사람.txt")

alpha = ['a', 'e', 'i', 'o', 'u']
T = int(input())
for test_case in range(1, T+1):
    word = input()
    for i in range(5):
        word = word.replace(alpha[i], '')
    print(f'#{test_case} {word}')
