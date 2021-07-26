# 一旦你创建了一个列表，你可以添加、删除或是搜索列表中的项目

# 基本操作
# 购物清单

shoplist = ['苹果', '芒果', '胡萝卜', '香蕉']
print('我有', len(shoplist), '个商品在我的购物清单.')
print('它们是：'),  # 提示
for item in shoplist:
    print(item)
print('我还买了大米.')
shoplist.append('大米')
print('现在我的购物清单是：', shoplist)

# 基本操作——增加
# append 追加
# %%
li = ['苹果', '芒果', '胡萝卜', '香蕉']
li.append('大米')
print(li)
li.append(1)
print(li.append('hello'))  # None：无返回值，li.append()只是一个方法、动作
print(li)

# insert 插入

li = ['苹果', '芒果', '胡萝卜', '香蕉']
li.insert(3, '草莓')
print(li)

# extend 追加到末尾

li = ['苹果', '芒果', '胡萝卜', '香蕉']
li.extend('cc')
print(li)
li.extend([1, 2, 3])
print(li)
#  li.extend(123)
print(li)

# 应用实例：
# 连续输入员工姓名，输入Q/q退出并打印列表
li = []
while True:
    username = input("请输入要添加的员工姓名：")
    if username.strip().upper() == 'Q':
        break
    li.append(username)
    print(li)
print(li)

# 列表——删

# remove:按照元素删除
li = ['苹果', '芒果', '胡萝卜', '香蕉']
li.remove('芒果')
print(li)

# pop : 按照索引删除--有返回值
li = ['苹果', '芒果', '胡萝卜', '香蕉']
name = li.pop(1)
print(name, li)

name = li.pop()  # 不写索引则默认删除最后一个
print(name, li)

# clear : 清空

li = ['苹果', '芒果', '胡萝卜', '香蕉']
li.clear()
print(li)

# del :删除
li = ['苹果', '芒果', '胡萝卜', '香蕉']
del li[2:]
print(li)
del li  # 删除之后，已经不存在，打印报错
print(li)

# 循环删除

li = [11, 22, 33, 44, 55, 66, 77, 88, 99]
for i in range(len(li)):
    print(i)
    del li[0]
    print(li)
