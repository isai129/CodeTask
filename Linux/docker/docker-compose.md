

**‍一、docker-compose简介**

docker-compose是docker提供的一个命令行工具，用来定义和运行由多个容器组成的应用。

为什么需要docker-compose？

一般我们一个完整的应用部署包括几个服务：Web应用、[MySQL](https://cloud.tencent.com/product/cdb?from_column=20065&from=20065)服务、[Redis](https://cloud.tencent.com/product/crs?from_column=20065&from=20065)服务，有的可能用到Kafka服务、Prometheus服务等等。

那么如何管理这么多服务呢？我们就需要docker-compose来帮我们实现批量管理[容器服务](https://cloud.tencent.com/product/tke?from_column=20065&from=20065)。

接下来我们来看看docker-compose是如何批量管理容器服务的？这就说道docker-compose.yml了。

docker-compose.yml可以同时管理多个container，包括他们之间的关系、使用已存在的image还是自己build新的镜像 、各种网络端口定义、储存空间定义等。

然后我们可以用docker compose up -d完成应用所有容器的创建和启动。

ok，重点来了，我们来看看如何使用docker compose吧。

使用dockercompose 基本上分为三步：

1.使用Dockerfile定义镜像；

2.使用docker-compose.yml定义组成的应用程序的服务；

3.运行docker compose up启动并运行程序；

**总结：dockerfile记录单个镜像的构建过程， docker-compse.yml记录一个项目（一般是多个镜像）的构建过程。**

**二、docker-compose.yml详解**

一份标准配置文件应该包含 version、services、networks 三大部分，其中最关键的就是 services 和 networks 两个部分。

1.version：docker-compose 文件版本，可在https://docs.docker.com/compose/compose-file/compose-versioning/ 查看docker-compose文件版本支持特定的 Docker 版本。

2.services：服务名称，自定义。

3.networks：定义网络。实现了网络隔离。

**三、docker-compose.yml的demo**

以下定义了docker-compose-demo和 docker-compose-mysql-demo两个容器，相关指令解释可查看后面的注释。

```javascript
version : '3'                                      #compose文件版本支持特定的Docker版本
services:                                          #本工程的服务配置列表
 
  docker-compose-demo:                             #服务名，自定义
    container_name: docker-compose-container-demo  #容器名

    build:                                         #基于Dockerfile文件构建镜像时使用的属性
      context: .                                   #代表当前目录，也可以指定绝对路径[/path/test/Dockerfile]或相对路径[../test/Dockerfile]，尽量放在当前目录，便于管理
      dockerfile: Dockerfile-demo                  #指定Dockerfile文件名
    ports:                                         
      - "5555:6666"                                #指定宿主机端口映射到本容器的端口
    volumes:                                        
      - .:/tmp                        
             #目录挂载
    depends_on:                                    #本服务启动，依赖于mysql，也就是mysql优先于docker-compose-demo启动
      - mysql

    restart: always                                #是否随docker服务启动重启
    networks:                                      #加入指定网络
      - my-network                                 #自定义的网络名
    environment:                                   #设置容器的环境变量
      - TZ=Asia/Shanghai                           #这里设置容器的时区为亚洲上海，也就解决了容器通过compose编排启动的时区问题
 
  mysql:                                           #服务名，自定义
    container_name: docker-compose-mysql-demo      #容器名
    image: mysql:5.7                               #指定基于mysql:5.7镜像为基础镜像来构建镜像。ports:
      - "33061:3306"
    command: [                                           #使用command可以覆盖容器启动后默认执行的命令
            '--character-set-server=utf8mb4',            #设置数据库表的数据集
            '--collation-server=utf8mb4_unicode_ci',     #设置数据库表的数据集
            '--default-time-zone=+8:00'                  #设置mysql数据库的时区问题
    ]
    environment:           
      MYSQL_DATABASE: swapping                            #设置初始的数据库名
      MYSQL_ROOT_PASSWORD: 398023                         #设置root连接密码
      MYSQL_ROOT_HOST: '%'
    restart: always
    networks:
      - my-network
networks:                        
  my-network:                                             #自定义的网络
```

 

**docker-compose常用命令**

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



**五、总结**

以上就是docker-compose的基本使用方式了。

回想起第一次接触docker-compose的时候，因为当时测试的一个服务需要再加一个容器，使用docker-compose up后面没有加 -d，导致关闭xshell就不能使用了，也是那时候开始对Docker这块内容有了更进一步的认知。