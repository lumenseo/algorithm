T = int(input())
for i in range(T):
    a = input()
    K = int(input())
    b = {}
    c = len(a)
    minn = c +1

    maxx = -1
    for i in a:
        if i not in b:
            
            number = []
            b[i] = number
            for j in range(c):
                if a[j] == i:
                    b[i].append(j)
            for x in range(len(number)-K+1):
                target = number[x+K-1] - number[x] +1
                if target < minn:
                    minn = target
                if target > maxx:
                    maxx = target
    if maxx == -1:
        print(maxx)
    else:
        print(minn, maxx)