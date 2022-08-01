best_score = 0
winner = 0
for i in range(1, 6):
    chef = list(map(int, input().split()))
    score = sum(chef)
    if best_score < score:
        best_score = score
        winner = i
print(winner, best_score)