# python 解释器

---

Linux/Unix系统中，一般的python版本为2.x,可以将python3.x安装在/usr/local/python3目录中。

安装完成后，我们可以将路径 /usr/local/python3/bin 添加到您的 Linux/Unix 操作系统的环境变量中，
这样您就可以通过 shell 终端输入下面的命令来启动 Python3 。

    $ PATH=$PATH:/usr/local/python3/bin/python3    # 设置环境变量
    $ python3 --version
    Python 3.8.0

在Window系统下你可以通过以下命令来设置Python的环境变量，假设你的Python安装在 C:\Python38 下:

    set path=%path%;C:\python38

---

# 交互式编程

在命令提示符中输入"Python"命令来启动Python解释器：

    $ python3

    $ python
    Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
 
    print('hello,python!')
    hello,python!

当键入一个多行结构时，续行是必须的:

    flag = True
    if flag:
        print("flag条件为True!")
    flag条件为True!

---

# 脚本式编程


    $ python ../test/helloword.py
    hello,word
    The quick brown fox jumps over the laazy dog
    100+200= 300


[helloword](../test/helloword.py)


>在Linux/Unix系统中，你可以在脚本顶部添加以下命令让Python脚本可以像SHELL脚本一样可直接执行：
> > `#! /usr/bin/env python3`  
> >  修改脚本权限，使其有执行权限:`$ chmod +x hello.py`