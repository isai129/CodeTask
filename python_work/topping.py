# 5.4 使用 if 语句处理列表
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



