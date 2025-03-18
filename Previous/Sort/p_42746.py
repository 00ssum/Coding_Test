#시간 초과 나온 코드
from itertools import permutations
def solution(numbers):
    numbers=list(map(str,numbers))
    arr=list(map("".join, permutations(numbers,len(numbers))))
    arr.sort()
    answer = arr[-1]
    return answer
  
  #----------------------------------------
# 참고한 코드
import functools
def comparator(a,b):
    #ex> a=10 b=2 => -1 // 6, 10=> 1 // 6,2 =>1
    t1 = a+b #102
    t2 = b+a #210
    # t1이 크다면 1  // t2가 크다면 -1  //  같으면 0
    return (int(t1) > int(t2)) - (int(t1) < int(t2))

def solution(numbers):
    n=list(map(str,numbers))
    # cmp_to_key를 기준으로, 내림차순 정렬
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    answer = str(''.join(n)) #join으로 합쳐서 문자열로 바꾼뒤 출력
    return answer
