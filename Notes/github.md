# github远程仓库

## 1.创建SSH Key

> 切换至用户主目录下

1. 主目录目录下生成SSH Key的秘钥对（.ssh\id_rsa<私钥>,id_rsa.pub<公钥>文件）
   1.  `cd ~`
   2.  `ssh-keygen -t rsa -c "youremail@example.com"`

2. 拷贝公钥 id_rsa.pub内容\
    `cat .ssh/id_rsa.pub`
## 2.在github中绑定ssh秘钥

登陆GitHub，打开“settings”，“SSH and GPG Keys”页面，点击‘New SSH key’， 然后填上Title，在Key文本框里粘贴id_rsa.pub文件的内容，然后点击’Add SSH key’

## 3.创建远程仓库

## 4.与本地仓库建立链接

> 建立关联：`git remote add origin` <远程仓库ssh地址>

> 删除关联：`git remote rm origin`

> 查看关联：`git remote -v`

## 5.同步

> #### 本地项目推送到远端
> 1. 初始化仓库:`git init`
> 2. 添加所有文件到暂存区:`git add .` (后面跟文件名就是指定添加指定文件)
> 3. 提交到当前分支：`git commit -m "first commit" `（添加文件描述信息）
> 4. 链接远程仓库：`git remote add origin  https://github.com/xx/xx.git`
> 5. 把本地仓库的链接到远程仓库master分支：`git pull origin master`
> 6. 把本地仓库的文件推推送到远端master分支 `git push -u origin master`

### 1.首次使用

    git push -u origin <分支>

### 2.非首次

    git push --force origin <分支>

### 3.(clone)克隆远程仓库

1. ssh:`git clone git@github.com:user/branch.git` 
2. https:`git clone https://github.com/user/branch.git` 

> git clone默认会把远程仓库整个给clone下来,但只会在本地默认创建head指向的分支

#### 1.获取远程指定分支

    git clone -b <指定分支名> <远程仓库地址>

#### 2.获取其他分支

    git branch -a 列出所有分支
    git checkout -t origin/分支名

### 4.报错

#### 1

> error: failed to push some refs to 'git@github.com:远程库名.git' hint: Updates were rejected because the tip of your current branch is behind hint: its remote counterpart. Integrate the remote changes (e.g. hint: 'git pull ...') before pushing again. hint: See the 'Note about fast-forwards' in 'git push --help' for details.

> 错误:无法推动一些文件至“git@github.com:远程库名.” 提示:更新被拒绝，因为当前分支的在后面 提示:它的远程副本。集成远程更改 提示:‘git pull…’)，然后再次推。 提示:详见“git push -help”中的“关于快进的说明”。

> 1.将远程存储库中的更改合并到当前分支中 `git pull --rebase origin <分支>`

> 2.再执行同步`git push -u origin <分支>`

#### 2.

> fatal: refusing to merge unrelated histories
> 拒绝合并不相关的历史

### git命令解惑

1. `git pull origin master`

> `git pull origin <远端分支 a >:<本地分支 b>`意思是把远端的分支 a拉取到本地分支b，当前本地分支不是b也可以操作

2. `git pull origin <远端分支a>`

> 意思是把远端的分支a同步到当前本地分支，并自动合并。 git pull 意思本地已经和远端有了关联，同步当前分支最新内容。

3.`git push <远程主机名> <本地分支名>:<远程分支名>`
> git push origin master意思 把本地master分支推送到远端，如果远端有和master关联的分支，就推送到那个关联的分支，如果没有就创建一个远端master分支。 git push origin master:remote-test，意思就是把本地的 master分支 推送到远程的 remote-test分支，两个分支建立关联。

