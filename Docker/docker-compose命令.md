
```javascript
#启动
docker-compose -f /data/docker-compose/docker-compose.yml up -d  

#ps：列出所有运行容器
docker-compose ps

#logs：查看服务日志输出
docker-compose logs

#build：构建或者重新构建服务
docker-compose build

#start：启动指定服务已存在的容器
docker-compose start docker-compose-demo

#stop：停止已运行的服务的容器
docker-compose stop docker-compose-demo

#rm：删除指定服务的容器
docker-compose rm docker-compose-demo

#up：构建、启动容器
docker-compose up

#-d：后台运行
docker-compose up -d

#stop：停止容器
docker-compose stop

```