N= int(input())
hints=[]
for _ in range(N):
    hints.append(list(map(int, input().split())))

answer_count=0

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i==j or j==k or k==i:
                continue

            candidate=[i, j, k]
            all_match=True

            for num, s, b in hints:
                h_num= [int(n) for n in str(num)]
                strike=0
                ball=0

                for idx in range(3):
                    if candidate[idx]==h_num[idx]:
                        strike+=1
                    elif h_num[idx] in candidate:
                        ball+=1
                if strike != s or ball != b:
                    all_match=False
                    break
            
            if all_match:
                answer_count+=1
print(answer_count)