word = input()
cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for cro in cro_list:
    word = word.replace(cro, '#').strip()
print(len(word))