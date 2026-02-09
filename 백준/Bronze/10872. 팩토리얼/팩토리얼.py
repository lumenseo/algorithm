result=1

def factorial(num):
    global result
    if num<=1:
        return
    
    result*=num

    factorial(num-1)

N=int(input())
factorial(N)
print(result)