from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")


def ping(request):
    return render(request, "ping.html")


def pong(request):
    # print(request)
    # print(dir(request))
    # print(request.GET.get('ball'))
    # ball = request.GET.get('ball')
    # context = {
    #     'name': ball,
    # }
    return render(request, "pong.html", {"name": request.GET.get("ball")})


def oddeven(request, number):
    if number == 0:
        answer = 0
    elif number % 2 == 0:
        answer = "짝수"
    else:
        answer = "홀수"

    context = {
        "number": number,
        "answer": answer,
    }
    return render(request, "oddeven.html", context)


def calculate(request, firstnum, secondnum):
    plus = firstnum + secondnum
    minus = firstnum - secondnum
    multi = firstnum * secondnum
    devision = firstnum // secondnum
    context = {
        "plus": plus,
        "minus": minus,
        "multi": multi,
        "devision": devision,
        "firstnum": firstnum,
        "secondnum": secondnum,
    }
    return render(request, "calculate.html", context)


def pl_test(request):
    return render(request, "pltest.html")


import random


def pl_result(request):
    pokemon_list = [
        {
            "name": "루주라",
            "imglink": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxODA1MDhfMTAw%2FMDAxNTI1NzY5MjI1MDQ2.L0ce7VLo6dfPE634Rukt6X35aDvkSaEMvYh3GV9y9Nsg.pxx_ZDJX1zC3oAFJIZ4qJFlF4f3Q72dgC9G7Zc04MjIg.GIF.jessica3954%2FexternalFile-14.gif&type=sc960_832_gif",
        },
        {
            "name": "깨봉이",
            "imglink": "https://mblogthumb-phinf.pstatic.net/20130501_137/ahn3607_1367416033294usyCu_JPEG/bw012.flv_001108000.jpg?type=w2",
        },
        {
            "name": "질퍽이",
            "imglink": "https://mblogthumb-phinf.pstatic.net/MjAxODAyMTZfMTYg/MDAxNTE4NzEwNjA5Mzk1.C5aOyQU-oQIIvdhKvaGcBMOpR5OFpFpCUJC0MBCUPw0g.FIDNxnS7zux23bOfoEv6MxYg63VIpYoa5onjM5qmANUg.GIF.lcj1222/tumblr_mmd5wiyMiw1s5mujoo1_400.gif?type=w800",
        },
        {
            "name": "또가스",
            "imglink": "http://img.dmitory.com/img/201805/gNW/EYV/gNWEYV6bnyGoOOIqE8CgY.gif",
        },
        {
            "name": "잉어킹",
            "imglink": "https://cdn.ppomppu.co.kr/zboard/data3/2020/0502/20200502133734_oddyiqea.gif",
        },
        {
            "name": "우츠동",
            "imglink": "https://mblogthumb-phinf.pstatic.net/20160229_125/dndidu_1456753462604pfkf1_GIF/tumblr_nwoo8eED7c1tgjlm2o1_500.gif?type=w2",
        },
        {
            "name": "닥트리오",
            "imglink": "https://postfiles.pstatic.net/MjAxNjEwMTlfMjEz/MDAxNDc2ODU2MDIzMDI3.XZZEX0k7DmOsHGVLFdATDi1n_JZXvLrbma6I4vmYQWEg.0hB96iDaggpqhhZrdpClfo8kqrgcYGw2eAvFhtEUiuQg.GIF.b6789000/tumblr_of8y26Ii0C1vxkyzno1_500.gif?type=w2",
        },
        {
            "name": "골뱃",
            "imglink": "http://24.media.tumblr.com/204c064f4e930ed294b89c49957c250f/tumblr_muargfR1H01rw0xupo2_500.gif",
        },
        {
            "name": "메타몽",
            "imglink": "https://blog.kakaocdn.net/dn/spr2T/btqY9ZJOdGz/3wFDVvBbGIqhg4K9qj2j10/img.gif",
        },
    ]
    plname = request.GET.get("plname")
    random.seed(plname)
    random.shuffle(pokemon_list)
    context = {"plname": plname, "pokemon": pokemon_list[6]}
    return render(request, "plresult.html", context)


def lipsum(request):
    return render(request, "lipsum.html")


def lipsum_result(request):
    para = int(request.GET.get("para"))
    word = int(request.GET.get("word"))
    answer = []
    word_list = ["루주라", "깨봉이", "질퍽이", "또도가스", "잉어킹", "고라파덕", "골뱃", "이상해씨", "픽시", "식스테일"]
    for i in range(para):
        tmp_word = ""
        for j in range(word):
            tmp_word = tmp_word + random.choice(word_list) + " "
        answer.append(tmp_word)

    context = {
        "answer": answer,
    }
    return render(request, "lipsum_result.html", context)
