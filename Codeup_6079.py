'''
1, 2, 3 ... 을 계속 더해 나갈 때,
그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
계속 더하는 프로그램을 작성해보자.

'''
# 0 <= n <= 1000
n = int(input())

for m in range(0, n):
    if (m-1)* m < 2*n <= m * (m+1):
        print(m)