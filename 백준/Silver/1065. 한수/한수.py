N= int(input())

hansu_count=0

for i in range(1,N+1):
    if i<100:
        hansu_count+=1
    else:
        nums=list(map(int, str(i)))

        if nums[1]-nums[0]==nums[2]-nums[1]:
            hansu_count+=1
print(hansu_count)