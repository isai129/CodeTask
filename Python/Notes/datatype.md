# 基本数据类型

---

Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

> 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。

等号（=）用来给变量赋值。

等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。

    counter = 100
    miles = 1000.0
    name = 'alien'

---

## 1. 多个变量赋值

Python允许同时为多个变量赋值:
> 创建一个整型对象，值为 `1`，从后向前赋值，三个变量被赋予相同的数值。
>> `a = b = c = 1`

也可以为多个对象指定多个变量
> 两个整型对象` 1` 和 `2` 的分配给变量 `a` 和 `b`，字符串对象` "robot"` 分配给变量 c
>> `a, b, c = 1, 2, 'robot'`

---

## 2. 标准数据类型

Python中有六个标准的数据类型：

- Number(数字)
- String（字符串）
- List(列表)
- Tuple(元祖)
- Set（集合）
- Dictionary（字典）

> 不可变：Number(数字）、String（字符串）、Tuple（元祖）

> 可变：List（列表）、Dictionary（字典）、Set（字典）

---

### 1. Number（数字）

Python3 支持 `int`、`float`、`bool`、`complex`（复数）

> 置的 `type()` 函数可以用来查询变量所指的对象类型

    a, b ,c ,d = 20, 5.5,  True, 4+3j
    print(type(a), type(b), type(c), type(4))
    <class 'int'> <class 'float'> <class 'bool'> <class 'int'>

> 还可以用 isinstance 来判断：

    a = True
    isinstance(a,bool)
    True

`isinstance` 和 `type` 的区别在于：

- `type()`不会认为子类是一种父类类型
- `isinstance`会认为子类是一种父类类型

        class A:
            pass
        class B(A):
            pass
        isinstance(A(),A)
        class A:
            pass
        class B(A):
            pass
        isinstance(A(),A)
        type(A()) == A
        True
        isinstance(B(),A)
        True
        type(B()) == A
        False

当你指定一个值时，Number 对象就会被创建：

    val1 = 1
    val2 = 2

使用del语句删除一些对象引用:

    del var1[,var2[,var3[....,varN]]]

可以通过使用del语句删除单个或多个对象:

    var1,var2,var3,var4,var5 = 1, 2, 3, 4, 5
    del var1
    del var2, var3, var4, var5

*数值运算*

    >>> 5 + 4  # 加法
    9
    >>> 4.3 - 2 # 减法
    2.3
    >>> 3 * 7  # 乘法
    21
    >>> 2 / 4  # 除法，得到一个浮点数
    0.5
    >>> 2 // 4 # 除法，得到一个整数
    0
    >>> 17 % 3 # 取余
    2
    >>> 2 ** 5 # 乘方
    32

*注意：*

1. Python可以同时为多个变量赋值，如`a, b = 1, 2`
2. 一个变量可以通过赋值指向不同类型的对象
3. 数值的除法包含两个运算符：`/` 返回一个浮点数;`//` 返回一个整数
4. 在混合计算时，Python会把整型转换成为浮点数

*数值类型实例*

|   int    |    float    |   complex    |
|:------:	|:----------:	|:----------:	|
|   10    |     0.0        |    3.14j    |
|   100    |    12.70    |    45.j        |
|  -789    |    -21.9    | 9.322e-36j    |
|   080    |  32.3e+18    |    .876j    |
|  -0127    |     -90        |  -6.54+0j    |
| -0x260    | -32.54e100    |   3e+26j    |
|  0x69    |  70.2e-12    |  5.34e-7j    |

> Python还支持复数，复数由实数部分和虚数部分构成，可以用`a + bj`,或者`complex(a,b)`表示， 复数的实部`a`和虚部`b`都是浮点型

---

### 2. String（字符串）

Python中的字符串用单引号 `'` 或 双引号 `" `括起来，同时使用反斜杠 `\` 转义特殊字符。

字符串的截取的语法格式如下：

    变量[头下标:尾下标]

索引值以 0 为开始值，-1 为从末尾的开始位置：

![image](../Images/string-1.svG)

加号 `+` 是字符串的连接符， 星号 `*` 表示复制当前字符串，与之结合的数字为复制的次数:

    robot = 'google'
    print(robot)
    google
    print(robot[0:-1])
    googl
    print(robot[0])
    g
    print(robot[2:5])
    ogl
    print(robot[2:])
    ogle
    print(robot * 2)
    googlegoogle
    print(robot + 'TEST')
    googleTEST

> Python 使用反斜杠 `\`转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 `r`，表示原始字符串：

    print('go\nogle')
    go
    ogle
    print(r'go\nogle')
    go\nogle

> 另外，反斜杠()可以作为续行符，表示下一行是上一行的延续。也可以使用 `"""`...`"""` 或者 `'''`...`''' `跨越多行

> Python 没有单独的字符类型，一个字符就是长度为1的字符串。

> 与 C 字符串不同的是，Python 字符串不能被改变。
>> 向一个索引位置赋值，比如`word[0] = 'm'`会导致错误。

**注意：**

1. 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
2. 字符串可以用+运算符连接在一起，用*运算符重复。
3. Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
4. Python中的字符串不能改变。

---

### 3. List(列表)
