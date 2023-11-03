
### 1、更新用Docker命令部署的应用

#### 第一步

利用`docker ps`命令确定[容器](https://cloud.tencent.com/product/tke?from_column=20065&from=20065)的名字，

```javascript
docker ps 
```

复制

![](https://ask.qcloudimg.com/raw/yehe-1935965624ba740/tftdm3y4cu.png)

这边圆圈圈起来的就是容器的名字啦。

Halo里面的容器名字就是`halo`

#### 第二步

备份数据(重要)，并停止容器

利用`docker inspect 容器的名字`找出你容器的映射到本地的文件路径，

![](https://ask.qcloudimg.com/raw/yehe-1935965624ba740/bjc83r0r7a.png)

图片里就是：

```javascript
cp -r /root/.halo /root/.halo.1.4.15  # 备份并重命名为.halo.1.4.15
```

复制

#### 第三步

拉取最新的[容器镜像](https://cloud.tencent.com/product/tcr?from_column=20065&from=20065)

```javascript
docker pull halohub/halo:1.4.16
```

复制

`halohub/halo:1.4.16`这部分替换成你需要更新的镜像的名字和版本号

很多是类似这种`xxxxx/xxxxx:latest`

#### 第四步

重新创建容器

```javascript
docker run -it -d --name halo -p 8090:8090 -v ~/.halo:/root/.halo --restart=unless-stopped halohub/halo:1.4.16
```

复制

这部分的命令可以保存在了自己对应文件夹下的`config.txt`文件里，下次更新，直接粘贴出来，修改最后面镜像的部分（这里是`halohub/halo:1.4.16`）重新部署就ok了。

参考来源：[Halo官方文档](https://cloud.tencent.com/developer/tools/blog-entry?target=https%3A%2F%2Fdocs.halo.run%2Fgetting-started%2Fupgrade%2F)

### 2、更新用Docker-compose部署的应用

很简单，只要三步。

#### 第一步

进入到你docker-compose所在的文件夹下，执行

```javascript
whereis docker-compose 
```

```javascript
docker-compose pull
```

 

#### 第二步

重启你的容器

```javascript
docker-compose up -d --remove-orphans
```

 

#### 第三步（可选）

删除掉旧的镜像

```javascript
docker image prune 
```

 
### 3、直接利用Portainer更新

有安装Portainer的同学可以直接用Portainer来更新容器镜像。

Portainer的安装可以看这里：[【Docker系列】Docker可视化面板——Portainer](https://cloud.tencent.com/developer/tools/blog-entry?target=https%3A%2F%2Fwww.shutiaoya.com%2Findex.php%2F2022%2F03%2F26%2Fportainer-mb%2F)

#### 第一步

登陆Portainer面板，选择容器

![](https://ask.qcloudimg.com/raw/yehe-1935965624ba740/nipuyshm55.png)

#### 第二步

选择需要更新的容器，点击`Recreate`，然后点击`Pull latest images`，最后点击`Recreate`

等待完成就ok了。

![](https://ask.qcloudimg.com/raw/yehe-1935965624ba740/qu2fkfgg2m.png)