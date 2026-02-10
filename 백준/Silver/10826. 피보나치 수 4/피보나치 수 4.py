import sys
sys.setrecursionlimit(10**7)


def fibo(num):
    if num<=1:
        return num
    if memo.get(num): # 메모이제이션
        return memo[num]
    
    memo[num]=fibo(num-1)+fibo(num-2)
    return memo[num]


n=int(input())
memo={}
result=fibo(n)
print(result)