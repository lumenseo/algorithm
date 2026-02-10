# 시작점: N
# 끝점: 1
# 누적값(전달되는 값): N//2 

def recur(num):
    if num==0:
        return 
    
    recur(num//2) # 2로 나눈 몫을 전달  # 일단 끝까지 들어갔다가
    print(num%2, end='')  # 되돌아오면서 출력하자 # 어떤 걸 할것인지를 줄 위치를 제대로

N=int(input())
recur(N)