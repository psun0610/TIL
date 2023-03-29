# mush = []
# for i in range(10):
#     mush.append(int(input()))

# ans = 0
# i = 0
# for i in range(10):
#     ans += mush[i]
#     if ans > 100:
#         break
# # 만약 버섯을 끝까지 다 먹었는데도 100이 넘지 않는다면 그대로 합 출력
# # if i == 9: 로 하면 i가 9일 때 ans가 100이 넘는 경우가 생기므로 틀림
# if ans < 100:
#     print(ans)

# else:
#     # 100이 넘기 직전까지의 합과 100을 넘은 후의 합의 절대값을 계산
#     pre = -(ans - mush[i] - 100)
#     next_ = ans - 100

#     # 100을 넘은 후의 합의 절대값이 더 작거나 같다면 합을 그대로 출력
#     if pre >= next_:
#         print(ans)
#     # 100을 넘기 직전의 합의 절대값이 더 작다면 합에서 mush[idx]를 뺀 값을 출력
#     else:
#         print(ans - mush[i])

##############################################

mush = []
for i in range(10):
    mush.append(int(input()))

ans = 0
for i in range(10):
    ans += mush[i]
    if ans == 100:
        break
    elif ans > 100:
        # 100을 넘은 후의 합의 절대값이 더 작거나 같다면 합을 그대로 출력
        if -(ans - mush[i] - 100) >= ans - 100:
            break
        else:
            ans = ans - mush[i]
            break
            
print(ans)