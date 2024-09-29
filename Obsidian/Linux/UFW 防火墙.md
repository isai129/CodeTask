防火墙是一个用来监视和过滤进出网络流量的工具。它通过定义一系列安全规则，来决定是否允许或者屏蔽指定的流量。

Ubuntu 自带的防火墙配置工具被称为 UFW (Uncomplicated Firewall)。UFW 是一个用来管理 iptables 防火墙规则的用户友好的前端工具。它的主要目的就是为了使得管理 iptables 更简单，就像名字所说的，简单的。

本文描述如何在 Ubuntu 20.04上使用 UFW 工具来配置和管理一个防火墙。一个被正确配置的防火墙是所有系统安全中最重要的部分。

## 一、前提条件

仅仅 root 或者其他有 sudo 权限的用户可以管理系统防火墙。最佳实践就是以 sudo 用户来运行管理员任务。

## 二、安装 UFW

UFW 是标准 Ubuntu 20.04 安装过程中的一部分，它应该已经在你的系统上存在。如果因为某些原因，它没有被安装，你可以通过输入下面的命令安装它：

```bash
sudo apt update
sudo apt install ufw
```

## 三、检查 UFW 的状态

安装过程不会自动激活防火墙，以避免服务器被锁住。你可以检查 UFW 的状态，输入：

```bash
sudo ufw status verbose
```

输出如下：

```bash
Status: inactive
```

如果 UFW 激活了，输入应该类似下面这样：

