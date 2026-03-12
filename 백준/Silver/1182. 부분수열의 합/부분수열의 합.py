N, S= map(int, input().split())
num= list(map(int, input().split()))

cnt=0

def recur(idx, subset):
    global cnt

    # 기저조건
    if idx==N:
        if len(subset)!= 0 and sum(subset)==S:
            cnt += 1
        return
    
    # 포함하는 경우
    recur(idx+1, subset+[num[idx]])
    # 아닌 경우
    recur(idx+1, subset)


recur(0, [])
print(cnt)