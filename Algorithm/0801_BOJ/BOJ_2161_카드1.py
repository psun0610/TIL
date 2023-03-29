from collections import deque
N = int(input())
card = deque(range(1, N+1))
trash = []

while len(card) > 1:
    trash.append(card.popleft())
    card.append(card.popleft())

print(*trash, card[0])