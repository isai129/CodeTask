# 5.3 if 语句
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