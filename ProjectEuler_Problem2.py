# 4백만 이하의 짝수 값을 갖는 모든 피보나치 항을 더하면 얼마가 될까?
pibo_list = [1, 2]
x = 0
num = 1

while pibo_list[num] < 3000000: # 이 부분이 약간 틀린 것 같 
    value = pibo_list[num-1] + pibo_list[num]
    num += 1
    pibo_list.append(value)

for y in pibo_list:
    if y % 2 == 0:
        x += y

print(x)
