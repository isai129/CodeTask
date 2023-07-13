 
# 1. 起步

## 1.12运行 Python 代码片段

```bash
print("Hello Python World!")
```

# 2. 变量和简单数据类型

## 2.22  变量名命名规则:

	1.变量名只能包含字母、数字和下划线,
	2.能以字母或下划线打头，但不能以数字打头
	3.变量名不能包含空格
	4.不要将 Python 关键字和函数名用作变量名
	5.变量名应既简短又具有描述性
	6.慎用小写字母 l 和大写字母 O，因为它们可能被人错看成数字 1 和 0。
	7.应使用小写的 Python 变量名
		`Python没有内置的常量类型,通常使用小写字母和下划线表示变量,全大写来表示常量
		变量是可以赋给值的标签，也可以说变量指向特定的值。

## 2.2.3 变量是标签


## 2.3  字符串

```bash
name = 'irene'
print(f"首字母大写\t{name.title()}") # 首字母大写
print(f"全部大写\t{name.upper()}")  # 全部大写
print(f"全部小写\t{name.lower()}")  # 全部小写
print(f"清除前面空格\n'{name.lstrip()}'") # 清除前面空格
print(f"清除后面空格\n'{name.rstrip()}'") # 清除后面空格
print(f"清除前后空格\n'{name.strip()}'")  # 清除前后空格
# f字符串,f 是 format（设置格式）的简写，通过把花括号内的变量替换为其值来设置字符串的格式
#将消息 
message = f"\tHello {name.strip()},\n\tlet`s go to see move!"
print(message)
#在编程中，空白泛指任何非打印字符，如空格、制表符和换行符。你可以使用空白来组织输
#出，让用户阅读起来更容易。
# /n:换行符; /t:制表符
print("Languages:\n\tPython\n\tC\n\tJavaScript")

```

## 2.4数

```bash
# 2.4.3 数值列表,函数 range() 能够轻松地生成一系列数  
  
for value in range(1, 5):  
print(value)  
  
# 可使用函数 list()将 range()的结果直接转换为列表,也可只指定一个参数，这样它将从 0 开始  
numbers = list(range(6)) # 也可只指定一个参数，这样它将从 0 开始  
print(numbers)  
  
# 可指定步长。为此，可给这个函数指定第三个参数.  
even_number = list(range(2, 11, 2)) # 函数 range()从 2 开始数，然后不断加 2，直到达到或超过终值（11）  
print(even_number)  
  
# 函数 range()几乎能够创建任何需要的数集  
  
squares = [] # 创建一个名为 squares 的空列表  
for value in range(1, 11): # 使用函数 range()让 Python 遍历 1～10 的值  
# square = value ** 2 # 计算当前值的平方,，并将结果赋给变量 square# squares.append(square) # 将新计算得到的平方值附加到列表 squares 末尾  
# 为了让代码更简洁，可不使用临时变量 square ，而直接将每个计算得到的值附加到列表末尾:  
squares.append(value ** 2)  
print(squares) # 循环结束后，打印列表 squares  
# 简单的统计计算:  
  
digits = []  
for value in range(0, 111, 3):  
digits.append(value)  
print(digits)  
print(min(digits)) # 最小值  
print(max(digits)) # 最大值  
print(sum(digits)) # 总和  
  


```




# 3.组织列表

```bash
avengers = ['iron man','captain america','hulk','thor','black widow','hawkeye']