![](https://pic3.zhimg.com/80/v2-820802ccc5708f60154952460f9c429e_720w.webp)

## 四、UFW 默认策略

默认情况下，UFW 阻塞了所有进来的连接，并且允许所有出去的连接。这意味着任何人无法访问你的服务器，除非你打开端口。运行在服务器上的应用和服务可以访问外面的世界。

默认的策略定义在`/etc/default/ufw`文件中，并且可以通过使用`sudo ufw default <policy> <chain>`命令来修改。

防火墙策略是用来构建更多详细的和用户自定义的规则的基础。通常情况下，初始的默认策略是一个很好的起点。

## 五、应用配置

大部分应用都附带一份应用配置，它描述了服务，并且包含了 UFW 设置。这个规则在软件包安装的时候，被自动创建在`/etc/ufw/applications.d`目录下。

想要列举出你系统上所有的应用配置，输入：

```bash
sudo ufw app list
```

与你系统上安装的软件包有关系，输出应该看起来像下面这样：

```bash
Available applications:
  Nginx Full
  Nginx HTTP
  Nginx HTTPS
  OpenSSH
```

想要查找更多关于指定配置和包含规则的信息，使用下面的命令：

```bash
sudo ufw app info 'Nginx Full'
```

输出应该显示"Nginx Full"配置打开了端口"80"和"443”。

```bash
Profile: Nginx Full
Title: Web Server (Nginx, HTTP + HTTPS)
Description: Small, but very powerful and efficient web server

Ports:
  80,443/tcp
```

你也可以为你的应用创建自定义的配置。

## 六、启用 UFW

如果你在远程位置连接你的 Ubuntu，在启用 UFW 防火墙之前，你必须显式允许进来的 SSH 连接。否则，你将永远都无法连接到机器上。

现在 UFW 防火墙被配置允许 SSH 远程连接，启用它，输入：

```bash
sudo ufw allow ssh
```

输出：

```bash
Rules updated
Rules updated (v6)
```

如果 SSH 运行在非标准端口，你需要打开这个端口。

例如，如果你的 SSH 守护程序监听了`7722`，输入下面的命令，允许连接通过那个端口：

```bash
sudo ufw allow 7722/tcp
```

现在防火墙被配置允许进来的 SSH 连接，你可以输入下面的命令，启用它：

```bash
sudo ufw enable
```

输出如下：

```bash
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup
```

你将会被警告启用防火墙可能会中断现有的 SSH 连接，输入"y”，并且回车。

## 七、打开端口

取决于运行在你服务器上的应用，你需要根据服务打开不同的端口。

通用的打开端口的语法如下：

```bash
ufw allow port_number/protocol
```

下面是一些关于如何允许 HTTP 连接的方法。

第一个选项就是使用服务名。UFW 检查`/etc/services`文件，其中指定服务的端口和协议：

```bash
sudo ufw allow http
```

你也可以指定端口号和协议：

```bash
sudo ufw allow 80/tcp
```

当没有给出协议的时候，UFW 同时创建`tcp`和`udp`的规则。

另外一个选项就是使用应用程序配置。在这个例子中，是"Nginx HTTP”：

```bash
sudo ufw allow 'Nginx HTTP'
```

UFW 还支持另外一种语法，使用 `proto` 关键字来指定协议。

### 7.1 端口范围

UFW 允许你打开端口范围。使用分号分隔开端口的起点和终点，当你指定协议时，或者是 `tcp`，或者是`udp`。

例如，如果你想允许端口从`7100`到`7200`，同时支持`tcp`和`udp`，你将要运行下面的命令：

```bash
sudo ufw allow 7100:7200/tcp
sudo ufw allow 7100:7200/udp
```

### 7.2 允许指定 IP 地址访问指定端口

想要允许指定源 IP 的所有端口上的所有连接通过，使用`from`关键字，加上源地址。

这里是一个 IP 地址白名单的例子：

```bash
sudo ufw allow from 64.63.62.61
```

如果你指向允许给定 IP 访问指定的端口，使用`to any port`关键字加上端口号。

例如，允许从 IP`64.63.62.61`的机器，通过`22`端口访问,输入：

```bash
sudo ufw allow from 64.63.62.61 to any port 22
```

### 7.3 允许子网

允许一个子网 IP 地址的访问和允许一个单个 IP 地址的访问，命令是一样的。唯一的不同是需要指定网络掩码。

下面是一个例子，显示如何允许 IP 地址(192.168.1.1 到 192.168.1.254)，通过 3360(MySQL)，你可以使用这个命令：

```bash
sudo ufw allow from 192.168.1.0/24 to any port 3306
```

### 7.4 允许指定网络接口的连接

想要允许连接通过指定网络接口，使用`allow in on` 和 网络接口的名字：

```bash
sudo ufw allow in on eth2 to any port 3306
```

## 八、禁止连接

对于所有进来连接的默认的策略被设置为`deny`，如果你没有修改它，UFW 将会屏蔽所有进来的连接，除非你指定打开连接。

写禁止规则和写允许规则是一样的，你需要的仅仅是使用`deny`关键字替换`allow`。

比如说你打开了端口`80`和`443`，并且你的服务器处于来自`23.24.25.0/24`网络的攻击。想要禁止来自`23.24.25.0/24`的所有连接，使用下面的命令：

```bash
sudo ufw deny from 23.24.25.0/24
```

这里是一个例子，关于禁止从`23.24.25.0/24`对`80`和`443`端口的访问，你可以使用下面的命令：

```bash
sudo ufw deny proto tcp from 23.24.25.0/24 to any port 80,443
```

## 九、删除 UFW 规则

有两种不同的方式可以删除 UFW 规则。通过规则序号和通过指定的规则。

通过规则序号来删除 UFW 规则很简单，特别是你刚接触 UFW。

想要通过规则序号来删除，你需要找到你想删除的规则序号。想要这么做，运行下面的命令：

```bash
sudo ufw status numbered
```

输出：

```bash
Status: active

     To                         Action      From
     --                         ------      ----
[ 1] 22/tcp                     ALLOW IN    Anywhere
[ 2] 80/tcp                     ALLOW IN    Anywhere
[ 3] 8080/tcp                   ALLOW IN    Anywhere
```

想要删除规则，序号为3，这个规则允许对端口8080的连接，你可以使用下面的命令：

```bash
sudo ufw delete 3
```

删除规则的第二种方法就是指定实际的规则。例如，如果你添加过一个打开端口`8069`的规则，你可以通过下面的命令删除它：

```bash
sudo ufw delete allow 8069
```

## 十、禁用 UFW

如果因为任何原因，你需要停止 UFW，并且使得所有规则失效，你可以运行：

```bash
sudo ufw disable
```

稍后，如果你想重新启用 UFW，并且激活所有规则，输入：

```bash
sudo ufw enable
```

## 十一、重置 UFW

重置 UFW 将会禁用 UFW，删除所有激活的规则。如果你想撤销所有的应用规则，并且重新开始时，这个很有用。

想要重置 UFW，简单输入下面的命令:

```bash
sudo ufw reset
```

## 十二、IP 伪装

IP 伪装是一种在 Linux内核中的 NAT（网络地址转换），它通过重写源 IP 和目标 IP 的地址和端口，来转换网络流量。使用 IP 伪装技术，你可以允许局域网中的一台或者多台机器，和互联网进行交互，其中的一台 Linux 机器扮演网关。

使用 UFW 配置 IP 伪装需要几个步骤：

首先，你需要启用 IP 转发。想要这么做，打开`/etc/ufw/sysctl.conf`文件：

```bash
sudo nano /etc/ufw/sysctl.conf
```

查找并且取消这一行的注释`net.ipv4.ip_forward = 0`:

```bash
net/ipv4/ip_forward=1
```

下一步，你需要配置 UFW 来允许转发包。打开 UFW 配置文件：

```bash
sudo nano /etc/default/ufw
```

定位到`DEFAULT_FORWARD_POLICY`处，修改值从`DROP`到`ACCEPT`：

```bash
DEFAULT_FORWARD_POLICY="ACCEPT"
```

现在你需要设置在`nat`表和伪装规则中默认的`POSTROUTING`策略。想要这么做，打开`/etc/ufw/before.rules`文件，并且附加下面的行进去，像下面这样：

```bash
sudo nano /etc/ufw/before.rules
```

附加下面的行：

```bash
[[NAT]] table rules
*nat
:POSTROUTING ACCEPT [0:0]

# Forward traffic through eth0 - Change to public network interface
-A POSTROUTING -s 10.8.0.0/16 -o eth0 -j MASQUERADE

# don't delete the 'COMMIT' line or these rules won't be processed
COMMIT
```

不要忘记将`-A POSTROUTING`一行中的`eth0`替换成你的公开网络接口的名字：

当你做完这些，保存，并且关闭文件。

最后，通过禁用，重新启用 UFW，重载 UFW 规则。

```bash
sudo ufw disable
sudo ufw enable
```