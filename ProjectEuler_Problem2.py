# 4백만 이하의 짝수 값을 갖는 모든 피보나치 항을 더하면 얼마가 될까?
fibo_list = [1, 2]
x = 0
num = 1

while fibo_list[num] < 3000000: # 이 부분이 약간 틀린 것 같음
    value = pibo_list[num-1] + fibo_list[num]
    num += 1
    fibo_list.append(value)

for y in fibo_list:
    if y % 2 == 0:
        x += y

print(x)
