# 公共方法
# 1.排序
# 正向排序：sort()
li = [1, 5, 6, 3, 2, 9, 7]
li.sort()
print(li)
# 倒序排序: li.sort(reverse=Ture)
li = [1, 3, 2, 7, 5, 0, 6]
li.sort(reverse=True)
print(li)

# 反转： li.reverse()
li = [2, 1, 0, 5, 4, 7]
li.reverse()
print(li)

# 补充：
# 字符串列表排序——根据字符串的第一个字符对应的ASCII码排序
li = ['lhdsf', 'dsaow', 'oefec', 'pwfic']
li.sort()
print(li)

# count()数元素出现的次数
li = ['fdsc', 'dsa', '木木', [2, 4, 6, 1, 6], '木木']
num = li.count('木木')
print(num)

# len()计算列表长度
li = [3, 5, 1, ['木木', 'tre', 'pld'], 'etg', '木木']
l = len(li)
print(l)

# li.index('元素’）查看索引
li = ['sff', 'rew', '陌陌', [2, 5, 1, 0, 3], 'ai', 'tw']
print(li.index('ai'))
