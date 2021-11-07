# if 4의 배수
#     if 100의 배수
#         if 400의 배수 -> 1
#         else -> 0
#     else -> 1  => 4의 배수인 다른 수
# else -> 0  => 4의 배수가 아닌 수


year = int(input())

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("1")
        else:
            print("0")
    else: 
        print("1")
else:
    print("0")