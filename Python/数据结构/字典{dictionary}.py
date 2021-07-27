# 字典是一种映射类型，字典用` { }` 标识，它是一个无序的键(key) : 值(value) 的集合
# 标记方式：d = {key1 : value1, key2 : value2 }
# dict
#   key（键）必须是不可变数据类型，可哈希
#   value（值）任意数据类型
#   优点：二分查找去查询
#   存储大量的关系型数据
#   特点：<=3.5版本无序，3.6以后都是有序

#   1.字典— 增

# dict['键'] = 值

dict1 = {'age': 18, 'name': 'xc', 'sex': 'female'}
dict1['height'] = 165
print(dict1)
dict1['age'] = 21
print(dict1)

#   2.字典— 删
#   删除优先使用pop(有返回值，要删除的内容不存在时不报错)，而不是del
#   pop删除

dict2 = {'age': 18, 'name': 'xc', 'sex': 'female'}
print(dict2.pop('age'))  # 有age直接删除---有返回值，按键删除
print(dict2)
print(dict2.pop('erge', '没有此键,None'))  # 没有erge----可设置返回值：没有此键/None
print(dict2)

#   popitem 随机删除

dict2 = {'age': 18, 'name': 'cx', 'sex': 'female'}
print(dict2.popitem())

#   clear清空
dict2 = {'age': 18, 'name': 'xc', 'sex': 'female'}
dict2.clear()  # 清空字典
print(dict2)

#   del删除
dict2 = {'age': 18, 'name': 'xc', 'sex': 'female'}
del dict2['name']  # 有则删除
print(dict2)
del dict2['sex2']  # 没有报错

#   3.字典——改
#   update
dict3 = {'age': 18, 'name': 'xc', 'sex': 'female'}
dict4 = {'name': 'alex', 'weigh': 172}
dict4.update(dict3)  # 有则更新覆盖，没有则增加
print(dict3)
print(dict4)

#   4.字典——查
#   keys,values,items

dict5 = {'age': 18, 'name': 'xc', 'sex': 'female'}
print(dict5.keys(), type(dict5.keys()))
print(dict5.values())
print(dict5.items())

#  得到键值，首选get
print(dict5['name'])  # 有则打印
print(dict5['name1'])  # 无则报错
print(dict5.get('name1', '没有此键'))  # 没有name1----可设置返回值：没有此键/None

#   循环输出

for i in dict5:
    print(i)  # 循环打印键（默认为键）

for i in dict5.keys():  # 循环打印键
    print(i)

for i in dict5.values():
    print(i)  # 循环打印值

for i in dict5.items():
    print(i)  # 循环打印键值对

for k, v in dict5.items():
    print(k, v)  # 打印键和值

#   字典的嵌套

dic = {'name': ['alex', 'route', 'root', 'administrator', 'mstsc'],
       'py9': {'time': '12312', 'study_fee': '19800', 'addr': 'cbd'},
       'age': 21}
dic['age'] = 16
print(dic)  # 找到age，再更新为16

dic['name'].append('rt')  # 找到name，在添加名字
print(dic)

dic['name'][1] = dic['name'][1].upper()  # 找到name，再把route变为大写
print(dic)

dic['py9']['female'] = 6  # 找到元祖，增加键值对female:6
print(dic)


# 应用实例：
# 输入一串字符，遇到字母，转换为‘_’,并打印输出

info = input('请输入：')
for i in info:
    if i.isalpha():
        info = info.replace(i, '_')
print(info)
