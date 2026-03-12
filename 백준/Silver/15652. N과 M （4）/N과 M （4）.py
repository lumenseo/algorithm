N, M= map(int, input().split())

path=[]

# 시작: 0개의 숫자 선택
# 종료: M개의 숫자 선택
# 다음: 다음 숫자 호출

def recur(cnt, prev):
    # 종료조건:
    if cnt==M:
        print(*path)
        return

    # 다음 호출:
    for i in range(prev, N+1):
        path.append(i)
        recur(cnt+1, i)
        path.pop()
        
recur(0,1)
