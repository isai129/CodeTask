我们将在**/etc/profile.d/proxy.sh**下添加一个shell脚本文件。这将确保设置适用于所有登录的用户。

```undefined
sudo vim /etc/profile.d/proxy.sh
```

填充您的代理值。

```powershell
# set proxy config via profie.d - should apply for all users
# 
export http_proxy="http://127.0.0.1:7890/"
export https_proxy="http://10.10.1.10:7890/"
export no_proxy="127.0.0.1,localhost"

# For curl
export HTTP_PROXY="http://127.0.0.1:7890/"
export HTTPS_PROXY="http://127.0.0.1:7890/"
export NO_PROXY="127.0.0.1,localhost"
```

将要从代理中排除的其他 IP 添加到 NO_PROXY 和 no_proxy 环境变量。

使其可执行。

```undefined
sudo chmod +x  /etc/profile.d/proxy.sh
```

获取文件以开始使用代理设置，或者注销并重新登录。

```undefined
source /etc/profile.d/proxy.sh
```

确认 ：

```powershell
$ env | grep -i proxy
```

## 为 APT 包管理器设置代理

上述设置适用于应用程序和命令行工具。如果您只想为 APT 包管理器设置代理，请按如下所示进行配置。

```powershell
$ sudo vim /etc/apt/apt.conf.d/80proxy
Acquire::http::proxy "http://127.0.0.1:7890/";
Acquire::https::proxy "https://127.0.0.1:7890/";
```

如果需要认证，则这样设置。

```xml
Acquire::http::proxy "http://<username>:<password>@<proxy>:<port>/";
Acquire::https::proxy "https://<username>:<password>@<proxy>:<port>/";
Acquire::ftp::proxy "ftp://<username>:<password>@<proxy>:<port>/";
```

## 仅为 wget 设置代理

要设置与 wget 命令一起使用的代理设置，请将它们添加到 **~/.wgetrc** 文件中。

```powershell
$ vim ~/.wgetrc                           
use_proxy = on
http_proxy = http://127.0.0.1:7890/ 
https_proxy = http://127.0.0.1:7890/ 
```