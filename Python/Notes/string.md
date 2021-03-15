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

| **转义字符** | **描述**                                           | **实例**                                                                                                |
|----------|--------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| \(在行尾时)  | 续行符                                              | print("line1\<br>...line2\<br>...line3")<br>line1 line2 line3                                         |
| \\       | 反斜杠符号                                            | print("\\")                                                                                           |
| \'       | 单引号                                              | print("\'")                                                                                           |
| \''      | 双引号                                              | print("\"")                                                                                           |
| \a       | 响铃                                               | print("\a")                                                                                           |
| \b       | 退格(backspace)                                    | print("Hello \b World")                                                                               |
| \000     | 空                                                | print("\000")                                                                                         |
| \n       | 换行                                               | print("\n")                                                                                           |
| \v       | 纵向制表符                                            | print("Hello \v World")                                                                               |
| 	        | 横向制表符                                            | print("Hello 	 World")                                                                                |
| \r       | 回车,将\r后面的内容移到字符串开头,并逐一替换开头部分的字符,直至将\r后面的内容完全替换完成 | print("Hello \rWorld!")<br>World!<br>print("google runoob taobao \r 123456")<br>123456 runoob taobao  |
| \f       | 换页                                               | print("Hello World")                                                                                  |
| \yyy     | 八进制数,y代表0~7的字符,例如:\012代表换行                       |  print("\110\145\154\154\157\40\127\157\162\154\144\41")<br>Hello World!                              |
| \xyy     | 十六进制数，以 \x 开头，y 代表的字符，例如：\x0a 代表换行               | print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")<br>Hello World!                             |
