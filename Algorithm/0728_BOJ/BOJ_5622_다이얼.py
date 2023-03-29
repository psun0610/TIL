# word = input()
# time = 0
# # dial = {2: ['A', 'B', 'C'],
# #         3: ['D', 'E', 'F'],
# #         4: ['G', 'H', 'I'],
# #         5: ['J', 'K', 'L'],
# #         6: ['M', 'N', 'O'],
# #         7: ['P', 'Q', 'R', 'S'],
# #         8: ['T', 'U', 'V'],
# #         9: ['W', 'X', 'Y', 'Z']
# # }
# for alpha in word:
#     if alpha == 'A' or alpha == 'B' or alpha == 'C':
#         time += 3
#     elif alpha == 'D' or alpha == 'E' or alpha == 'F':
#         time += 4
#     elif alpha == 'G' or alpha == 'H' or alpha == 'I':
#         time += 5
#     elif alpha == 'J' or alpha == 'K' or alpha == 'L':
#         time += 6
#     elif alpha == 'M' or alpha == 'N' or alpha == 'O':
#         time += 7
#     elif alpha == 'P' or alpha == 'Q' or alpha == 'R' or alpha == 'S':
#         time += 8
#     elif alpha == 'T' or alpha == 'U' or alpha == 'V':
#         time += 9
#     else:
#         time += 10
# print(time)


# 방법 2
word = input()
time = 0
dial = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]
for alpha in word:
    time += dial[ord(alpha)-65]
print(time)