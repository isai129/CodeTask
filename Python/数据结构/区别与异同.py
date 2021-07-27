# 列表（list)
# 特点：
# 1.可以用list()函数或者方括号[]创建，元素之间用","分隔
list1 = list((1, 2))
# 2.列表的元素不需要具有相同的类型
list2 = [1, 3, 'red', 4.5]
# 3.使用索引来访问元素
print(list1[1])
# 4.可切片
print(list2[1:3])

# 方法：
# 增加
list1.append('tess')
print(list1)
# 计算列表中参数x出现的次数
x = list1.count('tess')
print(x)
# 向列表中追加另一个列表L
list1.extend(list2)
print(list1)
# 获得参数在列表中的位置
t = list1.index(3)
print(t)
# 先列表中插入数据
list2.insert(3, 'ree')
print(list2)
# 删除列表中的成（通过下标删除）
list2.pop(3)
print(list2)
# 删除列表中的成员
list1.remove('tess')
print(list1)
# 将列表中的成员顺序颠倒
list1.reverse()
print(list1)
# 将列表中的成员排序
list1.clear()
list3 = [1, 4, 2, 0, 5, 8]
list1.extend(list3)
print(list3.sort())
