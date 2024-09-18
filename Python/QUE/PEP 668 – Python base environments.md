## 前言

### [](https://www.yaolong.net/article/pip-externally-managed-environment/#%E7%8E%B0%E8%B1%A1)现象

在 Manjaro 22、Ubuntu 23.04、Fedora 38 等最新的linux发行版中运行pip install时，通常会收到一个错误提示：`error: externally-managed-environment`，即“外部管理环境”错误，但这不是一个 bug。

![](https://www.yaolong.net/img/2023/pipx/pip3_error.png)

如果您想阅读，这是完整的错误信息：

|   |   |
|---|---|
|```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>```|```bash<br>$ sudo pip3 install please-cli<br>error: externally-managed-environment<br><br>× This environment is externally managed<br>╰─> To install Python packages system-wide, try 'pacman -S<br>    python-xyz', where xyz is the package you are trying to<br>    install.<br>    <br>    If you wish to install a non-Arch-packaged Python package,<br>    create a virtual environment using 'python -m venv path/to/venv'.<br>    Then use path/to/venv/bin/python and path/to/venv/bin/pip.<br>    <br>    If you wish to install a non-Arch packaged Python application,<br>    it may be easiest to use 'pipx install xyz', which will manage a<br>    virtual environment for you. Make sure you have python-pipx<br>    installed via pacman.<br><br>note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.<br>hint: See PEP 668 for the detailed specification.<br>```|

### [](https://www.yaolong.net/article/pip-externally-managed-environment/#%E8%83%8C%E5%90%8E%E7%9A%84%E5%8E%9F%E5%9B%A0)背后的原因

“外部管理环境”错误背后的原因：Manjaro 22、Ubuntu 23.04、Fedora 38 以及其他的最新发行版中，正在使用 Python 包来实现此增强功能。

这个更新是为了避免「操作系统包管理器 (如pacman、yum、apt) 和 pip 等特定于 Python 的包管理工具之间的冲突」。

这些冲突包括 Python 级 API 不兼容和文件所有权冲突。

  

更多详情可以在官方查看：

[

PEP 668 – Python base environments

Python 增强提案 (PEP)

![](https://www.yaolong.net/site/py.png)peps.python.org


  
---

## [](https://www.yaolong.net/article/pip-externally-managed-environment/#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88)解决方案

### [](https://www.yaolong.net/article/pip-externally-managed-environment/#%E6%96%B9%E6%A1%88%E4%B8%80%E7%B2%97%E6%9A%B4-%E5%8E%BB%E6%8E%89%E8%BF%99%E4%B8%AA%E6%8F%90%E7%A4%BA)方案一、(粗暴) 去掉这个提示

强制删除此警告，回归到熟悉的操作。

将 “x” 替换为实际版本。

|   |   |
|---|---|
|```<br>1<br>```|```bash<br>sudo mv /usr/lib/python3.x/EXTERNALLY-MANAGED /usr/lib/python3.x/EXTERNALLY-MANAGED.bk<br>```|

  

和之前一样，现在您可以直接运行 `pip(3) install package_name` 命令来安装python模块。

  

### [](https://www.yaolong.net/article/pip-externally-managed-environment/#%E6%96%B9%E6%A1%88%E4%BA%8C%E6%8E%A8%E8%8D%90-%E4%BD%BF%E7%94%A8pipx)方案二、(推荐) 使用pipx

您在上面看到的涉及手动工作。Pipx 使其自动化。

它会自动为您安装的每个应用程序创建一个新的虚拟环境。不仅。它还在 中创建指向它的链接.local/bin。这样，安装该软件包的用户就可以从命令行中的任何位置运行它。

我想这就是大多数桌面 Linux 用户想要的。

使用以下命令在 Ubuntu 上安装 pipx：

|   |   |
|---|---|
|```<br>1<br>```|```bash<br>sudo apt install pipx<br>```|

它可能会安装大量的依赖项：

![](https://www.yaolong.net/img/2023/pipx/install-pipx.png)

现在将其添加到 PATH 中，以便您可以从任何地方运行。

|   |   |
|---|---|
|```<br>1<br>```|```bash<br>pipx ensurepath<br>```|

![](https://www.yaolong.net/img/2023/pipx/pipx-ensurepath.png)

提示：

您必须关闭终端并重新登录才能发生更改。

现在我们可以使用 Pipx 而不是 Pip 安装 Python 包：

|  |  |
| ---- | ---- |
| ```<br>1<br>``` | ```bash<br>pipx install package_name<br>``` |
|  |  |

这个是一个例子：

![](https://www.yaolong.net/img/2023/pipx/pipx-install-example.png)

提示：

要删除使用 pipx 安装的软件包，请使用 `pipx uninstall package_name` 命令。

  

### [](https://www.yaolong.net/article/pip-externally-managed-environment/#%E6%96%B9%E6%A1%88%E4%B8%89%E9%AB%98%E9%98%B6-%E4%BD%BF%E7%94%A8venv)方案三、(高阶) 使用venv

如果您是开发人员，

在运行或构建py文件时遇到如下图 `ModuleNotFoundError: No module named 'xxx'` 的错误，

推荐切换为该方案，即使用Python虚拟环境。

![](https://www.yaolong.net/img/2023/pipx/py_error.png)

借助虚拟环境，您可以使用不同版本的包依赖项和Python。这样，您就可以避免包之间的任何冲突。

> 这种方法适合从事Python项目的软件开发人员和程序员。

#### [](https://www.yaolong.net/article/pip-externally-managed-environment/#%E5%AE%89%E8%A3%85-venv)安装 venv

|   |   |
|---|---|
|```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>```|```bash<br><br>sudo apt install python3-venv<br><br>#或<br><br>sudo apt install python3.10-venv<br><br>```|

#### [](https://www.yaolong.net/article/pip-externally-managed-environment/#%E7%94%9F%E6%88%90%E4%B8%80%E4%B8%AApython%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83)生成一个Python虚拟环境

|   |   |
|---|---|
|```<br>1<br>```|```bash<br>mkdir -p $HOME/.env && python3 -m venv $HOME/.env/project_name<br>```|

现在，您将看到一个.env在您的主目录中，并且在 .env 中，您将拥有项目目录。

每个虚拟环境项目目录中都会有自己的 Python 和 Pip 副本。

#### [](https://www.yaolong.net/article/pip-externally-managed-environment/#%E5%AE%89%E8%A3%85%E6%A8%A1%E5%9D%97%E5%A6%82-algoliasearch)安装模块，如 algoliasearch

|   |   |
|---|---|
|```<br>1<br>2<br>```|```bash<br>$HOME/.env/project_name/bin/python -m pip install --upgrade pip<br>$HOME/.env/project_name/bin/python -m pip install algoliasearch<br>```|

#### [](https://www.yaolong.net/article/pip-externally-managed-environment/#%E7%94%A8%E6%96%B0%E7%9A%84%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83%E6%89%A7%E8%A1%8Cpy%E6%96%87%E4%BB%B6)用新的虚拟环境执行py文件

|   |   |
|---|---|
|```<br>1<br>2<br>```|```bash<br>source $HOME/.env/project_name/bin/activate<br>$HOME/.env/project_name/bin/python ./demo.py<br>```|

  

这只是 Python 虚拟环境的一个简短示例。如果您想了解更多信息，这里有一份详细指南。

[

Python Virtual Environments

在本教程中，您将学习如何使用 Python 虚拟环境来管理 Python 项目。您还将深入了解使用 venv 模块构建的虚拟环境的结构，以及使用虚拟环境背后的原因环境背后的原因。



![](https://www.yaolong.net/site/realpython.jpg)

](https://realpython.com/python-virtual-environments-a-primer/?ref=yaolong.net "Python Virtual Environments")  

### [](https://www.yaolong.net/article/pip-externally-managed-environment/#%E6%96%B9%E6%A1%88%E5%9B%9B%E5%85%B6%E4%BB%96-%E4%BD%BF%E7%94%A8%E5%8E%9F%E7%94%9F%E5%8C%85)方案四、(其他) 使用原生包

据我所知，Pip 提供了一种安装 Python 包的舒适方法。然而，一些Python应用程序也打包为APT或其他本机包。在您的发行版存储库中搜索它并从那里安装它（如果可用）。

例如，我试图安装 WoeUSB-ng。如果我使用 Arch Linux，AUR 也提供相同的软件包。

  

