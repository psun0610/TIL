alpha = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
sent = input()
while sent != '#':
    cnt = 0
    for a in alpha:
        cnt += sent.count(a)
    print(cnt)
    sent = input()