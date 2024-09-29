```bash
# version: "3.8"
services:
  alist:
    image: xhofe/alist:latest
    container_name: alist
    volumes:
        - '/etc/alist:/opt/alist/data'
        - /stat:/stat
        - /opt/alist/data/temp/aria2:/opt/alist/data/temp/aria2
        - /opt/alist/data/temp/qbittorrent:/opt/alist/data/temp/qbittorrent
    ports:
        - '5244:5244'
    environment:
        - PUID=1000
        - PGID=1000
        - UMASK=0122
    restart: always
  Aria2-Pro:
    container_name: aria2-pro
    image: p3terx/aria2-pro
    environment:
      - PUID=1000
      - PGID=1000
      - UMASK_SET=0122
      - RPC_SECRET=2161023252
      - RPC_PORT=6800
      - LISTEN_PORT=6888
      - DISK_CACHE=64M
      - IPV6_MODE=false
      - UPDATE_TRACKERS=true
      - CUSTOM_TRACKER_URL=
      - TZ=Asia/Shanghai
    volumes:
      - ${PWD}/aria2/config:/config
      - ${PWD}/aria2/downloads:/stat/aria2/downloads
    ports:
      - "6800:6800"
      - "6888:6888"
      - "6888:6888/udp"
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: 1m
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

```