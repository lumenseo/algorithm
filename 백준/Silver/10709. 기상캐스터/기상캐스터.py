H, W= map(int, input().split())
weather=[list(input()) for _ in range(H)]

result=[[-1]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if weather[i][j]=='c':
            result[i][j]=0

        elif j>0 and result[i][j-1] >=0 :
            result[i][j]=result[i][j-1]+1

for row in result:
    print(*row)