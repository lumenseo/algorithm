import sys
sys.setrecursionlimit(300000)

n, m= map(int, input().split())
arr= [list(map(int, input().split())) for _ in range(n)]

# 상 하 좌 우
dx=[-1, 1, 0, 0] # 행, 가로 방향으로 늘어선 줄, 을 바꾸니까 위아래 이동
dy=[0, 0, -1, 1] # 열, 세로 방향으로 늘어선 줄, 을 바꾸니까 좌우 이동

def dfs(x, y):
    arr[x][y]=0
    area=1

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<m:
            if arr[nx][ny]==1:
                area += dfs(nx, ny)
    
    return area

picture_count=0
max_area=0

for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            picture_count+=1
            current_area= dfs(i,j)
            max_area=max(max_area, current_area)

print(picture_count)
print(max_area)