# 列表,由一系列按特定顺序排列的元素组成,可以将任何东西加入列表中，其中的元素之间可以没有任何关系。
# 列表通常包含多个元素，因此给列表指定一个表示复数的名称.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print([bicycles])

# 列表是有序集合，因此要访问列表的任意元素，只需将该元素的位置（索引）告诉 Python即可。

print(bicycles[0])

# .title()让首字母大写
print(bicycles[1].title())

# Python 为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为-1，可让 Python返回最后一个列表元素：

print(f"最后一个元素:\t{bicycles[-1].title()}")
print(f"倒数第二个元素:\t{bicycles[-2].strip()}")

message = f"my first bicycle was {bicycles[2]}"
print(message.upper())

avengers = ['iron man', 'captain america', 'hulk', 'thor', 'black widow', 'hawkeye']

print(f"1.{avengers[0]}")
print(f"2.{avengers[1]}")
print(f"3.{avengers[2]}")
print(f"4.{avengers[3]}")
print(f"5.{avengers[4]}")
print(f"6.{avengers[-1]}")

# 大多数列表将是动态的，这意味着列表创建后，将随着程序的运行增删元素

avengers[5] = 'jarvis'
print(avengers)

# append()方法将元素添加到列表末尾
avengers[5] = 'hawkeys'
avengers.append('vision')
print(avengers)

# insert()可在列表的任何位置添加新元素

avengers.insert(0, 'nick fury')
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

# 
to_old = 'thor'
avengers.remove(to_old)
print(f"\n{to_old.title()} is too old.")

# 方法 remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来确保将每个值都删除。


print(avengers)

avengers.insert(0, 'iron man')
print(avengers)
avengers.insert(2, 'thor')
print(avengers)
avengers.append('hawkeys')
print(avengers)

message = f"Hello,{avengers[0].title()}"
print(message)

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

print(sorted(cars, reverse=True))
print(cars)

#  倒着打印列表

# 要反转列表元素的排列顺序，可使用方法 reverse()

cars.reverse()
print(cars)

# 使用函数 len()可快速获悉列表的长度

len(cars)
print(len(cars))

my_list = ['taiwan', 'hongkong', 'jp', 'tokyo', 'vegas']
print(my_list)
print(sorted(my_list))
print(my_list)
print(sorted(my_list, reverse=True))
print(my_list)
my_list.reverse()
print((my_list))
my_list.reverse()
print(my_list)
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
print(len(my_list))
print(my_list[0])
print(my_list[-1])



