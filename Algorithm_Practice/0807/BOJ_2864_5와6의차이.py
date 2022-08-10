# 최솟값은 6을 5로
# 최댓값은 5를 6으로 변환하여 합 계산

a, b = input().split()
print(sum([int(a.replace('6', '5')), int(b.replace('6', '5'))]),
        sum([int(a.replace('5', '6')), int(b.replace('5', '6'))]))