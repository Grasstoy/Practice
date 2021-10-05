# 4백만 이하의 짝수 값을 갖는 모든 피보나치 항을 더하면 얼마가 될까?
pibo_list = [1, 2]
x = 0
num = 1

while pibo_list[num] < 4000000:
    value = pibo_list[num-1] + pibo_list[num]
    num += 1
    pibo_list.append(value)
    if pibo_list[num] > 4000000:
        pibo_list.pop()
        break

for y in pibo_list:
    if y % 2 == 0:
        x += y

print(x)
