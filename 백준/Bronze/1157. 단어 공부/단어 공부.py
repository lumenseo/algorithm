string=input().upper()
for_counting=list(set(string))

cnt_list=[]
for char in for_counting:
    num_count=string.count(char)
    cnt_list.append(num_count)

max_count=max(cnt_list)

if cnt_list.count(max_count)>1:
    print('?')
else:
    max_index=cnt_list.index(max_count)
    print(for_counting[max_index])