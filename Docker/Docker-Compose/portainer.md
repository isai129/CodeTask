```BASH
version: '3.9'
services:
  # 基础环境组件
  # 1.Portainer
  portainer:
    image: portainer/portainer-ce:latest
    container_name: portainer
    command: -H unix:///var/run/docker.sock
    restart: unless-stopped
    deploy:
      resources:
        limits:
          cpus: '0.50'
          memory: 800M
        reservations:
          cpus: '0.1'
          memory: 256M
    network_mode: 'host'
      #ports:
      #- "9999:9000"
      #- "8000:8000"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock #数据文件挂载
      - portainer_data:/data portainer/portainer-ce #配置文件挂载
    environment:
      - HTTP_PROXY=http://127.0.0.1:7890
      - HTTPS_PROXY=http://127.0.0.1:7890
      - NO_PROXY=localhost,127.0.0.1,.example.com"
# 存储卷
volumes:
  portainer_data:
~                                
```