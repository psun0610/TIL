w_list = [int(input()) for _ in range(10)]
k_list = [int(input()) for _ in range(10)]

w_list.sort()
k_list.sort()

w_score = w_list[-1] + w_list[-2] + w_list[-3]
k_score = k_list[-1] + k_list[-2] + k_list[-3]

print(w_score, k_score)