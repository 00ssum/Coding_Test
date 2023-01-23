def solution(brown, yellow):
    #yellow = x * y
    #brown = 2*(x+y) + 4
    #(brown - 4)//2 = x + y
    
    x = 0
    sum = (brown - 4) // 2 #x+y

    for r in range(sum): #0 ~ x+y
        if r * (sum-r) == yellow: #x *y =yellow
            x = max(r, sum-r) #둘중 큰수가 x
            break
            
    answer = [x + 2 , sum-x + 2] # y,x값 +2씩
    return answer
