## 参数[¶](https://docs.linuxserver.io/images/docker-jellyfin/#parameters "永久链接")

容器是使用运行时传递的参数（例如上面的参数）进行配置的。这些参数用冒号分隔并`<external>:<internal>`分别表示。例如，`-p 8080:80`将公开`80`容器内部的端口，以便可以从容器外部端口上的主机 IP 进行访问`8080`。

### 端口 ( `-p`)[¶](https://docs.linuxserver.io/images/docker-jellyfin/#ports-p "永久链接")

|范围|功能|
|---|---|
|`8096`|HTTP 网络用户界面。|
|`8920`|可选 - https webUI（您需要设置自己的证书）。|
|`7359/udp`|可选 - 允许客户端发现本地网络上的 Jellyfin。|
|`1900/udp`|可选 - DNLA 和客户端使用的服务发现。|

### 环境变量 （`-e`）[¶](https://docs.linuxserver.io/images/docker-jellyfin/#environment-variables-e "永久链接")

|环境|功能|
|---|---|
|`PUID=1000`|对于 UserID - 请参阅下面的说明|
|`PGID=1000`|对于 GroupID - 请参阅下面的说明|
|`TZ=Etc/UTC`|指定要使用的时区，请参阅此[列表](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List)。|
|`JELLYFIN_PublishedServerUrl=192.168.0.5`|设置自动发现响应域或IP地址。|

### 体积映射 ( `-v`)[¶](https://docs.linuxserver.io/images/docker-jellyfin/#volume-mappings-v "永久链接")

| 体积              | 功能                                             |
| --------------- | ---------------------------------------------- |
| `/config`       | Jellyfin 数据存储位置。_这可能会变得非常大，对于大型集合来说可能超过 50GB。_ |
| `/data/movies`  | 媒体去这里。根据需要添加任意数量，例如`/data/movies`、`/data/tv`等。 |
| `/data/tvshows` | 媒体去这里。根据需要添加任意数量，例如`/data/movies`、`/data/tv`等。 |

#### 杂项选项[¶](https://docs.linuxserver.io/images/docker-jellyfin/#miscellaneous-options "永久链接")

|范围|功能|
|---|---|
|||

## 文件中的环境变量（Docker 秘密）[¶](https://docs.linuxserver.io/images/docker-jellyfin/#environment-variables-from-files-docker-secrets "永久链接")

您可以使用特殊的 prepend 从文件中设置任何环境变量`FILE__`。

举个例子：

`[](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-4-1)-e FILE__MYVAR=/run/secrets/mysecretvariable`

`MYVAR`将根据文件的内容设置环境变量`/run/secrets/mysecretvariable`。

## 用于运行应用程序的 Umask[¶](https://docs.linuxserver.io/images/docker-jellyfin/#umask-for-running-applications "永久链接")

