n=int(input())
dic={}
for i in range(n):
    val,key=input().split()
    dic[int(key)]=val

so_dic=sorted(dic.values())
print(*so_dic)