print(f"1.{avengers[0]}")
print(f"2.{avengers[1]}")
print(f"3.{avengers[2]}")
print(f"4.{avengers[3]}")
print(f"5.{avengers[4]}")
print(f"6.{avengers[-1]}"

# 大多数列表将是动态的，这意味着列表创建后，将随着程序的运行增删元素

avengers[5] = 'jarvis'
print(avengers)

# insert()可在列表的任何位置添加新元素

avengers.insert(0,'nick fury')
print(avengers)

# 使用 del 语句删除元素，条件是知道其索引

del avengers[0]
print(avengers)

# 使用方法 pop()删除末尾的元素,让你能够接着使用它。
# 术语弹出（pop）源自这样的类比：列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素。

poped_avengers = avengers.pop()  # 从avengers中弹出'vision'并赋值给变量poped_avengers.
print(avengers)
print(poped_avengers)

# 弹出列表中任何位置处的元素,只需在圆括号中指定要删除元素的索引

first_avengers = avengers.pop(0)
print(f"the first avengers is :{first_avengers.title()}")

# 如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用 del 语句；
# 如果你要在删除元素后还能继续使用它，就使用方法 pop()。
# 如果只知道要删除的元素的值，可使用方法 remove()

print(avengers)
avengers.remove('hawkeys')
print(avengers)

to_old = 'thor'
avengers.remove(to_old)
print(f"\n{to_old.title()} is too old.")

# 方法 remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来确保将每个值都删除。
print(avengers)

# 使用方法 sort()对列表永久排序(按与字母顺序正向)  
  
cars = ['toyota', 'suvaru', 'bmw', 'audi']  
cars.sort()  
print(cars)  
  
# 按与字母顺序相反的顺序排列,只需向 sort()方法传递参数:reverse=True  
  
cars.sort(reverse=True)  
print(cars)  
  
# 使用函数 sorted()对列表临时排序  
  
cars = ['toyota', 'suvaru', 'bmw', 'audi']  
print(sorted(cars))  
  
# reverse参数 -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。

# 要反转列表元素的排列顺序，可使用方法 reverse()  
cars.reverse()  
print(cars)  
  
# 使用函数 len()可快速获悉列表的长度  
  
len(cars)  
print(len(cars))


```


# 4.操作列表

### 4.1 遍历整个列表  

```bash
# for循环  
magicians = ['alice', 'david', 'carolina']  
for magician in magicians:  
print(magician)  
# 使用单数和复数式名称，可帮助你判断代码段处理的是单个列表元素还是整个列表  
print(f'{magician.title()}, that was a great trick!')

# Python 函数 range()让你能够轻松地生成一系列数

for value in range(1, 5):  
print(value)  
  
# 可使用函数 list()将 range()的结果直接转换为列表,也可只指定一个参数，这样它将从 0 开始  
numbers = list(range(6)) # 也可只指定一个参数，这样它将从 0 开始  
print(numbers)  
  
# 可指定步长。为此，可给这个函数指定第三个参数.  
even_number = list(range(2, 11, 2)) # 函数 range()从 2 开始数，然后不断加 2，直到达到或超过终值（11）  
print(even_number)  
  
# 函数 range()几乎能够创建任何需要的数集

squares = [] # 创建一个名为 squares 的空列表  
for value in range(1, 11): # 使用函数 range()让 Python 遍历 1～10 的值  
# square = value ** 2 # 计算当前值的平方,，并将结果赋给变量 square# squares.append(square) # 将新计算得到的平方值附加到列表 squares 末尾  
# 为了让代码更简洁，可不使用临时变量 square ，而直接将每个计算得到的值附加到列表末尾:  
squares.append(value ** 2)  
print(squares) # 循环结束后，打印列表 squares



# 简单的统计计算:  

digits = []  
for value in range(0, 111, 3):  
digits.append(value)  
print(digits)  
print(min(digits)) # 最小值  
print(max(digits)) # 最大值  
print(sum(digits)) # 总和  


# 4.3.4 列表解析  
  
squares = [value ** 2 for value in range(1, 111)] # 将for 循环和创建新元素的代码合并成一行  
  
# 指定一个左方括号,并定义一个表达式，用于生成要存储到列表中的值.  
# 表达式为 value**2，它计算平方值。接下来，编写一个 for 循环，用于给表达式提供值，再加上右方括号  


print(squares)

avengers = ['iron man', 'captain america', 'hulk', 'thor', 'black widow', 'Hawkeye']  
# 打印该列表的一个切片,  
print(avengers[:3]) # 输出包含前三名队员  
print(avengers[2:])  
print(avengers[-2:]) #  
print(avengers[1:4]) # 1-3  

# 遍历切片,for 循环  
players = ['charles', 'martina', 'michael', 'florence', 'eli']  
print("Here are the first three players on my team: ")  
for player in players[:3]:  
print(player)

# 4.4.3 复制列表  
 
my_foods = ['pizza', 'hot dog', 'carrot cake']  
  
# 这行不通：  
# friend_foods = my_foods  
  
# 切片  
# 同时省略起始索引和终止索引[:],这让 Python 创建一个始于第一个元素、终止于最后一个元素的切片，即整个列表的副本. 

friend_foods = my_foods[:]  
  
print("my favourite foods are:")  
print(my_foods)  
print("\nMy friend`s favourite foods are:")  
print(friend_foods)

my_foods.extend(['cake', 'cannnoli'])  
friend_foods.append('ice cream')  
print("my favourite foods are:")  
print(my_foods)  
print("\nmy friend favourite foods are :")  
print(friend_foods)

print(f"The first three my favourite foods are:{my_foods[:3]}")  
  
print(f"Three items from the middle of the list are:{my_foods[3:4]}")  
  
print(f"The last three my favourite foods are:{my_foods[2:]}")


```


# 5.if语句

## 5.1 示例

```bash
 
cars = ['audi', 'bmw', 'subaru', 'toyota'] # 一个汽车列表，并想将其中每辆汽车的名称打印出来  
# 对于大多数汽车，应以首字母大写的方式打印其名称，但对于汽车名'bmw'，应以全大写的方式打印  
for car in cars:  
if car == 'bmw': # 首先检查当前的汽车名是否是'bmw'  
print(car.upper()) # '=='运算符在两边的值相等时返回True，就以全大写方式打印,  
else:  
print(car.title()) # 否则返回 False,就以首字母大写的方式打印  
  
  


```


## 5.2 条件测试  

```bash

# 每条 if 语句的核心都是一个值为 True 或 False 的表达式，这种表达式称为条件测试,。Python  
# 根据条件测试的值为 True 还是 False 来决定是否执行 if 语句中的代码。  
  
# 5.21 检查是否相等
>>> car = 'bmw'
>>> car == 'bmw'
>>> True

# 5.23 检查是否相等时忽略大小写
>>> car = 'Audi'
>>> car =='audi'
>>> False
>>> car.lower() == 'audi'
>>> True

# 5.2.3 检查是否不相等
# 要判断两个值是否不等，可结合使用惊叹号和等号（!=），其中的惊叹号表示不
requested_topping = 'mushrooms'  
if requested_topping != 'anchovies':  
print('Hold the anchovies')

# 5.2.4 数值比较
>>>age = 18
>>>age == 18
>>>True
# 检查两个数是否不等
answer = 17
if answer != 42:
print('That is not correct answer. Please try again!')

# 5.25 检查多个条件
# 1. 使用 and 检查多个条件
# 要检查是否两个条件都为 True，可使用关键字 and 将两个条件测试合而为一
>>>age = 23
>>>age_1 = 18
>>>age_0 >= 21 and age_1 >= 21
>>>False
>>>age_1 = 22
>>>(age_0 >= 21) and (age_1 >= 21)  # 可将每个测试分别放在一对圆括号内,改善可读性
>>>True

# 2. 使用 or 检查多个条件
# 关键字 or 也能够让你检查多个条件，但只要至少一个条件满足，就能通过整个测试
>>>age_0 = 22
>>>age_1 = 18
>>>age_0 >= 21 or age_1 >=21
>>>True
>>>age_0 = 18
>>>age_0 >= 21 or age age_1 >= 18
>>>False

# 5.2.6 检查特定值是否包含在列表中

requested_toppings = ['mushrooms', 'onions', 'pineapple']  
'mushrooms' in requested_toppings


# 5.2.7 检查特定值是否不包含在列表中 (not in )  
banned_users = ['andrew', 'carolina', 'david']  
user = 'marie'  
if user not in banned_users:  
print(f"{user.title()}, you can post a response if you wish.")

# 5.2.8 布尔表达式(术语)(条件测试),通常用于记录条件  
# 在跟踪程序状态或程序中重要的条件方面，布尔值提供了一种高效的方式。




```

## 5.3 if 语句  

```bash


# 5.3.1 简单的 if 语句  
  
age = 19  
if age >= 18:  
print("you are old enough to vote!")  
print("Have you registered to vote yet?")  
  
# 5.3.2 if-else 语句  
# 5.3.3 if-elif-else 结构  
  
age_1 = 13  
if age_1 < 4:  
print("Your admission cost is $0.")  
elif age_1 < 18:  
print("Your admission cost is $25.")  
else:  
print("Your admission cost is $40.")  
  
age_2 = 21  
if age_2 < 4:  
price = 0  
elif age_2 < 18:  
price = 25  
else:  
price = 40  
print(f"Your admission cost is ${price}.")  
  
# 5.3.4 使用多个 elif 代码块  
age_3 = 40  
prices = 100  
if age_3 < 4:  
price = prices * 0  
elif age_3 < 18:  
price = prices * 0.25  
elif age_3 < 55:  
price = prices * 1  
elif age_3 < 55:  
price = prices * 0.5  
else:  
price = prices * 0.2  
print(f"Your admission cost is ${price}.")  
# else 是一条包罗万象的语句，只要不满足任何 if 或 elif 中的条件测试，其中的代码就会执  
# 行。这可能引入无效甚至恶意的数据。如果知道最终要测试的条件，应考虑使用一个 elif 代码  
# 块来代替 else 代码块。  
  
  
# 5.3.6 测试多个条件  
chose = []  
chose_1 = 2  
chose_2 = 3  
chose_3 = 5  
chose_4 = 6  
chose_5 = 7  
menu = [value for value in range(1, 10, 2)]  
if chose_1 in menu:  
chose.insert(0, f"a.{chose_1}")  
if chose_2 in menu:  
chose.insert(1, f"b.{chose_2}")  
if chose_3 in menu:  
chose.insert(2, f"c.{chose_3}")  
if chose_4 in menu:  
chose.insert(3, f"d.{chose_4}")  
if chose_5 in menu:  
chose.insert(4, f"e.{chose_5}")  
print(menu)  
print(chose)  
for cho in chose:  
print(cho.title())  
  
# 练习 5-3: 外星人颜色  
alien_color = 'Green'  
if alien_color.lower() == 'green':  
print("Your are great!")  
  
alien_color_1 = "GReen"  
score = 100  
if alien_color_1.lower() == 'green':  
print(f"Your score are {score * 0.05}")  
elif alien_color_1.lower() == 'yellow':  
print(f"Your score are {score * 0.1}")  
else:  
print(f"Your score are {score * 0}")  
  
  
alex_age = 16  
if alex_age < 2:  
status = 'baby'  
elif alex_age < 4:  
status = 'toddler'  
elif alex_age < 13:  
status = 'kid'  
elif alex_age < 20:  
status = 'teenager'  
elif alex_age < 65:  
status = 'adult'  
else:  
status = 'elder'  
print(f"Your are {status}!")  
  
  
favourite_fruits = ['apple', 'bananas', 'orange', 'watermelon']  
if 'apple' in favourite_fruits:  
print("you really like apple!")  
if 'bananas' in favourite_fruits:  
print('you relly like bananas!')  
if 'orange' in favourite_fruits:  
print('you relly liake orange!')  
if 'watermelon' in favourite_fruits:  
print('you relly like orange!')  
for fruits in favourite_fruits:  
print (fruits.title())

```


## 5.4 使用 if 语句处理列表  

```bash

# #5.41 检查特殊元素  
  
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']  
for requested_topping in requested_toppings:  
if requested_topping == 'green peppers':  
print(f"Sorry,we are out of green peppers right now!")  
else:  
print(f"Adding {requested_topping}.")  
print("\nFinished making tour pizza!")  
  
# 5.4.2 确定列表不是空的  
  
requested_toppings = []  
if requested_toppings:  
# 在 if 语句中将列表名用作条件表达式时，Python 将在列表至少包含一个元素时返回 True，并在列表为空时返回 False。  
for requested_topping in requested_toppings:  
print(f"Adding {requested_topping}.")  
print("\n Finshed making your pizza! ")  
else:  
print("Are you sure you want a plain pizza?")  
  
# 5.43 使用多个列表  
  
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']  
requested_toppings = ['mushrooms', 'pineapple', 'extra cheese']  
for requested_topping in requested_toppings:  
if requested_topping in available_toppings:  
print(f"Adding {requested_topping}")  
else:  
print(f"Sorry,we don`t have {requested_topping}.")  
print("\nFinished making your pizza!")
```




