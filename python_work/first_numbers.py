# 4.3 数值列表,函数 range() 能够轻松地生成一系列数

for value in range(1, 5):
    print(value)

# 可使用函数 list()将 range()的结果直接转换为列表,也可只指定一个参数，这样它将从 0 开始
numbers = list(range(6))  # 也可只指定一个参数，这样它将从 0 开始
print(numbers)

# 可指定步长。为此，可给这个函数指定第三个参数.
even_number = list(range(2, 11, 2))  # 函数 range()从 2 开始数，然后不断加 2，直到达到或超过终值（11）
print(even_number)

# 函数 range()几乎能够创建任何需要的数集

squares = []  # 创建一个名为 squares 的空列表
for value in range(1, 11):  # 使用函数 range()让 Python 遍历 1～10 的值
    # square = value ** 2  # 计算当前值的平方,，并将结果赋给变量 square
    # squares.append(square)  # 将新计算得到的平方值附加到列表 squares 末尾
    # 为了让代码更简洁，可不使用临时变量 square ，而直接将每个计算得到的值附加到列表末尾:
    squares.append(value ** 2)
print(squares)  # 循环结束后，打印列表 squares

# 简单的统计计算:

digits = []
for value in range(0, 111, 3):
    digits.append(value)
    print(digits)
    print(min(digits))  # 最小值
    print(max(digits))  # 最大值
    print(sum(digits))  # 总和

# 4.3.4 列表解析

squares = [value ** 2 for value in range(1, 111)]  # 将for 循环和创建新元素的代码合并成一行

# 指定一个左方括号,并定义一个表达式，用于生成要存储到列表中的值.
# 表达式为 value**2，它计算平方值。接下来，编写一个 for 循环，用于给表达式提供值，再加上右方括号

print(squares)

# 4-3

number_list_4_3 = []
for value in range(1, 21):
    number_list_4_3.append(value)
print(number_list_4_3)

# 4-4 创建一个包含数 1～1 000 000 的列表，再使用一个 for 循环将这些数打印出来。
number_list_4_4 = []
for value in range(1, 1000001):
    number_list_4_4.append(value)
print(number_list_4_4)

number_list_4_4_1 = [value for value in range(1, 1000001)]
print(number_list_4_4_1)
# 4-5
print(min(number_list_4_4_1))
print(max(number_list_4_4_1))
print(sum(number_list_4_4_1))

# 4-6 包含1～20 的奇数列表
number_list_4_6 = []
for value in range(1, 21, 2):
    number_list_4_6.append(value)
print(number_list_4_6)

# 4-7 包含 3～30 能被 3 整除的数
number_list_4_7 = []
for value in range(3, 31, 3):
    number_list_4_7.append(value)
print(number_list_4_7)

# 4-8 包含前 10 个整数（1～10）的立方
number_list_4_8 = [value ** 3 for value in range(1, 11)]
print(number_list_4_8)
