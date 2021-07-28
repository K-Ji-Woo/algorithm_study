'''
입력은 여러 개의 테스트 케이스로 이루어져 있다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
'''

result_list = []


while True:
    try:
        A, B = input().split()
        A = int(A)
        B = int(B)

        result = A + B

        result_list.append(result)

    except :
        break



for i in range(len(result_list)):
    print(result_list[i])