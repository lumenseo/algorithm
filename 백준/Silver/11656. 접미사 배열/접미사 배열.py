S=input()

suffix_list=[]
for i in range(len(S)):
    a=S[i:]
    suffix_list.append(a)
#print(suffix_list)
result=sorted(suffix_list)

for i in result:
    print(i)