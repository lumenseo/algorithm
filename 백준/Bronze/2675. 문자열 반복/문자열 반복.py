T=int(input())

for tc in range(T):

    R, string= input().split()
    R=int(R)
    
    P=""

    for char in string:
        P+=char*R

    print(P)
