paper=[[0]*100 for _ in range(100)]

N= int(input())

for _ in range (N):
    x, y= map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            if 0 <= i <=100 and 0<= j <=100:
                paper[i][j]=1

result=0
for row in paper:
    result+=sum(row)

print(result)