# python数据类型和变量

---

## 1. python解释器

### 1. `print（）`函数

[hello python.py](../test/helloword.py "hello python")

### 2. python交互环境

命令行模式下，可以执行python进入Python交互式环境，也可以执行`python hello.py`运行一个.py文件。

> Git Bash `MinTTY`不支持交互操作,进入python解释器时前面需添加`winpty`。（在 /etc/bash.bashrc 这个文件中加入alias python=’winpty python ‘就好了，然后重启bash，因为它每次重启时会读取bashrc文件来进行初始配置。

`No such file or directory` ：必须切换到`.py`文件所在目录

Python交互式环境会把每一行Python代码的结果自动打印出来，但是，直接运行Python代码却不会。

[calc.py](../test/calc.py "calc")

> 直接运行Python文件，windows不行，mac和linux可以在文件首行加入`#!/user/bin/env python3`

### 3. 输入与输出（IO)

1. `print()`：在括号中加入字符串，可以输出指定文字[helloword.py](../test/helloword.py "hello word")
2.

## 2. 数据类型与变量

---

1. 整数

python可以处理任意大小的整数，包括负数。写法与数学上一样：`1`,`100`,`-8080`,`0`

*十六进制(hex)*：用前缀`0x`和0-9，a-f表示。

> 对于很大的数`1000000000`，很难数清楚0的个数。Python允许在数字中间以_分隔。写成10_000_000_000和10000000000是完全一样的。 十六进制数也可以写成0xa1b2_c3d4。
>
2.浮点数（小数）
> 浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的

> 浮点数可以用数学写法，如`1.23`，`3.14`，`-9.01`，等.对于很大或很小的浮点数，就必须用科学计数法表示，把10用e替代， 1.23x10<sup>10就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5，等等。

3.字符串 字符串是以单引号'或双引号"括起来的任意文本，比如'abc'，"xyz"等等。
> ''或""本身只是一种表示方式，不是字符串的一部分，因此，字符串'abc'只有a，b，c这3个字符。如果'本身也是一个字符，那就可以用""括起来， 比如"I'm OK"包含的字符是I，'，m，空格，O，K这6个字符。

> 转义字符`\`可以转义很多字符，比如`\n`表示换行，`\t`表示制表符，字符`\`本身也要转义，所以`\\`表示的字符就是`\`

> `r''`表示''内部的字符串默认不转义

> `'''...'''`的格式表示多行内容

4.布尔值 布尔值和布尔代数的表示完全一致，一个布尔值只有`True`、`False`两种值
> Python中，可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来

> 布尔值可以用and、or和not运算

1. `and`运算是`与`运算，只有所有都为`True`，`and`运算结果才是`True`
2. `or`运算是`或`运算，只要其中有一个为`True`，`or`运算结果就是`True`
3. `not`运算是`非`运算，它是一个`单目运算符`，把`True`变成`False`，`False`变成`True`

> 布尔值经常用在条件判断中:

5.空值（`None`)  
空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

6.**变量  
变量的概念基本上和初中代数的方程变量是一致的，只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。

> 变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头:

1. `a = 1`,变量`a`是一个整数。
2. `t_007 = "T007`，变量`t_007`是一个字符串。
3. `Answer = Ture`,变量`Answer`是一个布尔值`Ture`.

> 在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量。

> 变量本身类型不固定的语言称之为`动态语言`，与之对应的是`静态语言`。`静态语言`在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。

> 请不要把赋值语句的等号等同于数学的等号,比如下面的代码：

`x = 10`\
`x = x + 2`
从数学上理解x = x + 2那无论如何是不成立的,在程序中，赋值语句先计算右侧的表达式`x + 2`,，得到结果`12`，再赋给变量`x`。 由于`x`之前的值是`10`，重新赋值后，`x`的值变成`12`。

> 理解变量在计算机内存中的表示也非常重要:

当我们写：
`a = 'ABC'`
Python解释器干了两件事情：

1. 在内存中创建了一个'ABC'的字符串；
2. 在内存中创建了一个名为a的变量，并把它指向'ABC'。

> 也可以把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据

7. 常量 所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。
   > Python中，通常用全部大写的变量名表示常量(习惯上的用法)

