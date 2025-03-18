for i in range(1, len(array)): # [1]번부터 시작: 정렬 안된 데이터중 맨 앞자리 =바꿀 target의 위치
    for j in range(i, 0, -1): # target부터 -1씩 (왼쪽으로)자리 이동
        if array[j] < array[j-1]:#target보다 큰값이면 
            array[j], array[j-1] = array[j-1], array[j] #한칸씩 뒤로 밀음
        else:  # 나보다 작은값을 만나면
            break #그자리에 삽입
