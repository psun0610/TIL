for i in range(3):
    number = input()
    cnt = 1
    max_cnt = 1
    for j in range(7):
        if number[j] == number[j+1]:
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
        else:
            cnt = 1
    print(max_cnt)