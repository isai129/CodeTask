静态地址

1.系统版本

`lsb_release -a

2.修改 `/etc/netplan` 的配置文件

备份 ：

```bash
sudo cp /etc/netplan/00-installer-config.yaml /etc/netplan/00-installer-config.yaml.original
```

修改:`00-installer-config.yaml

```bash
# This is the network config written by 'subiquity'
network:
  ethernets:
    eno1:
      dhcp4: false
      addresses:
        - 192.168.12.100/24
      routes:
        - to: default
          via: 192.168.12.1
      nameservers:
        addresses: [114.114.114.114,192.18.12.1]
  version: 2

```

在上面的文件中，我们使用了以下内容：

- eno1：接口名称
- addresses：用来设置静态IP
- nameservers：用来设置 DNS server
- routes： 用来设置网关

**注意:** 根据环境更改 IP 详细信息和接口名称。

要使上述更改生效，请使用以下 netplan 命令应用这些更改

```bash
$ sudo netplan apply
```

执行以下命令，查看接口的 ip 地址

```bash
$ ip addr show ens33
```

执行以下命令，查看缺省路由

```bash
$ ip route show
```