#### 除法

在Python中，有两种除法:

1. `/`,结果是浮点数，即使是两个整数恰好整除，结果也是浮点数.
2. `//`称为地板除，两个整数的除法仍然是整数(只取结果的整数部分)

> `%`余数运算 可以得到两个整数相除的余数

> Python支持多种数据类型，在计算机内部，可以把任何数据都看成一个“对象”，而变量就是在程序中用来指向这些数据对象的， 对变量赋值就是把数据和变量给关联起来。

> 对变量赋值`x = y`是把变量`x`指向真正的对象，该对象是变量`y`所指向的。随后对变量`y`的赋值不影响变量`x`的指向。

> Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的

> Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。

## 3. 字符串和编码

### 1. ASCII和Unicode

区别：ASCII编码是1个字节，而Unicode编码通常是2个字节。

1. 字`A`用`ASCII`编码是十进制的`65`，二进制的`01000001`；
2. 字符`0`用`ASCII`编码是十进制的`48`，二进制的`00110000`，注意字符`'0'`和整数`0`是不同的；
3. 汉字`中`已经超出了`ASCII`编码的范围，用`Unicode`编码是十进制的`20013`，二进制的`01001110 00101101`

> 如果把`ASCII`编码的`A`用`Unicode`编码，只需要在前面补`0`就可以，因此，`A`的`Unicode`编码是`00000000 01000001`。

> 如果统一成Unicode编码，乱码问题从此消失了。但是，如果你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间， 在存储和传输上就十分不划算。

### 2. `UTF-8`编码

> `UTF-8`编码把一个`Unicode`字符根据不同的数字大小编码成`1-6`个字节，常用的英文字母被编码成`1`个字节，汉字通常是`3`个字节，只有很生僻的
> 字符才会被编码成`4-6个`字节。如果你要传输的文本包含大量英文字符，用`UTF-8`编码就能节省空间：

| 字符    | ASCII        | Unicode            | UTF-8                        |
|------	|----------	|-------------------	|----------------------------	|
| A        | 01000001    | 00000000 01000001    | 01000001                    |
| 中    | x            | 01001110            | 11100100 10111000 10101101    |

> 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

> 用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件
> ![images](../Images/Unicode&UTF-8.png)
> 浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器：
> ![images](../Images/Unicode&UTF-8.2.png)

### 3. Python的字符串

> 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言
[the_string.py](../test/the_string.py "string")

1. 对于单个字符的编码,Python提供了
    1. `ord()`函数获取字符的整数表示；`chr(66)'B'`
    2. `chr()`函数把编码转换为对应的字符。`chr(25991)'文'`

> 由于Python的字符串类型是`str`，在内存中以Unicode表示，一个字符对应若干个字节。
> 如果要在网络上传输，或者保存到磁盘上，就需要把`str`变为以字节为单位的`bytes`。

2. Python对`bytes`类型的数据用带`b`前缀的单引号或双引号表示：`x = b'ABC'`

> 注意区分`'ABC'`和b`'ABC'`，前者是`str`，后者虽然内容显示得和前者一样，但`bytes`的每个字符都只占用一个字节。

3. 以Unicode表示的`str`通过`encode()`方法可以编码为指定的`bytes`

`'ABC' .encode('ascii')
b'ABC'
'中文' .encode('UTF-8')
b'\xe4\xb8\xad\xe6\x96\x87'`
> 纯英文的`str`可以用`ASCII`编码为`bytes`，内容是一样的，含有中文的`str`可以用`UTF-8`编码为`bytes`。
> 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。

> 在`bytes`中，无法显示为`ASCII`字符的字节，用`\x##`显示。

> 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是`bytes`。要把`bytes`变为`str`，就需要用`decode()`方法：
> `b'ABC' .decode('utf-8') 'ABC'`

> 如果bytes中包含无法解码的字节，decode()方法会报错：
`b'\xe4\xb8\xad\xff'.decode('utf-8')  
Traceback (most recent call last):  
File "<input>", line 1, in <module>  
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 3: invalid start byte`
> 如果`bytes`中只有一小部分无效的字节，可以传入`errors='ignore'`忽略错误的字节：

