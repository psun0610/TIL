import sys
input = sys.stdin.readline

def is_int(n):
    try:
        int(n)
        return True
    except:
        return False

n, m = map(int, input().split())
pokemons = {}
pokemons_reverse = {}
num = 0
for i in range(n):
    num += 1
    pokemons[input().strip()] = num
pokemons_reverse = dict(map(reversed, pokemons.items()))

for i in range(m):
    what = input().strip()
    if is_int(what):
        print(pokemons_reverse.get(int(what)))
    else:
        print(pokemons.get(what))
    