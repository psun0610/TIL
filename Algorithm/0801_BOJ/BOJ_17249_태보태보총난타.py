# @가 나올때마다 count하면 됨
taebo = input()
left_punch = 0
right_punch = 0
turn = False
for punch in taebo:     # @===@==@=@==(^0^)==@=@===@
    if punch in '(^0^)':
        turn = True
    if turn == False:
        if punch == '@':
            left_punch += 1
    else:
        if punch == '@':
            right_punch += 1
print(left_punch, right_punch)

# 방법 2
taebo = input()
turn_index = taebo.find('(^0^)')
left = taebo[:turn_index]
right = taebo[turn_index+6:]
print(left.count('@'), right.count('@'))