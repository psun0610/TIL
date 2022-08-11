works = list(map(int, input().split()))
if sum(works) >= 100:
    print('OK')
else:
    min_work = works.index(min(works))
    if min_work == 0:
        print('Soongsil')
    elif min_work == 1:
        print('Korea')
    else:
        print('Hanyang')