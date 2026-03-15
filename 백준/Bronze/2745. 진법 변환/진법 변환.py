#import sys
#sys.stdin=open('input.txt', 'r')

N, B = input().split()

B=int(B)
N_reversed=N[::-1]

chars="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dec_result=0

for i, digit in enumerate(N_reversed):
    real_value=chars.index(digit)
    dec_result += real_value*(B**i)

print(dec_result)