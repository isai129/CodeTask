#  4.4.3 复制列表

# 同时省略起始索引和终止索引[:],这让 Python 创建一个始于第一个元素、终止于最后一个元素的切片，即整个列表的副本.

my_foods = ['pizza', 'hot dog', 'carrot cake']

# 这行不通：
# friend_foods = my_foods

# 切片
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

# 4-10
print(f"The first three my favourite foods are:{my_foods[:3]}")

print(f"Three items from the middle of the list are:{my_foods[3:4]}")

print(f"The last three my favourite foods are:{my_foods[2:]}")

for my_food in my_foods[:]:
    print(my_food.title())

numbers_list_1s = []
for value in range(1, 10, 2):
    numbers_list_1s.append(value)
print(numbers_list_1s)

numbers_list_2s = [value * 2 for value in range(1, 10, 2)]
print(numbers_list_2s)
