# 不可变的列表被称为元组,但使用圆括号来标识.
# 4.5.1 定义元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#  dimensions[0] = 250   TypeError: 'tuple' object does not support item assignment
# 严格地说，元组是由逗号标识的，圆括号只是让元组看起来更整洁、更清晰。
# 定义只包含一个元素的元组，必须在这个元素后面加上逗号.
mt_tuple = (2,)  # 创建只包含一个元素的元组通常没有意义，但自动生成的元组有可能只有一个元素。

# 4.5.2 遍历元组中的所有值
# 像列表一样，也可以使用 for 循环来遍历元组中的所有值:

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# 4.5.3 修改元组变量

# 虽然不能修改元组的元素，但可以给存储元组的变量赋值。

dimensions = (500, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)