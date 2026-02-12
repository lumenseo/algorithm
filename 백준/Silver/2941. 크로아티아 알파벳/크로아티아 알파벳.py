n=input()
croatia=['c=', 'c-','dz=','d-','lj','nj', 's=', 'z=']

for i in croatia:
    if i in n:
        n= n.replace(i,'*')

# print(len(n))

cnt=0
for i in n:
    cnt+=1
print(cnt)