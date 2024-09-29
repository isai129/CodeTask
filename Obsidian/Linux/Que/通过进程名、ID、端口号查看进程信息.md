1. 通过进程名查看

```bash
ps -ef | grep sshd
```

2. 通过进程ID查看

	1. 通过进程ID查询端口占用：
	
```bash
netstat -nap | grep 522
```
	
	2. 通过进程ID 查询进程名：
	
	  ```bash
	  ps -ef | grep 522
```

3. 通过端口号查看

```bash
netstat -tunlp | grep 22
```


4. 根据进程id杀死进程

```bash
sudo kill -9 522
```
