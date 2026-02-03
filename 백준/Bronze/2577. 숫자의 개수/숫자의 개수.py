A= int(input())
B= int(input())
C= int(input())
result=A*B*C

counting=[0]*10

for i in str(result):
    num=int(i)
    counting[num]+=1

for count in counting:
    print(count)