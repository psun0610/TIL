resistance = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}
color = [input() for _ in range(3)]
answer = int(str(resistance[color[0]]) + str(resistance[color[1]])) * (10**resistance[color[2]])
print(answer)