import sys
input = sys.stdin.readline

cards = []
cards_count = [0] * 10
for _ in range(5):
    card = input().strip()
    cards.append(card)

cards.sort(reverse=True, key=lambda card: card[2])

same_color = True
continuous = True
for i in range(4):
    # 색이 모두 같은지 판별
    if same_color == True and cards[i][0] != cards[i + 1][0]:
        same_color = False
    # 5장이 모두 연속된 숫자인지 판별
    if continuous == True and int(cards[i][2]) - 1 != int(cards[i + 1][2]):
        continuous = False

# 같은 숫자가 몇 갠지 판별하기 위해서 cards_count에 넣기
for card in cards:
    cards_count[int(card[2])] += 1

# 이미 계산이 끝났다면 return으로 빠져나오기 위하여 함수로 작성함
def card_game():
    # 1. 5장이 모두 같은 색, 연속 숫자 => 가장 높은 숫자 + 900
    if same_color == True and continuous == True:
        return int(cards[0][2]) + 900
    # 2. 4장이 모두 같은 숫자 => 같은 숫자 + 800
    if 4 in cards_count:
        return cards_count.index(4) + 800
    elif 5 in cards_count:
        return cards_count.index(5) + 800
    # 3. 3장 같은 숫자, 2장 같은 숫자 => 3장 숫자 * 10 + 2장 숫자 + 700
    if 3 in cards_count and 2 in cards_count:
        return cards_count.index(3) * 10 + cards_count.index(2) + 700
    # 4. 5장 같은 색 => 가장 높은 숫자 + 600
    if same_color == True:
        return int(cards[0][2]) + 600
    # 5. 5장 연속 숫자 => 가장 높은 숫자 + 500
    if continuous == True:
        return int(cards[0][2]) + 500
    # 6. 3장 같은 숫자 => 같은 숫자 + 400
    if 3 in cards_count:
        return cards_count.index(3) + 400
    # 7. 2장 같은 숫자, 2장 같은 숫자 => 큰 숫자 * 10 + 작은 숫자 + 300
    two = 0
    two_big, two_small = 0, 0
    for i in range(len(cards_count)):
        if cards_count[i] == 2 and two == 1:
            two += 1
            two_big = i
        elif cards_count[i] == 2:
            two += 1
            two_small = i
    if two == 2:
        return two_big * 10 + two_small + 300
    # 8. 2장 같은 숫자 => 같은 숫자 + 200
    if two == 1:
        return two_small + 200
    # 9. 아무것도 아니라면
    return int(cards[0][2]) + 100

print(card_game())
