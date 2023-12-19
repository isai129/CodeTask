**当我在虚拟机上执行它时`nc`工作正常。**

```
Connection to 10.0.0.10 22 port [tcp/ssh] succeeded!
```

**但是当我在我的 docker 容器中执行相同的命令时，它给出了以下 UNKNOWN 错误/异常。**

```
10.0.0.10: inverse host lookup failed: Unknown host 
(UNKNOWN) [10.0.0.10] 22 (ssh) open
```

**下面是我正在使用的`nc`命令：**

```
nc -vz 10.0.0.10 22 -w 4
```




只需将 -n 放在侦听器和客户端的两侧即可消除此错误，因为使用它会忽略 DNS 查找。


**如果还**没有通过**SSH 连接到 docker 容器，这是正常的。**

`Connection to 10.0.0.10 22 port [tcp/ssh] succeeded!` **在 VM 中可以看到，因为您已经以`ssh username@10.0.0.10`形式通过`ssh username@10.0.0.10`连接到 VM 中，并且在 VM 中将端口`22`用于 SSH。**

**但是，当您在 docker 容器内（使用`docker run`或`docker exec`或`docker attach` ）时，将**不会**使用端口`22` ，因此预计 docker 容器内会出现来自`nc`的以下错误：**

```
10.0.0.10: inverse host lookup failed: Unknown host 
(UNKNOWN) [10.0.0.10] 22 (ssh) open
```

**以下是在`nginx` docker 容器中使用`nc`成功测试是否使用端口`80`的步骤：**

```
$ sudo docker run --name docker-nginx -d -p 80:80 nginx
$ sudo docker exec -it docker-nginx /bin/bash
root@60ec582e90f4:/# apt-get -y update
root@60ec582e90f4:/# apt-get -y upgrade
root@60ec582e90f4:/# apt-get install -y net-tools
root@60ec582e90f4:/# apt-get install -y netcat   

# make sure that port 80 is used
root@60ec582e90f4:/# netstat -pan | grep 80
tcp     0   0 0.0.0.0:80   0.0.0.0:*   LISTEN  1/nginx: master pro 

# nc will work now inside the nginx container as port 80 is used inside the container

root@60ec582e90f4:/# nc -vz 127.0.0.1 80 -w 4
localhost [127.0.0.1] 80 (?) open
```

**因此， `nc -vz abcd P -w 4`在容器内工作，必须在该容器内的 IP 地址`abcd`上使用端口`P`**