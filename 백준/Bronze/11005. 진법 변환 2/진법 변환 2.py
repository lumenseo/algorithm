N, B= map(int, input().split())

result=[]

chars="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while N != 0:
    remainder = N % B
    result.append(chars[remainder])
    N= N//B

result.reverse()
print("".join(result))