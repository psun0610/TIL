def solution(users, emoticons):
    answer = []
    user_perchase_list = []

    for i in [10, 20, 30, 40]:
        price = 0
        tmplist = []
        for j in range(len(emoticons)):
            price = int(emoticons[j] * (100-i)/100)
            for user in users:
                # 만약 user가 원하는 할인율을 넘으면 이모티콘별 구매리스트에 넣음
                if i >= user[0]:
                    tmplist.append(price)
                else:
                    tmplist.append(0)
        user_perchase_list.append(tmplist)

    print(user_perchase_list)

    # for perchase in user_perchase_list:


    return answer

users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
print(solution(users, emoticons))