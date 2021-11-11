'''
T 받기

for i in T:
    A, B 받기
    print(A + B)
'''

import sys

T = int(input())

for i in range(T):
    A, B = sys.stdin.readline().split()
    A = int(A)
    B = int(B)
    print(A+B)