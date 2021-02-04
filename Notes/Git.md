# git

##终端命令
* $ mkdir 创建目录
* $ pwd 显示当前目录
* $ dir 显示当期目录 （windows）
 ---

### git命令

git init  --初始化仓库，将当前目录变成git可管理的仓库
>版本控制系统只能跟踪文本文件的变化
>在仓库目录下（或子目录）创建文件

$ git add <file> 将文件添加到仓库(暂存区)
>Unix的哲学是“没有消息就是好消息”

####把文件提交到仓库

    $ git commit -m <message>"说明" 
    告诉get，把文件提交到仓库，-m后面是本次提交的说明


#### git commit 可以一次提交多个文件
    * $ git add file1.txt
    * $ git add file2.txt file3.txt
    * $ git commit -m "add 3 files."
>> git status   查看仓库状态（status：状态） 
>> git diff <file> 查看差异（difference)，格式是unix通用的diff格式

####日志
    $ git log 显示从近到远的提交日志
    $ git log --pretty=oneline   一行显示，只显示哈希值和提交说明
>head 当前版本（指针）

####版本回退
    $ git reset --head <commit_id>
####命令记录
    $ git reflog

####修改文件名
    $ git mv <filename> <new filename>

####修改文件夹名(git mv)
    $ git mv <old folder> <new folder>
    1. -v 显示信息
    2. -f 强制重命名或移动，会覆盖目标文件
    3. -k 跳过对重命名或移动出错的文件
    4. -n 只显示信息
    @只能修改已经追踪的文件，直接commit提交
    
