# 基本数据类型
---
Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

>在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。

等号（=）用来给变量赋值。

等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。

    counter = 100
    miles = 1000.0
    name = 'alien'

## 1. 多个变量赋值

Python允许同时为多个变量赋值:
>创建一个整型对象，值为 `1`，从后向前赋值，三个变量被赋予相同的数值。
>>    `a = b = c = 1`

也可以为多个对象指定多个变量
>两个整型对象` 1` 和 `2` 的分配给变量 `a` 和 `b`，字符串对象` "robot"` 分配给变量 c
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
