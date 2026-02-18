N= int(input())
people=[]

for _ in range(N):
    weight, height=map(int, input().split())
    people.append((weight,height))

ans=[]

for i in range(N):
    rank=1
    for j in range(N):
        if people[j][0]> people[i][0] and people[j][1] > people[i][1]:
            rank+=1
    ans.append(rank)

print(*ans)