N= int(input())
arr=[list(map(int, input())) for _ in range(N)]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

# dfs
def dfs(x, y):
    arr[x][y]=0
    count=1

    # 델타 개념 적용
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        # 범위를 벗어나지 않는다면
        if 0<=nx<N and 0<=ny<N:
            # 연결된 부분도 1이라면
            if arr[nx][ny]==1:
                count += dfs(nx, ny)
    return count

# 정답 코드 작성
complex_count=[]

for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            complex_count.append(dfs(i,j))

complex_count.sort()

print(len(complex_count))
for count in complex_count:
    print(count)
