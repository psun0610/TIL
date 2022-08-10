# a = input()
# b = input()
# c = input()
# d = input()
# e = input()
# ans = ''
# for i in range(len(a)):
#     ans += a[i]
#     if len(b) - 1 >= i:
#         ans += b[i]
#     if len(c) - 1 >= i:
#         ans += c[i]
#     if len(d) - 1 >= i:
#         ans += d[i]
#     if len(e) - 1 >= i:
#         ans += e[i]
# print(ans)

# ================

words = [input() for _ in range(5)]
ans = ''
len_list = [len(i) for i in words]
for i in range(max(len_list)):
    for word in words:
        if len(word) - 1 >= i:
            print(word[i], end = '')