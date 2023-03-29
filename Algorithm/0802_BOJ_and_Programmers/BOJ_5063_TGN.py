N = int(input())
for _ in range(N):
    r, e, c = map(int, input().split())
    adv = r - (e - c)
    if adv > 0:
        print('do not advertise')
    elif adv == 0:
        print('does not matter')
    else:
        print('advertise')