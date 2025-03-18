def solution(N, stages):
    People = len(stages)
    loss = {}
    for i in range(2, N + 1):
        if People != 0:  
            loss[i] = stages.count(i) / People 
            People -= stages.count(i) #계산 완료한 사람 제거
        else: #해당 스테이지에 사람이 없으면
            loss[i] = 0

    loss=sorted(loss, key=lambda x: loss[x], reverse=True)
    return loss
