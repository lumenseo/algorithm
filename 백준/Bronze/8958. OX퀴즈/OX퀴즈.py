T = int(input())

for tc in range(1, T+1):
    arr=list(input())

    count=0
    total=0
    for result in arr:
        if result=='O':
            count+=1
            total+=count
        else:
            count=0
    
    print(total)