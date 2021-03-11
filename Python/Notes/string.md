# 字符串

---

字符串是 Python 中最常用的数据类型。我们可以使用引号( `'` 或 `"` )来创建字符串

创建字符串很简单，只要为变量分配一个值即可

    var1,var2 = 1 , 2

## 1. 访问字符串中的值

Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用

Python 访问子字符串，可以使用方括号 [] 来截取字符串，字符串的截取的语法格式如下：

    变量[头下标:尾下标]

> 索引值以 0 为开始值，-1 为从末尾的开始位置


![image](../Images/string-1.svg)

![images](../Images/python-str-runoob.png)

    var1 = "Hello World!"
    var2 = "google"
    var1[0]
    'H'
    var2[1:5]
    'oogl'

---

## 2. 字符串更新

截取字符串的一部分并与其他字段拼接

    var1 = 'hello word!'
    print("已更新字符串:",var1[:6]+"google")
    已更新字符串: hello google

---

## 3. 转义字符

需要在字符中使用特殊字符时，python 用反斜杠`\`转义字符:

