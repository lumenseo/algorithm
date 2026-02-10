def fibo(num):
    if num <= 1:   #종료조건
        return num
    
    if memo.get(num):   # 메모에 값이 있는 경우, 계산한 적이 있다면, .get() 안쓰면 오류
        return memo[num]   # 기존 기록된 값을 return
    
    # 한 번이라도 연산했다면, 딕셔너리에 기록
    memo[num]=fibo(num-1)+fibo(num-2)
    return memo[num]


n=int(input())
memo={}
result=fibo(n)
print(result)