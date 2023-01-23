# 상하좌우 움직임에 맞는 배열을 각각 만든게 특이함
#책코드
N = int(input())
map = list(input().split())
x,y = 1,1

# 상,하,좌,우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
move_type = ['U','D','L','R']

# 이동 방향을 하나씩 확인
for i in map:
  # 이동 후 좌표 구하기
  for j in range(len(move_type)):
    if i == move_type[j]: # 해당하는 움직임일 때
      nx = x + dx[j]
      ny = y + dy[j]
  # 공간을 벗어나는 경우 무시
  if 1 > nx or nx > N or ny < 1 or ny > N:
    continue
  x,y = nx,ny
  
  
  
  ---------------------------------
  #내코드
  n= int(input())
s= list(input().split())
init=[1,1]

for i in s:
    if i=='R'and (init[1]+1)<=n:
        init[1]+=1
    elif i=='L'and (init[1]-1)>=1:
        init[1]-=1
    if i=='U'and (init[0]-1)>=1:
        init[0]-=1
    if i=='D'and (init[0]+1)<=n:
        init[0]+=1

print(init)
