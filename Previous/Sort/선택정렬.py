for i in range(len(array)): 
    min_index = i#정렬 안된 데이터중 맨 앞자리 =바꿀 target의 위치
    for j in range(i+1, len(array)): #정렬 안된 값 중에 최소값 찾기
        if array[j] < array[min_index]:
            min_index = j #최소값 갱신
    array[i], array[min_index] = array[min_index], array[i] # SWAP : 바꿀 target의 위치<-> 가장 작은 데이터
