'''
EOF 처리 방법 2가지
1. try ~ exept
2. sys.stdin.read()
-> vscode는 사용자 입력을 받아서 처리하기 때문에 EOF에러가 발생하지 않음, 백준에서는 됨
'''
# import sys
# sent += sys.stdin.read()

sent = ''
while 1:
    try:
        sent += input()
    except:
        break

# sent = 'baekjoon online judge'
sent = sent.replace(' ', '').replace('\n', '')
alpha = [0] * 26
for s in sent:
    alpha[ord(s) - 97] += 1

for i in range(26):
    if alpha[i] == max(alpha):
        print(chr(i + 97), end = '')