  
一、Windows 环境

1、在虚拟机中，从微软官网下载SDelete （https://technet.microsoft.com/en-us/sysinternals/bb897443），下载完成后解压，然后 cmd 进入到刚刚存放的目录下（如 直接放在c盘根目录下），打开 cmd 执行：

-- 把整个 c 盘下的未使用的磁盘空间标记为 0，执行完后把虚拟机关机  
------------------------------------------------------  
C:\sdelete -z c:\

```bash
vboxmanage modifyhd DESKTOP-2JFANE7_VM.vdi --compact
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
```





二、Linux环境

1、在虚拟机中，打开终端执行：

-- 依次执行，执行完后把虚拟机关机  
------------------------------------------------------  
```bash
sudo dd if=/dev/zero of=/empty
```

sudo rm -f /empty  
------------------------------------------------------

2、然后进入宿主机 VBoxManage.exe 目录（通常为 VirtualBox 安装目录），然后执行 BoxManage 命令压缩 VDI 虚拟机磁盘文件即可。

------------------------------------------------------

VBoxManage.exe modifyhd "E:\VMs\rhel_erver_6.8_x64.vdi" --compact