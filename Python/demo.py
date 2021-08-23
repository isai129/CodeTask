print('hello,python!')

flag = True
if flag:
    print('flag条件为Ture')
# 注释

# 单引号
'''
注释1
注释2
注释3
'''
# 双引号

"""
注释1
注释2
注释3
"""

# 算数运算符

a = 10
b = 21
c = 0
print(a + b)
print(a - b)
print(a * b)
print(b / a)
print(b % a)
print(a ** b)
print(b // a)

c = a + b
print("1.c的值为：", c)
c = a - b
print("2.c的值为：", c)
c = a * b
print("3.c的值为：", c)
c = a / b
print("4.c的值为:", c)
c = a % b
print("5.c的值为:", c)

# 修改变量a,b,c
a = 2
b = 3
c = a ** b
print("6.c的值为:", c)
a = 10
b = 5
c = a // b
print("7.c的值为:", c)

# 比较运算符

a = 21
b = 10
c = 0

if a == b:
    print("1.a等于b")
else:
    print("1.a不等于b")

if a != b:
    print("2.a不等于b")
else:
    print("2.a等于b")

if a < b:
    print("3.a小于b")
else:
    print("3.a大于等于b")

if a > b:
    print("4.a大于b")
else:
    print("4.a小于等于b")

# 修改变量a和b的值
a = 5
b = 20
if a <= b:
    print("5.a小于等于b")
else:
    print("5.a大于b")

if b >= a:
    print("6.b大于等于a")
else:
    print("6.b小于a")

# 赋值运算符

a = 21
b = 10
c = 0

# = 简单赋值运算符
c = a + b  # 将 a + b 的运算结果赋值为 c
print("1.c的值为:", c)
# 加法赋值运算符
c += a  # 等效于 c = c + a
print("1.c的值为:", c)
# 减法赋值运算符
c -= a  # 等效于 c = c - a
print("2.c的值为：", c)
# 乘法赋值运算符
c *= a  # 等效于 c = c * a
print("3.c的值为：", c)
# 除法赋值运算符
c /= a  # 等效与 c= c/a
print('4.c的值为:', c)
# 取模赋值运算符
c %= a  # 等效于 c= c % a
print("5.c的值为:", c)
# 幂赋值运算符
c **= a  # 等效于 c = c ** a
print("6.c的值为:", c)
# 取整除赋值运算符
c //= a  # 等效于c = c // a
print("c的值为:", c)

# 海象运算符(可在表达式内部为变量赋值[python.8新增])
# 以下示例中,赋值表达式可以避免调用len()两次
a = 10
b = 20
if (n := len(a)) > 10:
    print(f"list is too long {n} elements,expected <= 10)")


# 位运算符

a = 60  #
b = 13
c = 0
print(a & b)


