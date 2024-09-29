```bash

error from daemon in stream: Error grabbing logs: invalid character '\x00' looking for beginning of value

# docker inspect 容器id  [[查看镜像的元数据]]
initial@HP-EliteDesk:~$ docker inspect --format ='{{.LogPath}}' clash
=/var/lib/docker/containers/d6493f256086606aceff3f5e787c0e9322117ebb04ceded6411e4412f07b4eef/d6493f256086606aceff3f5e787c0e9322117ebb04ceded6411e4412f07b4eef-json.log

sudo rm -rf /var/lib/docker/containers/d6493f256086606aceff3f5e787c0e9322117ebb04ceded6411e4412f07b4eef/d6493f256086606aceff3f5e787c0e9322117ebb04ceded6411e4412f07b4eef-json.log



```