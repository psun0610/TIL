# 테스트케이스 3개 런타임에러
'''
def solution(genres, plays):
    answer = []
    album = {}
    for i in range(len(genres)):
        if genres[i] not in album:
            album[genres[i]] = [[i, plays[i]]]
        else:
            album[genres[i]].append([i, plays[i]])

    print(album)

    for g in album:
        # 많이 재생된 노래 정렬
        album[g].sort(key = lambda x:-x[1])
    
    lenlist = []
    sumlist = []
    for g in album:
        # 많이 재생된 장르
        sum_ = 0
        len_ = 0
        for play in album[g]:
            sum_ += play[1]
            len_ += 1
        album[g].append(sum_)
        lenlist.append(len_)
        sumlist.append(sum_)
    sumlist.sort(reverse=True)

    for i in range(len(sumlist)):
        for g in album:
            print('album[g]', album[g])
            if sumlist[i] in album[g]:
                answer.append(album[g][0][0])
                if lenlist[i] >= 2:
                    answer.append(album[g][1][0])

    return answer
'''

def solution(genres, plays):
    answer = []
    dic1 = {}
    dic2 = {}
    
    for i, (g, v) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, v)]
        else:
            dic1[g] += [(i, v)]
        
        if g not in dic2:
            dic2[g] = v
        else:
            dic2[g] += v
    
    for key, value in sorted(dic2.items(), key = lambda x:x[1], reverse=True):   # 재생이 많이 된 장르 순
        for value1, value2 in sorted(dic1[key], key = lambda x:x[1], reverse=True)[:2]:     # 장르별로 재생이 많이 된 곡 순
            answer.append(value1)
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 150, 2500]))
