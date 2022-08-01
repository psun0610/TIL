a_card = list(map(int, input().split()))
b_card = list(map(int, input().split()))
a_score = 0
b_score = 0
winner = ''
for i in range(10):
    if a_card[i] > b_card[i]:
        a_score += 3
        winner = 'A'
    elif b_card[i] > a_card[i]:
        b_score += 3
        winner = 'B'
    else:
        a_score += 1
        b_score += 1

print(a_score, b_score)
if a_score > b_score:
    winner = 'A'
elif b_score > a_score:
    winner = 'B'
# 모두 비겼을 경우
if winner == '':
    winner = 'D'

print(winner)