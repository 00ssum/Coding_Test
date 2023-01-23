n, c = list(map(int, input().split()))
array = []
for _ in range(n) :
  array.append(int(input()))
array.sort()

start = 1 # 가능한 최소 거리
end = array[n-1] - array[0] # 가능한 최대 거리
result = 0

# 최소 거리 ~최대거리 까지 이진탐색 하며, C개의 공유기를 설치 할 수 있는 mid값 찾음
while (start <= end) :
  mid = (start + end) // 2 #가장 인접한 두 공유기 사이의 거리
  value = array[0] #초기 공유기 설치
  count = 1 #초기 공유기 갯수

  # 현재의 mid값을 이용해 공유기를 설치
  for i in range(1, n) : # 앞에서부터 차근 차근 설치
    if array[i] >= value + mid :
      value = array[i] #설치된 위치 갱신
      count += 1 # 공유기 +1
  
  if count >= c : # 설치가능 공유기 > C
    start = mid + 1 #start 증가 (최적인지 확인)
    result = mid # 일단 가능한거 저장
  else : # C > 설치 가능 공유기
    end = mid - 1 #mid값 감소

print(result)
