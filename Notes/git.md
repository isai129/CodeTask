# git

## 终端命令

* $ `mkdir` 创建目录
* $ `pwd` 显示当前目录
* $ `rm` 删除文件
* $ `dir` 显示当期目录 （windows）

 ---
## 设置git的用户名邮箱
    1.git config --global user.name ""
    2.git config --global user.email ""
>`git config --list`查看git当前配置 

## git命令

### 1.初始化仓库

`git init`
> 初始化仓库，将当前目录变成git可管理的仓库 | 版本控制系统只能跟踪文本文件的变化 | 在仓库目录下（或子目录）创建文件

### 2. 将文件添加到暂存区-stage

`git add <file>`

    1.git add file1.txt [文件1]
    2.git add file2.txt file3.txt [文件1 文件2 文件3]
    3.git add . [所有文件]
    4.git add --all  [所有文件]
    5.git code/*  [某目录(code)下所有文件]
    6.git code/*.md [某目录(code)下所有.md文件]
    7.git add code [code目录]

### 3.提交暂存区至当前分支

`git commit -m <message>`
> **把文件提交到仓库(当前分支main/hosp)，-m后面是本次提交的说明.**

#### vim

> **git commit 不输入 -m <message>会进入vim模式**

1.vim两种工作模式

- 命令模式：接受执行vim命令（默认模式）
- 编辑模式：对打开的文件内容进行 增、删、改 操作；ESC 退回命令模式

2.创建、打开文件： `vi [filename]`

1. vi + 文件路径（或文件名）创建或打开已有文件
2. 输入‘i'或“Insert”键进入编辑模式

3.保存文件：

1. “ESC” 键，退出编辑模式
2. 在命令模式下键入"ZZ"或者":wq"保存修改并且退出 vim
3. 只想保存文件，则键入":w",停留在命令模式

4.放弃所有文件修改：

1. 放弃所有文件修改：按下 "ESC" 键进入命令模式，键入 ":q!" 回车后放弃修改并退出vi
2. 放弃所有文件修改，但不退出 vi ，按下 "ESC" 键进入命令模式，键入 ":e!" ，回车后回到命令模式。

### 4.显示当前分支状态

    git status

### 5.显示差异（difference)

> 工作区（working directory）->暂存区（index /stage）->本地仓库（repository）
>> git自动创建第一个 **master（main)** 分支，以及指向master(main)的 **head** 指针
![image](Images/git01.png "Work Directory-Repository")

- `git diff <file> `查看wording tree与index/stage的差异
- `git diff <file>` --cached 查看index/stage与repository的差异
- `git diff <file>`HEAD 查看working tree与repository的差异(HEAD代表最近一次commit的信息)

### 6.显示日志

    git log 显示从近到远的提交日志
    git log --pretty=oneline   一行显示，只显示哈希值和提交说明

> **head 指向当前分支（指针）**

### 7.版本切换

    git reflog 命令记录
    git reset --head <commit_id>

### 8.修改文件名

    git mv <old folder> <new folder>
    1. -v 显示信息
    2. -f 强制重命名或移动，会覆盖目标文件
    3. -k 跳过对重命名或移动出错的文件
    4. -n 只显示信息
    @只能修改已经追踪的文件，直接commit提交

### 9.撤销工作区的修改（un stage)

1. 未添加到stage `git checkout -- <file>`
2. 已添加到stage
    1. `git reset HEAD <file>`
    2. `git checkout -- <file>`
    3. 已提交至当前分支->参考[7.版本切换]前提是还未推送至远程库

## 待更新（git checkout可替换命令 git switch 和 git restore

#### 删除文件

1.输入错误命令：`rm <file>`

1. 误删：`git checkout -- file`
2. 确定删除:
1. `git rm <file>`（从版本库中删除文件）

> 误删：

1.`git reset --hard`(将暂存区和工作区都恢复成指针指向分支的最新版本)

2.`git commit -m <message>`

1. `git log --pretty=oneline`查看之前提交的commit_id
2. `git reset --hard commit_id`
3. `git push origin HEAD --force` 提交当前HEAD

### 10.远程仓库(main主分支)
####1.添加
1. 关联远程仓库： `git remote add origin git@github:username:main.git`

2. 第一次推送main分支的所有内容：`git push -u origin main`

3. 推送最新修改：`git push origin main`

####2.clone远程仓库(main-主分支)
1. ssh:`git clone git@github.com:user/branch` 
2. https:`git clone https://github.com/user/branch` 

### 11.分支管理
>平行宇宙:，当你正在电脑前努力学习Git的时候，另一个你正在另一个平行宇宙里努力学习SVN:

>>在某个时间点，两个平行宇宙合并了，结果，你既学会了Git又学会了SVN！

>>>![image](Images/git02.png "branch")

####1. 创建与合并
>`head`指向当前分支
>>创建`dev`分支，git会创建一个`dev`指针，指向`master`相同的提交,再把`HEAD`指向`dev`,就表示当前在dev分支上，从现在开始，对工作区的修改和提交就是针对dev分支了，比如新提交一次后，dev指针往前移动一步，而master指针不变：
>>![image](Images/git03.png "dev")
