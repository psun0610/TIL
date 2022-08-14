alpha = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while 1:
    sent = input()
    if sent == '#':
        break
    cnt = 0
    for a in alpha:
        cnt += sent.count(a)
    print(cnt)