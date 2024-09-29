
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