stack=[]
def binary(num):
    global stack
    if num==0:
        return
    binary(num//2)
    stack.append(num%2)

N=int(input())
binary(N)
print(''.join(map(str, stack)))