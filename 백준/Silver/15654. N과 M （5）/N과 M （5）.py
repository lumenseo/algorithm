N, M= map(int, input().split())

num= list(map(int, input().split()))
num.sort()
    
path=[]
used=[0]*(N+1)

# 시작: 0개의 숫자 선택
# 종료: M개의 숫자 선택
# 다음: 다음 숫자 호출

def recur(cnt):
    # 종료조건:
    if cnt==M:
        print(*path)
        return

    # 다음 호출:
    for i in range(N):
        if used[i]:
            continue

        used[i]=1
        path.append(num[i])
        recur(cnt+1)
        path.pop()
        used[i]=0
        
recur(0)
