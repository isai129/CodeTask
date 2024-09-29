# if语句

# 5.1
cars = ['audi', 'bmw', 'subaru', 'toyota']  # 一个汽车列表，并想将其中每辆汽车的名称打印出来
# 对于大多数汽车，应以首字母大写的方式打印其名称，但对于汽车名'bmw'，应以全大写的方式打印
for car in cars:
    if car == 'bmw':  # 首先检查当前的汽车名是否是'bmw'
        print(car.upper())  # '=='运算符在两边的值相等时返回True，就以全大写方式打印,
    else:
        print(car.title())  # 否则返回 False,就以首字母大写的方式打印

# 5.2 条件测试
# 每条 if 语句的核心都是一个值为 True 或 False 的表达式，这种表达式称为条件测试,。Python
# 根据条件测试的值为 True 还是 False 来决定是否执行 if 语句中的代码。

# 5.21 检查是否相等
# 使用两个等号（==）检查 car 的值是否为'bmw'。这个相等运算符在两边的值相等时返回True，否则返回 False。

car = 'bmw'
car == 'bmw'

# 5.2.2 检查是否相等时忽略大小写

car = 'Audi'
car.lower() == 'audi'

# 5.2.3 检查是否不相等(!=)

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# 5.2.4 数值比较

age = 18
age == 18

# True

# 5.2.5 检查多个条件
## 1. 使用 and 检查多个条件(至少一个测试没有通过，整个表达式就为 False)
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
# False
## 2.使用 or 检查多个条件(只要至少一个条件满足，就能通过整个测试。)

age_0 >= 21 or age_1 >= 21
# True

# 5.2.6 检查特定值是否包含在列表中 (in)

requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
'pepperonl' in requested_toppings

# 5.2.7 检查特定值是否不包含在列表中 (not in )

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# 5.2.8 布尔表达式(术语)(条件测试),通常用于记录条件
# 在跟踪程序状态或程序中重要的条件方面，布尔值提供了一种高效的方式。


