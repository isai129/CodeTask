
**第一步：在 Ubuntu 中安装 VSFTPD 服务器**

```bash
sudo apt-get install vsftpd
# 一旦安装完成，初始情况下服务被禁用。因此，我们需要手动开启服务，同时，启动它使得在下次开机时能够自动开启服务：
systemctl enable vsftpd
systemctl start vsftpd
```


启动：

```bash
#查看其运行状态
systemctl  status vsftpd
#重启服务
systemctl  restart vsftpd
```

ftp用户：（需要主动创建）

```bash
sudo useradd -d /home/ftp/ftp_root -m ftpadmin
sudo passwd ftpadmin
#输入密码：Ft159263
再次输入密码：
chmod -R 777 /home/ftp/ftp_root
```

修改配置文件：

```bash
#修改配置
sudo vim /etc/vsftpd.conf
```

```bash
#Standalone mode
listen=YES
#设置为YES时vsftpd以独立运行方式启动，设置为NO时以xinetd方式启动（xinetd是管理守护进程的，将服务集中管理，可以减少大量服务.
max_clients=200
#在独立启动时限制服务器的连接数，0表示无限制
max_per_ip=0
#在独立启动时限制客户机每IP的连接数，0表示无限制
#Access rights
anonymous_enable=YES
#设置是否支持匿名用户访问
local_enable=YES
#置是否支持本地用户帐号访问
write_enable=NO
#否开放本地用户的写权限
anon_upload_enable=NO
#设置是否允许匿名用户上传
anon_mkdir_write_enable=NO
#置是否允许匿名用户创建目录
anon_other_write_enable=NO
#设置是否允许匿名用户其他的写权限(安全上比较重要，一般不建议开，不过关闭会不支持续传)
#Security
dirmessage_enable=YES
#允许为目录配置显示信息,显示每个目录下面的message_file文件的内容
use_localtime=YES
#vsftpd使用本机时间作为vsftpd时间
anon_world_readable_only=YES
#如果设为YES，则允许匿名登入者下载可阅读的文件
connect_from_port_20=YES
#指定FTP使用20端口进行数据传输
hide_ids=YES
#当设置为”yes“时，不显示ftp服务器的文件系统id（或名字），一律显示为：ftp text_userdb_names
#：为了性能，只显示id，而不显示对应的实际用户名字。
pasv_min_port=50000
#在PASV工作模式下，数据连接可以使用的端口范围的最小端口，0 表示任意端口；
pasv_max_port=60000
#在PASV工作模式下，数据连接可以使用的端口范围的最大端口，0 表示任意端口；

```

最后添加：
```bash
userlist_deny=NO
userlist_enable=YES
userlist_file=/etc/vsftpd.allowed_users
vim /etc/vsftpd.chroot_list
#输入ftpadmin后保存退出
 
#重启服务
systemctl start vsftpd
```

直接输入ftp localhost进行测试

![[Pasted image 20231128121032.png]]


配置 VSFTPD 

基于用户列表文件`/etc/vsftpd.userlist` 来允许或拒绝用户访问 FTP。

在默认情况下，如果通过`userlist_enable=YES `启用了用户列表，且设置`userlist_deny=YES` 时，那么，用户列表文件`/etc/vsftpd.userlist` 中的用户是不能登录访问的。

但是，选项`userlist_deny=NO` 则反转了默认设置，这种情况下只有用户名被明确列出在`/etc/vsftpd.userlist `中的用户才允许登录到 FTP 服务器。

```bash
userlist_enable=YES                   # vsftpd 将会从所给的用户列表文件中加载用户名字列表
userlist_file=/etc/vsftpd.userlist    # 存储用户名字的列表
userlist_deny=NO
```

当用户登录 FTP 服务器以后，他们将进入 `chrooted` 环境，即当在 FTP 会话时，其 root 目录将是其 home 目录。

将 FTP 用户限制在其 home 目录
```bash
chroot_local_user=YES
allow_writeable_chroot=YES
```

选项`chroot_local_user=YES` 意味着本地用户将进入 chroot 环境，当登录以后默认情况下是其 home 目录。
默认情况下，出于安全原因，VSFTPD 不允许 chroot 目录具有可写权限。然而，我们可以通过选项 `allow_writeable_chroot=YES` 来改变这个设置

重启VSFTPD 服务
```bash
systemctl restart vsftpd
```

