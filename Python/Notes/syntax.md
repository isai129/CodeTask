#Python3 基础语法
___

## 1. 编码

默认情况下，Python 3 源码文件以 `UTF-8` 编码，所有字符串都是 `unicode` 字符串。 

---

## 2. 标识符

- 第一个字符必须是字母表中字母或下划线` _ `
- 标识符的其他的部分由字母、数字和下划线组成
- 标识符对大小写敏感

>在 Python 3 中，可以用中文作为变量名，非 ASCII 标识符也是允许的
---

## 3. python保留字

保留字即关键字，我们不能把它们用作任何标识符名称。

>Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：
>> `import keyword`  
>> `keyword.kwlist`  
>` ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 
 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']`
---

## 4. 注释

Python中单行注释以` #` 开头:
`#!/usr/bin/python3`

多行注释可以用多个 `#` 号，还有 `'''` 和 `"""`：

        #!/usr/bin/python3
 
        # 第一个注释
        # 第二个注释
         
        '''
        第三注释
        第四注释
        '''
         
        """
        第五注释
        第六注释
        """

---

## 5. 行与缩进

python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {}

缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数

---

## 6. 多行语句

Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠`\`来实现多行语句

在 `[]`,` {}`, 或 `()` 中的多行语句，不需要使用反斜杠`\`

---

## 7. 数字(Number)类型

python中数字有四种类型：整数、布尔型、浮点数和复数。

- int(整数):1
- bool(布尔)：Ture，False。
- float(浮点数)：1.24,3E-2
- complex(复数)：1+2j

## 8. 字符串(String)

- python中单引号和双引号使用完全相同
- 使用三引号(`'''`或`"""`)可以指定一个多行字符串
- 转义符 `\`
- 反斜杠可以用来转义，使用`r`可以让反斜杠不发生转义
- 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
- 字符串可以用 `+` 运算符连接在一起，用 `*` 运算符重复
- Python 中的字符串有两种索引方式，从左往右以 `0` 开始，从右往左以 `-1 `开始
- Python中的字符串不能改变
- Python 没有单独的字符类型，一个字符就是长度为 1 的字符串
- 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]

## 9. 空行

函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。

空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。

>空行也是程序代码的一部分。

## 10. 等待用户输入

        input("\n\n按下 enter 键后退出。")

> "\n\n"在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出。

## 11. 同一行显示多条语句

Python可以在同一行中使用多条语句，语句之间使用分号`;`分割

    import sys ; x = 'runoob'; sys.stdout.write(x + '\n')

## 12. 多个语句构成代码组

缩进相同的一组语句构成一个代码块，我们称之代码组。

像`if`、`while`、`def`和`class`这样的复合语句，首行以关键字开始，以冒号 `:` 结束，该行之后的一行或多行代码构成代码组。

我们将首行及后面的代码组称为一个子句(clause)。

## 13. print 输出

print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：

[print.py](../test/print.py)

## 14. import与form...import

在 python 用` import` 或者 `from...import` 来导入相应的模块

- 将整个模块(module)导入，格式为： `import module`

- 从某个模块中导入某个函数,格式为： `from module import function`

- 从某个模块中导入多个函数,格式为： `from module import first func, second func, third func`

- 将某个模块中的全部函数导入，格式为： `from module import *`

