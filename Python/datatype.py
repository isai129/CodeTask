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