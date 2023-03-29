n, jimin, hansu = map(int, input().split())
cnt = 0
while jimin != hansu:
    jimin -= jimin // 2
    hansu -= hansu // 2
    cnt += 1
print(cnt)
