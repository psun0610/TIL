emoticon = [':-)', ':-(']
message = input()
happy = message.count(emoticon[0])
sad = message.count(emoticon[1])
if happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
elif happy == 0 and sad == 0:
    print('none')
elif happy == sad:
    print('unsure')