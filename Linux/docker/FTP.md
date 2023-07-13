```shell

docker run -d \
-v /var/ftp:/home/vsftpd \
-p 20:20 -p 21:21 -p 21100-21110:21100-21110 \
-e FTP_USER=init -e FTP_PASS=753869 -e \
PASV_ADDRESS=192.254.8.88 -e \PASV_MIN_POST=21100 -e PASV_PORT=21110 \
-e reverse_lookup_enable=NO \
--name vsftpd \
--restart=always fauria/vsftpd



# 登录容器内
docker exec -it vsftpd bash 

# 如果需要创建新用户，需要将用户和密码接入到以下文件内，默认里面包含了Docker启动容器时候创建的用户名和密码
cat /etc/vsftpd/virtual_users.txt
marionxue
passwd

#假如我们添加了user用户，我们需要建立对应用户的文件夹
mkdir /home/vsftpd/user

#把登录的验证信息写入数据库 
/usr/bin/db_load -T -t hash -f /etc/vsftpd/virtual_users.txt /etc/vsftpd/virtual_users.db

#重启容器
docker restart vsftpd

#访问缓慢
reverse_lookup_enable=NO #/etc/vsftpd/vsftpd.conf   

清空 /etc/resolv.conf

```


```bash

/etc/vsftpd/vsftpd.conf
anonymous_enable=YES #允许匿名访问,如果为NO，ftp、anonymous帐户将无法访问！

local_enable=YES #启动home目录(默认),允许本地用户访问,允许用账号密码的方式登陆

write_enable=YES #f允许写的权限(默认),允许本地用户写入，此项设置yes后，设置匿名的读写/上传权限才有效。

local_umask=022 #上传后的文件的默认掩码

anon_upload_enable=YES #

anon_mkdir_write_enable=YES

dirmessage_enable=YES #允许为目录配置显示信息,显示每个目录下面的message_file文件的内容。

xferlog_enable=YES #开启日记功能。

connect_from_port_20=YES #使用标准的20端口来连接ftp。

chown_uploads=YES #所有匿名上传的文件的所属用户将会被更改成chown_username。

chown_username=whoever #匿名上传文件所属用户名，默认whoever。

xferlog_file=/var/log/xferlog #日志文件位置。

xferlog_std_format=YES #使用标准格式。

idle_session_timeout=600 #这个参数是指等待输入FTP指令的空闲时间（秒）。初次连上FTP服务后、或上一次FTP指令执行完成后，开始计时。相当于使用FTP客户端命令行工具时，出现输入提示符，等待用户输入的时间。这个时间超时，客户端的（一个TCP，命令）连接会被断开。

data_connection_timeout=120 #这个参数是指等待数据传输（上传/下载）的空闲时间（秒）。当FTP服务端每接收/或发送一次数据包(trans_chunk_size大小，默认值是8KB)，就会复位一次这个定时器。相当于使用FTP客户端命令行工具时，出现传输速率为0的持续时间。这个时间超时，客户端的（两个TCP，命令与数据）连接都会被断开。当 data_connection_timeout 定时器启动时，idle_session_timeout定时器会停止。即两个定时，同一时刻只有一个有效！

nopriv_user=ftpsecure #当服务器运行于最底层时使用的用户名。

async_abor_enable=YES #允许使用\”async ABOR\”命令,一般不用,容易出问题

ascii_upload_enable=YES #管控是否可用ASCII 模式上传。默认值为NO，FTP在传输数据时，可使用二进制（Binary）方式，也可使用ASCII模式来上传或下载数据。

ascii_download_enable=YES #管控是否可用ASCII 模式下载。默认值为NO

ftpd_banner=Welcome to blah FTP service. #使用FlashFXP登陆时会在下方信息处显示欢迎信息.如果设置了banner_file则此设置无效

deny_email_enable=YES #如果匿名用户需要密码,那么使用banned_email_file里面的电子邮件地址的用户不能登录

banned_email_file=/etc/vsftpd/banned_emails  #禁止使用匿名用户登陆时作为密码的电子邮件地址

chroot_local_user=YES

chroot_list_enable=YES #如果启动这项功能，则所有列在chroot_list_file中的使用者不能更改根目录。

chroot_list_file=/etc/vsftpd/chroot_list #定义不能更改用户主目录的文件。

ls_recurse_enable=YES #是否能使用ls -R命令以防止浪费大量的服务器资源

listen=NO  # 此条改为NO也行，默认NO

listen_ipv6=YES #默认开启，不能跟listen=YES 一起使用，注释掉。

pam_service_name=vsftpd #配置虚拟用户，权限验证需要的加密文件,#使用pam托管的账号,定义PAM 所使用的名称，预设为vsftpd

userlist_enable=YES #启动并指定开放的白名单用户列表，#配置yes+加userlist_deny=NO后，则只有user_list文件中的用户，才能访问FTP服务器。#若启用此选项,userlist_deny选项才有效。

tcp_wrappers=YES #开启tcp_wrappers支持

其它配置
pasv_enable=YES #使用被动模式连接，PAVS请求。

pasv_min_port=54301 #允许ftp工具访问的端口起止端口，大于1024即可。#pasv连接模式时可以使用port 范围的下界，0 表示任意。默认值为0。

pasv_max_port=54305 #被动模式所使用的端口范围。#pasv连接模式时可以使用port 范围的上界，0 表示任意。默认值为0。

pasv_address=47.101.172.63 #你的服务器IP!。

pasv_addr_resolve=YES

virtual_use_local_privs=YES #开启虚拟用户登陆功能！用户登录后操作目录和本地用户权限一样。

guest_enable=YES  #开启虚拟用户功能,#如果开启,那么所有非匿名登陆的用户名都会被切换成guest_username指定的用户名vsftpd 。

guest_username=vsftpd 　#指定虚拟用户登录后的宿主用户/系统用户/本地用户，默认为vsftpd ！任何非 anonymous 登入的账号，均会被假设成为 guest，访客在vsftpd当中，预设会取得ftp这个使用者的相关权限。但可以透过 guest_username 来修改为指定的vsftpd 帐户。使用虚拟用户登陆后，会跟这个系统用户具有相同的权限。

user_config_dir=/etc/vsftpd/virconf/  #虚拟用户主目录配置文件。

allow_writeable_chroot=YES #允许写入用户主目录，最新版的vsftpd为了安全必须用户主目录（也就是/home/vsftpuser/ftpuser），或者allow_writeable_chroot=YES

anon_root=/var/ftp #匿名用户默认主目录。

anon_world_readable_only=YES #允许匿名用户下载可阅读的文档

accept_timeout=60 #被动模式超时时间,#PAVS请求超时,客户端和服务器端面必须统一pavs模式。

userlist_file=/etc/vsftpd/user_list #白名单用户

userlist_deny=NO #若设置为YES，则user_list 文件中的用户将不允许访问FTP服务器；若设置为NO，则只有user_list文件中的用户，才能访问FTP服务器。

#不常用配置
no_anon_password=NO #允许匿名anonymous用户无密码登录时，不询问口令。当设置为YES时，表示anonymous将会略过密码检验步骤，而直接进入vsftpd服务器内。所以一般默认都是NO（登录时会检查输入的email）。

reverse_lookup_enable=NO #禁用反向域名解析，上传文件慢，解决ftp登录慢，  #vi /etc/hosts  将网段中的ip地址配进去即可，名字可以随便起，如 192.168.0.1     Linux1 ，重启系统生效。

anon_upload_enable=YES #允许匿名用户上传文件。只有在write_enable设置为YES时，该配置项才有效。而且匿名用户对相应的目录必须有写权限。

anon_mkdir_write_enable=YES #允许匿名用户创建目录。只有在write_enable设置为YES时有效。且匿名用户对上层目录有写入的权限。

anon_other_write_enable=NO #若设置为YES，则匿名用户会被允许拥有多于上传和建立目录的权限，还会拥有删除和更名权限。

ascii_upload_enable=YES

ascii_download_enable=YES

local_root=/home #控制所有非匿名用户登录vsftpd时进入的目录

ftp_username=ftp #定义匿名用户的账户名称，默认值为ftp。

nopriv_user=nobody #所有登陆的用户都作为nobody身份，更安全。

listen_port=21 #监听的端口#绑定到某个端口

ftp_data_port=2020 #数据传输端口。

pasv_promiscuous+NO #关闭安全检查。

port_enable=YES #允许使用port模式。

connect_timeout=60 #PROT模式连接超时。

prot_promiscuous #关闭安全检查。

local_max_rate=0 #限制用户的上传下载速度，0为不限制，单位： bytes/秒，#本地用户的传输比率(b/s)。

anon_max_rate=51200 #匿名用户的传输比率(b/s).

listen-address=92.18.76.29 # 绑定本机IP。#绑定到某个IP,其它IP不能访问。

max_clients=100 #可接受的最大client数目,连接数。

max_per_ip=5 #每个ip的最大client数目。

check_shell=YES #仅在没有pam验证版本时有用,是否检查用户有一个有效的shell来登录

chown_uploads=YES #所有匿名上传的文件的所属用户将会被更改成chown_username 

file_open_mode=0666 #上传文件的权限配合umask使用 。

banner_file=/etc/vsftpd/banner #定义登录信息文件的位置

message_file=.message #目录信息文件

secure_chroot_dir=/usr/share/empty #这个选项必须指定一个空的数据夹且任何登入者都不能有写入的权限，当vsftpd 不需要file system 的权限时，就会将使用者限制在此数据夹中。默认值为/usr/share/empty

log_ftp_protocol=NO #当xferlog_std_format关闭且本选项开启时,记录所有ftp请求和回复,当调试比较有用.

one_process_model #是否使用单进程模式

text_userdb_names=NO ##当使用者登入后使用ls -al 之类的指令查询该档案的管理权时，预设会出现拥有者的UID，而不是该档案拥有者的名称。若是希望出现拥有者的名称，则将此功能开启。

use_localtime=YES #显示目录清单时是用本地时间还是GMT时间,可以通过mdtm命令来达到一样的效果

use_sendfile=YES #测试平台优化

setproctitle_enable=YES #显示会话状态信息,关!



```