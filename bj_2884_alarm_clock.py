# from typing import MutableMapping


# H M

# if M - 45 < 0 :
#     M = 60 - (45 - M)
#     if H > 0 :
#         H = H -1 
#     elif H == 0 :
#         H = 23
# elif M -45 > 0:
#     H
#     M = M - 45
# print(H, M)


H, M = input().split()
H = int(H)
M = int(M)


if M - 45 < 0 : # 시가 1만큼 줄어들어야 할 때
    M = 15 + M # 60 - (45 - M)
    if H > 0 :
        H -= 1
    elif H == 0 :
        H = 23
elif M - 45 >= 0 : # 시가 줄어들 필요 없을 때
    M -= 45

print(H, M)


