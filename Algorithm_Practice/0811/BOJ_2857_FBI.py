ans = []
for i in range(5):
    name = input()
    # spy_name = name[name.index('-')+1:]
    if 'FBI' in name:
        ans.append(i+1)

if len(ans) == 0:
    print('HE GOT AWAY!')
else:
    print(*ans)
    