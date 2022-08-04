for _ in range(int(input())):
    m, n = map(int, input().split())
    grid = [[]for _ in range(n)]
    for i in range(m):
        a = list(input().split())
        for j in range(n):
            grid[j].append(a[j])
    print(grid)

    movecnt = 0
    for i in range(n):
        boxNum = grid[i].count('1')
        floor = m - 1

        for j in range(m-1, -1, -1):
            if grid[i][j] == '1':
                movecnt += floor - j
                floor -= 1

    print(movecnt)