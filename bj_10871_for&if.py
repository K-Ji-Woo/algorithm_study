# 1. 정수 N개로 이루어진 수열 A를 입력받음
# 2. A에서 X보다 작은 수 출력

N, X = input().split()
A = input().split()

N = int(N)
X = int(X)

# c 원소 데이터 타입 변경
for i in range(N):
    A[i] = int(A[i])

# # 과제 수행
for j in range(N):
    if A[j] < X:
        print(A[j], end=' ')

