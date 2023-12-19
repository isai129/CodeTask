# 集合 类似于列表，但每个元素都必须是独一无二且不可变的：
# 可以使用`{}`或者set()函数创建集合
# 基本功能是进行成员关系测试和删除重复元素
# 它是无序的

# 基本操作

set1 = {1, 2, 3}
print(set1)
set2 = {1, 2, 3, [2, 3], {'name': 'xc'}}  # 列表是可变的（不可哈希），所以出错
print(set2)

# 1.集合——增

# add
set1 = {'alex', 'wueir', 'rain', 'egon', 'fid'}
set1.add('root')  # 因为集合是无序的，所以每次运行结果不一定一样，增加的位置也不一定一样
print(set1)

# update
set1.update('xc')  # 代添加，依然是无序的
print(set1)

# 2.集合——删

set1 = {'alex', 'wuer', 'del', 'rout', 'fwerr'}

# pop 随机删除
print(set1.pop())  # 有返回值，返回本次删除的内容
print(set1)

# remove——指定元素删除
set1.remove('del')
print(set1)

# clear——清空
set1.clear()
print(set1)  # 空集合：set()

# del
del set1
print(set1)  # 删除之后集合不存在，报错

# 3.集合不能改
# 集合是无序；
# 集合中的元素是不可变数据类型

# 4.集合—查
set1 = {'alex', 'fod', 'scad', 'cvb', 'csd'}
for i in set1:
    print(i)

# 5.集合之间的操作
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# 交集
print(set1 & set2)
print(set1.intersection(set2))
# 并集
print(set1 | set2)
print(set1.union(set2))
# 反交集(除交集以外的其他元素
print(set1 ^ set2)
print(set1.symmetric_difference(set2))
# 差集（前者独有的）
print(set1 - set2)
print(set1.difference(set2))
print(set2 - set1)
print(set2.difference(set1))

# 子集与超集
set3 = {1, 2, 3, 4, 5}
set4 = {1, 2, 3, 4, 5, 6, 7, 8}
print('------set3是set4的子集-----')
print(set3 < set4)
print(set3.issubset(set4))
print('-----set4是set3的超集-----')
print(set4 > set3)
print(set4.issuperset(set3))
