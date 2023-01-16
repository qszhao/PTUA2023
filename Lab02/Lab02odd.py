num = []
for i in range(2, 101):
    flag = 0
    for j in range(1, i+1):
        if i % j == 0:
            flag += 1
    if flag == 2:
        num.append(i)
print(num)