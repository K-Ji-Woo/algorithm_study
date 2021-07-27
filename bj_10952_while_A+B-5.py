'''
입력은 여러 개의 테스트 케이스로 이루어져 있다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

입력의 마지막에는 0 두 개가 들어온다.

'''


result_list = []

# 문제 수행
while True:
    A, B = input().split()
    A = int(A)
    B = int(B)
    
    if A + B == 0:
        break
    else:
        calculated = A + B
        result_list.append(calculated)


# 결과 출력
for i in range(len(result_list)):
    print(result_list[i])
