n = int(input())
cards = {}

# 최빈값 구하기
for _ in range(n):
    num = input()
    cards[num] = cards.get(num, 0) + 1

max_key = ''
max_value = 0
for card in cards:
    # value를 비교하여 더 큰 value를 찾아서 그의 키값구함
    if cards[card] > max_value or (cards[card] == max_value and int(card) < int(max_key)):
        max_key = card
        max_value = cards[card]

print(int(max_key))