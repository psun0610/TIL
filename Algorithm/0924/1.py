def solution(today, terms, privacies):
    answer = []
    ty, tm, td = map(int, today.split('.'))
    terms_dic = {}

    # 딕셔너리에 옮겨 담음
    for term in terms:
        alpha, num = term.split()
        terms_dic[alpha] = int(num)

    for i in range(len(privacies)):
        # date와 alpha에 수집일자, 약관 종류 담음
        date, alpha = privacies[i].split()
        dy, dm, dd = map(int, date.split('.'))
        # able에 이 약관의 유효기간 담음
        able = terms_dic[alpha]
        
        ay, am, ad = 0, 0, 0
        # 날짜 계산함
        if dd != 1:
            ad = dd - 1
            month = dm + able
            if month % 12 == 0:
                am = 12
                ay = dy + (month // 12) - 1
            else:
                am = month % 12
                ay = dy + (month // 12)

        else:
            ad = 28
            month = dm + able - 1
            if month % 12 == 0:
                am = 12
                ay = dy + (month // 12) - 1
            else:
                am = month % 12
                ay = dy + (month // 12)

        # 오늘 날짜와 비교
        if (ay < ty) or (ay == ty and am < tm) or (ay == ty and am == tm and ad < td):
            answer.append(i+1)

    return answer

today = '2022.05.28'
terms = ['A 18', 'B 12', 'C 6']
privacies = ['2021.06.12 A', '2020.01.01 B', '2021.06.12 C', '2022.02.20 C']
print(solution(today, terms, privacies))