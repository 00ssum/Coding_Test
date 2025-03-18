def quick_sort(array):
    if len(array) <=1: #빈 배열, 값이 1개만 전달될 경우
        return array # 해당 경우 종료

    pivot = array[0]  # [0]: 피벗
    tail = array[1:]  # [1]~[N] 피벗 외 리스트

#해당하는 값이 없을땐 빈 배열
    left_side = [x for x in tail if x <= pivot]  # 왼쪽 배열: 피봇보다 작거나 같은 값
    right_side = [x for x in tail if x > pivot]  # 오른쪽 배열: 피봇 보다 큰 값

    # 왼, 오른쪽 각각 정렬 수행
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(quick_sort(array))
