n = int(input())
gold = 0
for number in range(n+1):
    strnum = str(number)
    if strnum.count('4') + strnum.count('7') == len(strnum):
        gold = number
print(gold)