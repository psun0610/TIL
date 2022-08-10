angle = [int(input()) for i in range(3)]
if angle[0] == 60 and angle[1] == 60 and angle[2] == 60:
    print('Equilateral')
elif sum(angle) == 180:
    if angle[0] == angle[1] or angle[1] == angle[2] or angle[2] == angle[0]:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')