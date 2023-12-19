
docker compose

`compose.yml`

```powershell
docker pull ghcr.nju.edu.cn/home-assistant/home-assistant:stable
# 将ghcr.io替换为ghcr.nju.edu.cn```
```

```yaml
version: '3'
services:
  homeassistant:
    container_name: homeassistant
    image: "ghcr.nju.edu.cn/home-assistant/home-assistant:stable"
    volumes:
      - /PATH_TO_YOUR_CONFIG:/config
      - /etc/localtime:/etc/localtime:ro
      - /run/dbus:/run/dbus:ro
    restart: unless-stopped
    privileged: true
    network_mode: host
    devices:
     - /dev/ttyUSB0:/dev/ttyUSB0
    environment:
     - DISABLE_JEMALLOC: true
```



```
UFW放行8123端口：

```bash
sudo ufw allow 8123/tcp
```

一旦 Home Assistant 容器运行，Home Assistant 就应该可以使用`http://<host>:8123`（替换与系统的主机名或 IP）。
