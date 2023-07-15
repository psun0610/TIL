def solution(users, emoticons):
    rate = [10, 20, 30, 40]
    discount_list = [0] * len(emoticons)
    answer = [-1, -1]

    def search(idx):
        if idx == len(emoticons):
            cur_plus, cur_sale = 0, 0
            for i in range(len(users)):
                current_user_sum = 0
                for j in range(len(emoticons)):
                    # 유저의 기준 할인율보다 높다면 이 유저가 쓸 금액의 총합에 더함
                    if discount_list[j] >= users[i][0]:
                        current_user_sum += (
                            emoticons[j] * (100 - discount_list[j]) / 100
                        )
                # 유저가 쓸 금액의 총합이 기준 가격보다 높다면 플러스 유저 + 1
                if current_user_sum >= users[i][1]:
                    cur_plus += 1
                # 아니면 판매액에 더함
                else:
                    cur_sale += current_user_sum
                # 현재 answer과 비교하여 더 적합한 것으로 교체
                if (
                    cur_plus > answer[0]
                    or cur_plus == answer[0]
                    and cur_sale > answer[1]
                ):
                    answer[0] = cur_plus
                    answer[1] = cur_sale
            return

        for i in range(4):  # 할인율 완전탐색
            discount_list[idx] = rate[i]
            search(idx + 1)

    search(0)

    return answer


users = [
    [40, 2900],
    [23, 10000],
    [11, 5200],
    [5, 5900],
    [40, 3100],
    [27, 9200],
    [32, 6900],
]
emoticons = [1300, 1500, 1600, 4900]

print(solution(users, emoticons))