`b'\xe4\xb8\xad\xfd' .decode('utf-8',errors='ignore')
'中'`
> 要计算`str`包含多少个字符，可以用`len()`函数：
`len('abcde')
5`
> `len()`函数计算的是`str`的字符数，如果换成`bytes`，`len()`函数就计算字节数：

` len(b'ABC')
3 len(b'\xe4\xb8\xad\xe6\x96\x87')
6 len('中文'.encode('utf-8'))
6`

> 在操作字符串时，我们经常遇到`str`和`bytes`的互相转换。为了避免乱码问题，应当始终坚持使用`UTF-8`编码对`str`和`bytes`进行转换。

> 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
> 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：

    `#!/usr/bin/env python3 `   ** 告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释 **
    `# -*- coding: utf-8 -*- `  ** 告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。 **

> 申明了UTF-8编码并不意味着你的`.py`文件就是`UTF-8`编码的，必须并且要确保文本编辑器正在使用`UTF-8 without BOM`编码：

### 4. 格式化

#### 1. %

> 输出格式化的字符串,在Python中，采用的格式化方式和C语言是一致的，用`%`实现:

> 在字符串内部，`%s`表示用字符串替换，`%d`表示用整数替换，有几个`%?`占位符，后面就跟几个变量或者值，顺序要对应好。
> 如果只有一个`%?`，括号可以省略。

|  占位符    |  %d    |   %f    |   %s    |      %x        |
|:--------:	|:----:	|:------:	|:------:	|:------------:	|
| 替换内容    | 整数    | 浮点数    | 字符串    | 十六进制整数    |

> 其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：

    'hello,%s' %' word'  
    'hello, word'  
    'Hi, %s, you have $%d.' % ('Michael',1000000)  
    'Hi, Michael, you have $1000000.'

> 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
> 字符串里面的%是一个普通字符怎么办？这个时候就需要转义,用%%来表示一个%  
`'growth rate: %d %%' % 7`  
`growth rate: 7 %`

#### 2. format()

> 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多

`'hello,{0},成绩提升了{1: .1f}%'.format('小明',17.125)`  
`hello,小明,成绩提升了 17.1%`

#### 3. f-string

> 最后一种格式化字符串的方法是使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换：  
`r = 2.5`  
`s = 3.14 * r **2 `  
`print(f'the area of a circle with radius {r} is {s:2f}')`  
`the area of a circle with radius 2.5 is 19.625000`  
> 上述代码中，{r}被变量r的值替换，{s:.2f}被变量s的值替换，并且:后面的.2f指定了格式化参数（即保留两位小数），因此，{s:.2f}的替换结果是19.62。

> Python 3的字符串使用Unicode，直接支持多语言。

> 当`str`和`bytes`互相转换时，需要指定编码。最常用的编码是`UTF-8`。

## 4. 使用list和tuple

### 1. list （列表）

Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
`   classmates = ['michael','bob','tracy']`  
`  classmates`  
`  ['michael', 'bob', 'tracy']`

变量classmates 就是一个list

#### 1. `len()` 获得list元素的个数：

    `len(classmates)`  
    `3`

> 用索引来访问list中每一个位置的元素，记得索引是从`0`开始的：

`classmates[0]`  
`michael`  
`classmates[1]`  
`bob`  
`classmates[2]`  
`tracy`  
`classmates[3]`  
`Traceback (most recent call last):
File "<input>", line 1, in <module>
IndexError: list index out of range`

> 当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。

`classmates[-1]`
`tracy`
> 以此类推，可以获取倒数第2个、倒数第3个：

`>>> classmates[-2]`  
`Bob`  
`>>> classmates[-3]`  
`Michael`  
`>>> classmates[-4]`  
`Traceback (most recent call last):
File "<stdin>", line 1, in <module>
IndexError: list index out of range`
> 当然，倒数第4个就越界了。

#### 2.  `append()`，list中追加元素到末尾：

` classmates.append('adam')`  
`classmates`  
`['michael', 'bob', 'tracy', 'adam']`

#### 3.  `insert()` ，把元素插入到指定位置：

`classmates.insert(1,'adamx')`
`classmates`
`['michael', 'adamx', 'bob', 'tracy', 'adam']`

