> - [Alist](https://alist-doc.nn.ci/docs/intro/) 是一个可将多种网盘挂载成 [WebDAV](http://www.webdav.org/) 的 Web 应用。
> - 它可以使用 Docker 进行快速部署，并可对接 Aria Pro 组成一个网盘下载器。
> - 特别适用于部署在 NAS 上用来下载网盘上的文件。
> 

![concept](https://github.com/ShinChven/alist-aria2-pro-docker-compose/raw/master/alist+aria2-pro.drawio.svg)

## 使用 Docker Compose 部署

Alist 有官方的 Docker [镜像](https://hub.docker.com/r/xhofe/alist/)和[部署文档](https://alist-doc.nn.ci/docs/install/docker)。但我更倾向于使用 Docker Compose 来管理部署，这样可以将它和`Aria2 Pro`或其他应用一起部署。

### 前置工作

- 你的服务器、主机上需要安装 [Docker](https://docs.docker.com/engine/install/) 和 [Docker Compose](https://docs.docker.com/compose/)。
- 请熟悉 Docker 中的 [volume](https://docs.docker.com/storage/volumes/) 和 [network](https://docs.docker.com/network/)。

### 编写 docker-compose.yml

- 创建一个部署工程文件夹，并编写一个`docker-compose.yml`文件，并参`environment`和`volumes`节点中照注释（`#`）进行配置。
- `${PWD}`指代当前目录，默认配置会将程序产生的数据保存在这个文件中，如果你想将数据保存在其他位置，可以修改`volumes`配置（:号前为主机上的目录，后为容器内的目录）。

内容如下：


```bash
 # version: "3.8"
services:
  # Alist 的官方部署文档: https://alist-doc.nn.ci/en/docs/install/docker/
  alist:
    image: xhofe/alist:latest
    container_name: alist
    volumes:
        - '/etc/alist:/opt/alist/data'
        - /stat:/stat
    ports:
        - '5244:5244'
    environment:
        - PUID=1000
        - PGID=1000
        - UMASK=0122
    restart: always


  # Aria2 Pro 的官方部署文档: https://github.com/P3TERX/Aria2-Pro-Docker/blob/master/docker-compose.yml
  Aria2-Pro:
    container_name: aria2-pro
    image: p3terx/aria2-pro
    environment:
      - PUID=1000
      - PGID=1000
      - UMASK_SET=0122
      - RPC_SECRET=REPLACE_WITH_YOUR_OWN_ARIA2_RPC_SECRET # 配置Aria2 的 RPC secret 密钥，它将被用于 Alist 和 AriaNg 连接 Aria2
      - RPC_PORT=6800
      - LISTEN_PORT=6888
      - DISK_CACHE=64M
      - IPV6_MODE=false
      - UPDATE_TRACKERS=true
      - CUSTOM_TRACKER_URL=
      - TZ=Asia/Shanghai
    volumes:
      - ${PWD}/aria2/config:/config
      - ${PWD}/aria2/downloads:/downloads # 在:号前配置你要在主机上保存下载文件的路径
    ports:
      - "6800:6800"
      - "6888:6888"
      - "6888:6888/udp"
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 1m
  # Aria2 的 Web UI
  AriaNg:
    container_name: ariang
    image: p3terx/ariang
    command: --port 6880 --ipv6
    ports:
      - "6880:6880"
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 1m

~                          
```


### 部署并启动

- 在部署工程文件夹中，执行`docker-compose up -d`命令，就能完成部署了。
- 程序成功部署完毕 🥳

## 设置

在使用之前，还得设置一下 Alist 和 Aria2 Pro，让它们能互相连通。

### IP 地址与端口

这两个程序组合使用的时候，最好不要用`localhost`或`127.0.0.1`来访问，否则两者之间的连接会出现问题，请使用主机的局域网IP来访问。

以下是各种应用的访问端口，请将`${IP}`替换成你docker主机的IP地址：

| APP | URL |
| --- | --- |
| Alist | http://${IP\_ADDRESS}:5244 |
| Aria2 RPC | http://${IP\_ADDRESS}:6800 |
| AriaNg | http://${IP\_ADDRESS}:6880 |

### 配置和管理 Alist

- 在配置 Alist 之前需要，需要先取到 Alist 的`初始管理密码`，可以通过以下命令获取：

bash

Wrap|Copy

`docker exec -it alist ./alist -password` 

- 取到密码后，打开浏览器，访问`http://${IP_ADDRESS}:5244`，找到并进入管理入口并输入`初始管理密码`，即可进入 Alist 的管理界面。

### Alist 连接 Aria2 Pro

- 请在`Alist`的设置界面中找到`后端设置`中找到 Aria2 RPC 设置。
- 在`Aria2 RPC url`中填入`Aria2 RPC`的地址，即`http://${IP_ADDRESS}:6800/jsonrpc`
- 填入`Aria2 RPC`的`RPC secret`，即`docker-compose.yml`文件中`Aria2-Pro`服务的`environment`\-`RPC_SECRET`，默认为`REPLACE_WITH_YOUR_OWN_ARIA2_RPC_SECRET`。

### 挂载网盘

- 在`Alist`的设置界面中找到[添加账号](https://alist-doc.nn.ci/docs/driver/base)，以挂载网盘。

### 通过 AriaNg 查看和管理 Aria2 的下载任务

AriaNg 是 Aria2 的 Web UI，需要配置 Aria2 的 RPC 地址和 RPC 密钥，才能正常使用。

- 从浏览器中访问`http://${IP_ADDRESS}:6880/#!/settings/ariang`。
- 在`Aria2 RPC Secret`中设置你的`RPC_SECRET`，即`docker-compose.yml`文件中`Aria2-Pro`服务的`environment`\-`RPC_SECRET`，默认为`REPLACE_WITH_YOUR_OWN_ARIA2_RPC_SECRET`。
- 点击弹出的`重载`按钮便能完成配置。