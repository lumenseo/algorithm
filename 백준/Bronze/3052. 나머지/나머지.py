num_list=[]
rest_set=set()

# 수 10개를 입력받은 뒤, 이를 리스트에 저장
for _ in range(10):
    a=int(input())
    num_list.append(a)
# 리스트를 돌면서 그 값을 42로 나눈 나머지를 구하고, set에 넣기
for num in num_list:
    rest=num%42
    rest_set.add(rest)

print(len(rest_set))