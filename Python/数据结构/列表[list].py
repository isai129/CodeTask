# 处理一组有序项目的数据结构，即你可以在一个列表中存储一个 序列 的项目,一旦你创建了一个列表，你可以添加、删除或是搜索列表中的项目

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

# 列表— 改
# li[索引] = '被修改的内容‘

li = ['苹果', '芒果', '胡萝卜', '香蕉']
li[0] = '火龙果'  # 将索引为0的位置改为‘火龙果’
print(li)

#  li[切片] = '被修改的内容'（迭代式: 分成最小的元素，一个一个添加）

li = ['苹果', '芒果', '胡萝卜', '香蕉']
li[0:2] = 'abcd'  # 将索引0-2替换为abcd,切片之后迭代处理
print(li)

li[0:3] = ['我', '喜欢', '吃', '水果']
print(li)

#  列表 —— 查
#  从头到尾 ：for循环

li = ['苹果', '芒果', '胡萝卜', '香蕉']
for i in li:
    print(i)

# 某一个：索引
li = ['苹果', '芒果', '胡萝卜', '香蕉']
print(li[1])

# 一段：切片
li = ['苹果', '芒果', '胡萝卜', '香蕉']
print(li[0:2])

# 列表——嵌套

li = ['苹果', '芒果', '胡萝卜', ['a', 'b', 'c'], '香蕉']
print(li[2][1])
li[3][0].upper()  # 把列表中第四个元素列表的第一个元素变为大写
print(li)

# 列表——循环打印
# 索引默认从零开始
li = ['alex', 'root', 'ser', 'egon']
for i in li:
    print(li.index(i), i)

# 指定索引从100开始
for index, i in enumerate(li, 100):
    print(index, i)

# 其他常用操作

# split : 字符串转换成列表 str->list
s = 'xscd_fdsf_cdsvb_陌陌'
print(s.split('_'))

s1 = 'cds cjk sdl nkl g gfd gj kl jfk dlg f od jis fds342 34 234 235'
print(s1.split(' '))

# join:列表转换成字符串 list->str
# join(可迭代对象iterable) s
# 可迭代对象iterable: list,str,元祖
li = ['sxcd', 'gsg', 'fdsfds', '3242', 'gdg']
s = ''.join(li)
print(s)
s1 = '_'.join(li)
print(s1)

# rang : 顾头不顾尾——相当于有序的数字列表（可以反向，加步长）

for i in range(2, 6):
    print(i)

for i in range(3, 300, 5):
    print(i)

# 应用实例：
# 循环打印，列表里遇到列表也需要循环打印

li = [1, 2, 3, 4, 'alex', [3, 4, 5, 'route'], 'ear']
print(li)
for i in li:
    if type(i) == list:
        for n in i:
            print(n)
    else:
        print(i)

