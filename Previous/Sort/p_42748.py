def solution(array, commands):
    answer=[]
    for comm in commands:
        i,j,k = comm
        s=array[i-1:j]
        s.sort()
        answer.append(s[k-1])
    return print(answer)
