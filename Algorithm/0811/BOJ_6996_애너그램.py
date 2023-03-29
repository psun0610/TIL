T = int(input())
for test_case in range(T):
    a, b = input().split()
    lista = list(a)
    listb = list(b)
    if sorted(lista) == sorted(listb):
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')