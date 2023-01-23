n=int(input())
s_list= list(map(int,input().split()))
m=int(input())
c_list= list(map(int,input().split()))

# 방법 1:
for i in range(len(c_list)):
    if c_list[i] in s_list:
        print("yes", end=" ")
    else:
        print("no",end=" ")
        
        
# 방법 2: 
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2 #중간점
        if array[mid] == target: # 중간점 값= 찾는값 => 찾기 완료
            return mid

        elif array[mid] > target: # 중간점 값 > 찾는값
            end = mid - 1 #end 수정

        else:# 중간점 값 < 찾는값
            start = mid + 1 #start 수정
    return None

n=int(input())
s_list= list(map(int,input().split()))
m=int(input())
c_list= list(map(int,input().split()))

s_list.sort()
for i in c_list:
    result = binary_search(s_list, i, 0, n - 1)
if result == None:
    print("yes", end=" ")
else:
    print("no", end=" ")
