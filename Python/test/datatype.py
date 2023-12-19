# 数据类型
# 字符串是由单引号‘’或双引号“”括起来的任意文本
print('abc')

# 转义符\
# \n 表示换行 ，\t 表示制表符，\\ 表示 \
print('I\'m "OK\"!')
print('I\'m "OK"！')
print('\\\n 换行')
print('\t')
# r 表示’‘内的字符默认不转义
print(r'\\\t\\\\\\t\\')
# '''...'''表示多行内容
print('''line1
line2
line3''')
print(r'''hello,\n world''')

# 布尔值
age = 19
if age >= 18:
    print(True)
else:
    print(False)
# 变量
a = 123  # a是整数
print(a)  # 输出`123`
a = 'ABC'  # 变成字符串,解释器创建了字符串'ABC'和变量a，并把a指向'ABC'：
print(a)  # 输出 `ABC`
b = a # 解释器创建了变量b，并把b指向a指向的字符串'ABC'：
a = 'CBA' # 解释器创建了字符串'XYZ'，并把a的指向改为'XYZ'，但b并没有更改：
print(b)  # 输出 `ABC`
