#pip

---

*pip是[Python](python_basics.md "python_basics")中的标准库管理器，它允许你安装和管理不属于 Python标准库 的其它软件包。*

>JavaScript使用npm管理软件包，Ruby使用Gem,.NET使用NuGet。

> 在控制台中运行以下命令来验证 pip 是否可用：`pip --version`:
`pip 21.0.1 from c:\program files\python37\lib\site-packages\pip (python 3.7)`

> Python 拥有一个活跃的社区，它提供了一个更大的软件包集合，以供你开发所需。这些软件包发布在[Python Package Index](https://python.freelycode.com/contribution/detail/1544) ，也被称为 PyPI（发音 Pie Pea Eye）。

##1. Python Package Index(PyPI)

很多软件包通过为已有功能提供了友好地接口来简化 Python 开发。例如，你可以写一个脚本，仅使用 Python 标准库中的功能分析网页的内容：
[using-http.py](../using-http.py "pypi")
pip 会在 PyPI 中查找安装包，计算其依赖关系，安装并确保其能正常工作。

##2. requests
>PyPI 托管了一个非常流行的库 [requests](https://2.python-requests.org/en/master/ "requests docs") 来完成 HTTP 请求。

##3. 命令
    1.pip --version #显示版本和路径

    2.pip --help #获取帮助

    3.pip install -U pip #升级pip

    4.pip install SomePackage #最新版本

    5.pip install SomePackage==1.27 #指定版本

    6.pip install SomePackage>=1.27 #最小版本

    7.pip install --upgeade SomePackage #升级包，通过使用==，>=, <=, >, < 来指定一个版本号
    或pip install -U SomePackage #升级包

    8.pip uninstall SomePackage #卸载包

    9.pip search SomePackage  #搜索包

    10.pip show #显示安装包信息

    11.pip show -f SomePackage #查看指定包的详细信息

    12.pip list #列出已安装的包

    13.pip list -0 #查看可升级的包

    14.pip freeze #查看已经安装的包以及版本信息

    15.pip freeze -all > requirements.txt #输出本地包环境至文件

    16.pip install -r requirements.txt #安装指定文件中的包 (在其他系统中复制开发环境)

    17.pip install redis -i SomePackage -i https://mirrors.aliyun.com/pypi/simple(阿里云）



>添加pip 配置文件

1. 查看用户主目录下有没有“~/.pip/pip.conf"文件，没有则创建:

   1. `cd ~ `
   2. `mkdir .pip`
   3. `touch pip.conf`

2.打开配置文件，添加配置：
1. 豆瓣

    >[global]\
    index-url=http://pypi.douban.com/simple
    [install]trusted-host=pypi.douban.com`

2. 阿里云

    [global]\
    >index-url=http://mirrors.aliyun.com/pypi/simple
    [install]trusted-host=mirrors.aliyun.com`

### 国内源:

    1. 阿里云: https://mirrors.aliyun.com/pypi/simple

    2. 中国科技大学: https://pypi.mirrors.ustc.edu.cn/simple

    3. 豆瓣(douban): http://pypi.douban.com/simple

    4. 清华大学: https://pypi.tuna.tsinghua.edu.cn/simple



# 测试框架[pytest](https://docs.pytest.org/en/latest/ "pytest")
