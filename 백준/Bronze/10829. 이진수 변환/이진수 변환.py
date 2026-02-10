# return 으로 활용하기

# 시작점: N
# 끝점: 0
# 누적값(전달되는값): N//2
def recur(num):
    if num == 0:
        return ""

    return recur(num // 2) + str(num % 2)


N = int(input())
print(recur(N))