dwarfs=[]
for _ in range(9):
    dwarfs.append(int(input()))

total_sum=sum(dwarfs)
fake_sum=total_sum-100

spy1, spy2=0,0
for i in range(9):
    for j in range(i+1, 9):
        if dwarfs[i]+dwarfs[j]==fake_sum:
            spy1=dwarfs[i]
            spy2=dwarfs[j]
            break
    if spy1 != 0:
        break

dwarfs.remove(spy1)
dwarfs.remove(spy2)

dwarfs.sort()

for d in dwarfs:
    print(d)