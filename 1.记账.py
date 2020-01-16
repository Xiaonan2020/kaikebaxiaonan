print("一周记账")
print("-"*40)
income = []
expend = []
jieyu = {}
for i in range(0, 7):
    income.append(int(input(f"第{i+1}天收入:")))

print("-"*40)
for i in range(0, 7):
    expend.append(int(input(f"第{i+1}天一支出:")))
for i in range(0, 7):
    jieyu[i] = income[i] - expend[i]

sum = 0
for i in range(0, 7):
    sum += jieyu[i]

print("-"*40)
print("".ljust(10) + "收入".ljust(10) + "支出".ljust(10) + "结余".ljust(10))
print("-"*40)
for i in range(0, 7):
    print(f"第{i+1}天".ljust(5),income[i],"".ljust(10),expend[i],"".ljust(10),jieyu[i],"".ljust(10))
print("-"*40)
print(f"总结余:{sum}")