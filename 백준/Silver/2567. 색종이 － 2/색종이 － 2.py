paper=[[0]*101 for _ in range(101)]

N= int(input())

for _ in range(N):
    x, y= map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            if 0<=i<100 and 0<=j<100:
                paper[i][j]=1

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

total_length=0

for i in range(101):
    for j in range(101):
        if paper[i][j]==1:
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]

                if nx<0 or nx>=101 or ny<0 or ny>=101:
                    total_length+=1
                elif paper[nx][ny]==0:
                    total_length+=1
print(total_length)