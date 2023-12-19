1.删除非空目录 `rm -r 目录名

	``-r(–recursive 或 -R)：递归删除，主要用于删除目录，可删除指定目录及包含的所有内容，包括所有的子目录和文件
	
2.查看软件安装位置 

`whereis

3.查询运行软件所在路径

`which`

4.debain10

```bash

 1.查看ip
 ip a (address)
 
 2.查看路由表：
 ip r(route)
 
 3.测试端口通讯：
 
   initial@HP-EliteDesk:~$ nc -vz 111.20.87.234 89
   Connection to 111.20.87.234 89 port [tcp/*] succeeded!
   initial@HP-EliteDesk:~$ nc -vuz 202.107.200.20 6666
   Connection to 202.107.200.20 6666 port [udp/*] succeeded!

	-u代表udp协议 ，-v代表详细模式，-z 代表只监测端口不发送数据
	
	nc vuz 202.107.200.20 6666
	forward host lookup failed: Unknown host (正向主机查找失败：未知主机)
未配置DNS引起，加 `-n`参数，忽略DNS查找
	nc -vuz 202.107.200.20 6666 -n
	(UNKNOWN) [202.107.200.20] 6666 (?) open

```



