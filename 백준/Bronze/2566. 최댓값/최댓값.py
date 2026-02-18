row= [list(map(int, input().split())) for _ in range (9)]
max_r= 0
max_c= 0
max_num=-1

for i in range(9):
    for j in range(9):
        if max_num <= row[i][j]:
            max_num = row[i][j]
            max_r= i+1
            max_c= j+1

print(max_num)
print(max_r, max_c)