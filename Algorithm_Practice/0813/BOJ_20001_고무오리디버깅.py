question = 0
while 1:
    message = input()
    if message == '고무오리 디버깅 시작':
        continue

    if message == '문제':
        question += 1
    if message == '고무오리':
        if question == 0:
            question += 2
        else:
            question -= 1

    if message == '고무오리 디버깅 끝':
        if question == 0:
            print('고무오리야 사랑해')
        else:
            print('힝구')
        break