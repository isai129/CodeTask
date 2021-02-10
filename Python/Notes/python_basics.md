#python数据类型和变量

---

##第一个python程序

###1. `print（）`函数

[hello python.py](../helloword.py "hello python")

###2. python交互环境

命令行模式下，可以执行python进入Python交互式环境，也可以执行python hello.py运行一个.py文件。

>Git Bash `MinTTY`不支持交互操作,进入python解释器时前面需添加`winpty`。（在 /etc/bash.bashrc 这个文件中加入alias python=’winpty python ‘就好了，然后重启bash，因为它每次重启时会读取bashrc文件来进行初始配置。

`No such file or directory` ：必须切换到`.py`文件所在目录

Python交互式环境会把每一行Python代码的结果自动打印出来，但是，直接运行Python代码却不会。

[calc.py](../calc.py "calc")

##数据类型

---

1. 整数

    python可以处理任意大小的整数，包括负数。写法与数学上一样：`1`,`100`,`-8080`,`0`

    *十六进制(hex)*：用前缀`0x`和0-9，a-f表示。

    >对于很大的数`1000000000`，很难数清楚0的个数。Python允许在数字中间以_分隔。写成10_000_000_000和10000000000是完全一样的。十六进制数也可以写成0xa1b2_c3d4。