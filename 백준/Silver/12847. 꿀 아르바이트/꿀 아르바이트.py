import sys
input= sys.stdin.readline

n, m= map(int, input().split())
wages=list(map(int, input().split()))

# 예외 처리: 일할 수 있는 날이 0일인 경우 벌 수 있는 돈은 0원
# if m == 0:
#     print(0)
#     exit()

# 1. 첫 번째 윈도우의 합 구하기
window_sum= sum(wages[:m])
max_wage = window_sum

# 2. 슬라이딩 윈도우 시작
for i in range(m, n):
    # 이전 윈도우 합 - 이전날 급여 + 다음 날 급여
    window_sum= window_sum - wages[i-m] + wages[i]

    if window_sum > max_wage:
        max_wage=window_sum

print(max_wage)