#### 4. `pop()`，删除list末尾的元素：

`classmates.pop()`
`adam`
`classmates`
`['michael', 'adamx', 'bob', 'tracy']`
> 要删除指定位置的元素，用`pop(i)`方法，其中`i`是索引位置：  
`classmates.pop(1)`  
`adamx`  
`classmates`  
`['michael', 'bob', 'tracy']`

> 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：  
`classmates[1] = 'sarah'`
`classmates`
`['michael', 'sarah', 'tracy']`

> list里面的元素的数据类型也可以不同:  
`L = ['Apple',123,True]`

> list元素也可以是另一个list:  
`s = ['python','java',['asp','php'],'scheme']`   
`len(s)`  
`4`
>> 注意s只有4个元素，其中s[2]又是一个list，如果拆开写就更容易理解了：  
` p = ['asp','php']`  
`s = ['python','java',p,'scheme']`
>>> 要拿到'php'可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到。  
`p[1]`  
`php`  
`s[2][1]`  
`php`

> 如果一个list中一个元素也没有，就是一个空的list，它的长度为0：  
`L = []`  
`len(L)`  
`0`

### 2. tuple (元祖)

另一种有序列表叫元组：tuple。
> tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
> > `classmates = ('michael','bob','tracy')`  
> > 现在，`classmates`这个`tuple`不能变了，它也没有`append()`，`insert()`这样的方法。其他获取元素的方法和`list`是一样的，你可以
> > 正常地使用`classmates[0]`，`classmates[-1]`，但不能赋值成另外的元素。

**tuple的陷阱：**
当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来:

    t = (1,2)
    t
    (1, 2)

如果要定义一个空的tuple，可以写成()：

    t = ()
    t
    ()

> 但是，要定义一个只有1个元素的tuple，如果你这么定义：
`t = (1)`  
`t`  
`1`
> > 定义的不是`tuple`，是`1`这个数！  
> > 因为括号`()`既可以表示`tuple`，又可以表示数学公式中的小括号，这就产生了歧义  
> > 因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是`1`。
> 所以，只有`1`个元素的`tuple`定义时必须加一个逗号`,`，来消除歧义：
`t = (1,)`  
`t`  
`(1,)`

> **可变的`tuple`：**
>> `` t = ('a','b',['A','B'])``  
> 此时tuple包含三个元素： ![image](../Images/tuple0.png )

    t[2][0] = 'X'
    t[2][1] = 'Y'

> 当我们把list的元素'A'和'B'修改为'X'和'Y'后，tuple变为：
![image](../Images/tuple1.png )
t
('a', 'b', ['X', 'Y'])

> 表面上看，`tuple`的元素确实变了，但其实变的不是`tuple`的元素，而是`list`的元素。tuple一开始指向的list并没有改成别的list，所以，tuple
> 所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向`a`，就不能改成指向`b`，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！

`list`和`tuple`是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。

## 5. 条件判断

计算机之所以能做很多自动化的任务，因为它可以自己做条件判断。

年龄判断：

    age = 3
    if age >= 18:
        print('your age is',age)
        print('adult')
    else:
        print('your age is', age)
        print('teenager')
    your age is 3
    teenager

> 根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。

也可以用`elif`做更细致的判断：

    age = 3
    if age >= 18:
        print('adult')
    elif age >= 6:
        print('teenager')
    else:
        print('kid')
    kid

`elif`是`else if`的缩写，完全可以有多个`elif`,所以`if`得语句完整形式是：

    if <条件判断1>:
        <执行1>
    elif<条件判断2>:
        <执行2>
    elif<条件盘判断3>:
        <执行3>
    ...
    else:
        <执行...>

> `if`语句执行有个特点，它是从上往下判断，如果在某个判断上是`True`，把该判断对应的语句执行后，就忽略掉剩下的`elif`和`else`。

`if`判断条件还可以简写:

    if x:
        print('True')

只要`x`是非零数值、非空字符串、非空list等，就判断为True，否则为False。

**input()**
用input()读取用户的输入，这样可以自己输入，程序运行得更有意思：  
[input()](../test/input.py)