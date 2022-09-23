from django.shortcuts import render
import random

# Create your views here.
def index(request):

    return render(request, 'index.html')

def dinner(request):
    foods = [
        ['삼겹살', 'https://src.hidoc.co.kr/image/lib/2021/8/27/1630049987719_0.jpg'],
        ['연어초밥', 'https://ak-d.tripcdn.com/images/1i65u2224rw1i8rdsB808_R_400_10000_R5_Q100.jpg?proc=source/trip'],
        ['닭발', 'https://cdn-pro-web-251-112-godomall.spdycdn.net/pympym12_godomall_com/data/goods/20/03/10/1000000305/1000000305_detail_022.jpg'],
        ['보쌈', 'https://m.yorivery.com/data/goods/20/08/34//1000000919/1000000919_detail_051.jpg'],
        ['떡볶이', 'https://doewxs707ovkc.cloudfront.net/v3/prod/image/item/mainpage/907/ad4474bef39c4167b84477eaa7a5052f20210708171733.'],
        ['그딴 거 없음 굶어', 'https://blog.kakaocdn.net/dn/spr2T/btqY9ZJOdGz/3wFDVvBbGIqhg4K9qj2j10/img.gif'],
        ]
    food = random.choice(foods)
    context = {
        'food': food[0],
        'foodimg': food[1],
    }
    return render(request, 'dinner.html', context)


# 주작 메소드
# def lotto(request):
#     lottonums = []

#     ex = [3, 11, 15, 29 ,35, 44]
#     ex1 = [3, 11, 15, 29 ,35, 44,10]
#     bonus = 10


#     for i in range(5):
#         current = (random.sample(ex1,6))
#         dic = {}
#         dic['number'] = current

#         count = 12 - len(set(current+ex)) 
#         if count == 6:
#             dic['rank'] ='1등'
#         elif count == 5:
#             if bonus in current:
#                 dic['rank'] ='2등'
#             else:
#                 dic['rank'] ='3등'
#         elif count == 4:
#             dic['rank'] ='4등'
#         elif count == 3:
#             dic['rank'] ='5등'
#         else:
#             dic['rank'] ='꽝!'

#         lottonums.append(dic)

#     context = {
#         'lotto_nums': lottonums,
#         'lastweek': ex
#     }


#     return render(request,'lotto.html',context)


def lotto(request):
    lastweek = [3, 11, 15, 29, 35, 44]
    bonus = 10
    lotto_nums = []

    for i in range(5):
        dic = {}
        # 번호 구하기
        current = random.sample(range(1, 46), 6)
        # current.sort()
        dic['number'] = current

        # 등수 구하기
        cnt = 12 - len(set(lastweek + current))
        if cnt == 6:
            dic['rank'] = '1등'
        elif cnt == 5:
            if bonus in current:
                dic['rank'] = '2등'
            else:
                dic['rank'] = '3등'
        elif cnt == 4:
            dic['rank'] = '4등'
        elif cnt == 3:
            dic['rank'] = '5등'
        else:
            dic['rank'] = '꽝'

        lotto_nums.append(dic)

    context = {
        'lotto_nums': lotto_nums,
        'lastweek': lastweek,
        'bonus': bonus,
    }
    return render(request, 'lotto.html', context)