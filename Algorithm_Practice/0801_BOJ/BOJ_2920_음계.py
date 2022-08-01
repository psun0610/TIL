music_num = list(map(int, input().split()))
asc = [1, 2, 3, 4, 5, 6, 7, 8]
if music_num == asc:
    print('ascending')
elif music_num == asc[::-1]:
    print('descending')
else:
    print('mixed')