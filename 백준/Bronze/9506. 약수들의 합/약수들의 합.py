while True:
    N= int(input())
    if N==-1:
        break
    a=[]
    for i in range(N,1,-1):
        if N%i==0:
            a.append(N//i)
        
    if sum(a)==N:
        print(f'{N} = {" + ".join(map(str, a))}')
    else:
        print(f'{N} is NOT perfect.')