对于我们的所有镜像，我们提供了使用可选设置覆盖容器内启动的服务的默认 umask 设置的功能`-e UMASK=022`。请记住，umask 不是 chmod，它根据它不添加的值从权限中减去。在寻求支持之前，请先阅读[此处。](https://en.wikipedia.org/wiki/Umask)

## 可选参数[¶](https://docs.linuxserver.io/images/docker-jellyfin/#optional-parameters "永久链接")

[端口的官方文档](https://jellyfin.org/docs/general/networking/index.html)提供了可以提供自动发现的其他端口。

服务发现 ( `1900/udp`) - 由于如果此选项可配置，客户端自动发现将会中断，因此您目前无法在设置中更改此设置。DLNA 也使用此端口，并且需要位于本地子网中。

客户端发现 ( `7359/udp`) - 允许客户端发现本地网络上的 Jellyfin。发送到此端口的广播消息，内容为“谁是 Jellyfin 服务器？” 将获得一个 JSON 响应，其中包括服务器地址、ID 和名称。

  `[](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-5-1)  -p 7359:7359/udp \  [](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-5-2)  -p 1900:1900/udp \`

[环境的官方文档](https://jellyfin.org/docs/general/administration/configuration.html)有额外的环境，可以提供额外的可配置性，例如迁移到本机 Jellyfin 映像。

## 用户/组标识符[¶](https://docs.linuxserver.io/images/docker-jellyfin/#user-group-identifiers "永久链接")

使用卷（`-v`标志）时，主机操作系统和容器之间可能会出现权限问题，我们通过允许您指定用户`PUID`和组来避免此问题`PGID`。

确保主机上的所有卷目录都属于您指定的同一用户，并且任何权限问题都会像魔术一样消失。

在这种情况`PUID=1000`下`PGID=1000`，要找到您的使用方式，`id your_user`如下所示：

`[](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-6-1)id your_user`

输出示例：

`[](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-7-1)uid=1000(your_user) gid=1000(your_user) groups=1000(your_user)`

## Docker 模组[¶](https://docs.linuxserver.io/images/docker-jellyfin/#docker-mods "永久链接")

[![Docker 模组](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=jellyfin&query=%24.mods%5B%27jellyfin%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=jellyfin "查看此容器的可用模组。") [![Docker 通用模组](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "查看可用的通用模组。")

我们发布了各种[Docker Mod](https://github.com/linuxserver/docker-mods)以在容器内启用附加功能。可通过上面的动态徽章访问该图像可用的 Mod 列表（如果有）以及可应用于我们任何一个图像的通用 Mod。

## 支持信息[¶](https://docs.linuxserver.io/images/docker-jellyfin/#support-info "永久链接")

- 容器运行时的 shell 访问：
    
    `[](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-8-1)docker exec -it jellyfin /bin/bash`
    
- 实时监控容器的日志：
    
    `[](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-9-1)docker logs -f jellyfin`
    
- 容器版本号：
    
    `[](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-10-1)docker inspect -f '{{ index .Config.Labels "build_version" }}' jellyfin`
    
- 图片版本号：
    
    `[](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-11-1)docker inspect -f '{{ index .Config.Labels "build_version" }}' lscr.io/linuxserver/jellyfin:latest`
    

## 更新信息[¶](https://docs.linuxserver.io/images/docker-jellyfin/#updating-info "永久链接")

我们的大多数图像都是静态的、版本化的，并且需要图像更新和容器重新创建来更新内部的应用程序。除了一些例外（即 nextcloud、plex），我们不建议或支持更新容器内的应用程序。请参阅上面的[“应用程序设置”](https://docs.linuxserver.io/images/docker-jellyfin/#application-setup)部分，了解是否建议将其用于图像。

以下是更新容器的说明：

### 通过 Docker 撰写[¶](https://docs.linuxserver.io/images/docker-jellyfin/#via-docker-compose "永久链接")

- 更新图片：
    
    - 所有图像：
        
        `[](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-12-1)docker-compose pull`
        
    - 单张图像：
        
        `[](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-13-1)docker-compose pull jellyfin`
        
- 更新容器：
    
    - 所有容器：
        
        `[](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-14-1)docker-compose up -d`
        
    - 单个容器：
        
        `[](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-15-1)docker-compose up -d jellyfin`
        
- 您还可以删除旧的悬空图像：
    
    `[](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-16-1)docker image prune`
    

### 通过 Docker 运行[¶](https://docs.linuxserver.io/images/docker-jellyfin/#via-docker-run "永久链接")

- 更新图像：
    
    `[](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-17-1)docker pull lscr.io/linuxserver/jellyfin:latest`
    
- 停止正在运行的容器：
    
    `[](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-18-1)docker stop jellyfin`
    
- 删除容器：
    
    `[](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-19-1)docker rm jellyfin`
    
- 按照上面的说明，使用相同的 docker 运行参数重新创建一个新容器（如果正确映射到主机文件夹，您的`/config`文件夹和设置将被保留）
    
- 您还可以删除旧的悬空图像：
    
    `[](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-20-1)docker image prune`
    

### 通过 Watchtower 自动更新程序（仅在您不记得原始参数时使用）[¶](https://docs.linuxserver.io/images/docker-jellyfin/#via-watchtower-auto-updater-only-use-if-you-dont-remember-the-original-parameters "永久链接")

- 在其标签处拉取最新镜像，并在一次运行中将其替换为相同的环境变量：
    
    `[](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-21-1)docker run --rm \   [](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-21-2)  -v /var/run/docker.sock:/var/run/docker.sock \  [](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-21-3)  containrrr/watchtower \  [](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-21-4)  --run-once jellyfin`
    
- 您还可以删除旧的悬空图像：`docker image prune`
    

警告

我们不认可使用 Watchtower 作为现有 Docker 容器自动更新的解决方案。事实上，我们通常不鼓励自动更新。然而，这是一个有用的工具，可以在您忘记原始参数的情况下一次性手动更新容器。从长远来看，我们强烈建议使用[Docker Compose](https://docs.linuxserver.io/general/docker-compose)。

### 镜像更新通知 - Diun（Docker 镜像更新通知程序）[¶](https://docs.linuxserver.io/images/docker-jellyfin/#image-update-notifications-diun-docker-image-update-notifier "永久链接")

提示

我们推荐[Diun](https://crazymax.dev/diun/)来获取更新通知。不推荐也不支持其他在无人值守的情况下自动更新容器的工具。

## 本地建设[¶](https://docs.linuxserver.io/images/docker-jellyfin/#building-locally "永久链接")

如果您想出于开发目的或只是为了自定义逻辑而对这些图像进行本地修改：

`[](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-22-1)git clone https://github.com/linuxserver/docker-jellyfin.git [](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-22-2)cd docker-jellyfin [](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-22-3)docker build \   [](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-22-4)  --no-cache \  [](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-22-5)  --pull \  [](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-22-6)  -t lscr.io/linuxserver/jellyfin:latest .`

ARM 变体可以使用以下命令在 x86_64 硬件上构建`multiarch/qemu-user-static`

`[](https://docs.linuxserver.io/images/docker-jellyfin/#__codelineno-23-1)docker run --rm --privileged multiarch/qemu-user-static:register --reset`

注册后，您可以定义要与`-f Dockerfile.aarch64`.


```yaml
---
version: "3.5"
services:
  jellyfin:
    image: lscr.io/linuxserver/jellyfin:latest
    container_name: media-jellyfin
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Asia/Shanghai
      - DOCKER_MODS=linuxserver/mods:jellyfin-opencl-intel
    volumes:
      - /share/apps/jellyfin:/config
      - /share/apps/jellyfin/scripts:/custom-cont-init.d
      - /path/to/library:/config
      - /path/to/tvseries:/data/tvshows
      - /path/to/movies:/data/movies
    network_mode: 'host'
    ports:
      - 8096:8096
      - 8920:8920 [[optional]]
      - 7360:7359/udp [[optional]]
      - 1900:1900/udp [[optional]]
    devices:
      - /dev/dri:/dev/dri [[optional]]
    restart: unless-stop

```