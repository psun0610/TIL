# def PrintStar(n, star):
#     if n == 1:
#         return star
#     for i in range(int(n / 3) + 1, int(n * 2/3) + 1):
#         for j in range(int(n / 3) + 1, int(n * 2/3) + 1):
#             star[i][j] = ' '
#     return PrintStar(n / 3, star)
    

# n = int(input())
# star = [['*'] * (n+1) for _ in range(n+1)]
# star = PrintStar(n, star)
# for i in range(1, len(star)):
#     for j in range(1, len(star)):
#         print(star[i][j], end='')
#     print()


def PrintStar(n):
    if n == 3:
        return ['***', '* *', '***']
    list_ = PrintStar(n//3)
    star = []
    for i in list_:
        star.append(i * 3)
    for i in list_:
        star.append(i + ' ' * (n//3) + i)
    for i in list_:
        star.append(i * 3)
    return star

n = int(input())
star = PrintStar(n)
for i in star:
    print(i)