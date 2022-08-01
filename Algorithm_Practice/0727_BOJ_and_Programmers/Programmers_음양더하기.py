def solution(absolutes, signs):
    len_ = len(absolutes)
    sum_ = 0
    for i in range(len_):
        if signs[i] is True:
            sum_ += absolutes[i]
        else:
            sum_ -= absolutes[i]
    return sum_