def solution(citations):
    citations.sort(reverse=True) #내림차순 정렬
    #[6,5,3,1,0]
    for idx , citation in enumerate(citations):
        if idx >= citation: #인덱스(값보다 큰 논문의 수) >= 값
            return idx

    return len(citations) #값이 인덱스보다 크면= 인덱스 길이
