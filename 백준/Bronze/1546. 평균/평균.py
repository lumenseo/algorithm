N=int(input())
scores=list(map(int, input().split()))
M=max(scores)

false_scores=[]
for score in scores:
    f_s=score/M*100
    false_scores.append(f_s)

total=0
for fscore in false_scores:
    total+=fscore
print(total/N)