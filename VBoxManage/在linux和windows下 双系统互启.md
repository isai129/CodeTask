--在linux和windows下 双系统互启

安装virtualbox
  
安装后在terminal模式 用root权限的运行virtualbox 
sudo virtualbox，不用root会出错。 配置一个windows的运行环境, 想要什么样的自己设定。  
  
接下来做硬盘vmdk文件创建，这里直接创建整个硬盘的映射文件。创建单个分区的比较麻烦，又要提取mbr，又要修改bcd，而且还造成虚拟机能运行，原生启动错误的问题。  

创建前请分配所有硬盘分区的读写权限，假如有三个 sda1 sda2 sda3 那么命令行下  

```bash

sudo chmod 666 /dev/sda1  
  
sudo chmod 666 /dev/sda2  
  
sudo chmod 666 /dev/sda3 
```
  
使用如下指令创建 wmdk 硬盘的映射文件，这里用到的是Virtualbox的shell模式，更多内容请参看virtualbox高级用户手册  
  
```bash
sudo vboxmanage internalcommands createrawvmdk -filename /home/用户名/rawdisk.vmdk -rawdisk /dev/sda -relative  
```
  
用户名替换成自己的登录id， 这样rawdisk.vmdk就可以被Virtualbox（root权限下的）直接调用并且运行windows了。多个硬盘的请分别创建镜像，都加到Virtualbox的ATA管理器里面。  
  
在windows下运行物理磁盘的linux，请安装windows的VirtualBox，同样办法创建映射文件（命令稍有不同，看考windows版本Virtualbox的高级用户手册），注意请创建不同的映射文件，不要拿来在linux下创建的vmdk文件用，会死的很惨的。  
  
实践证明这个办法是彻底不用修改mbr，bcd 还有grub的。。。可以双物理磁盘上的系统互启动。。。

VirtualBox建立物理硬盘的虚拟磁盘链接：  
硬盘映射：  

**代码:**
--Linux下:  
```bash

VBoxManage internalcommands createrawvmdk -filename ~/nenew.vmdk -rawdisk /dev/sda  
Windows下:  
vboxmanage internalcommands createrawvmdk -filename d:\\nenew.vmdk -rawdisk \\.\PhysicalDrive0
```

注： linux下/dev/sda代表第一块硬盘，/dev/sdb为第二块硬盘……  
windows下\\.\PhysicalDrive0代表第一块硬盘，\\.\PhysicalDrive1为第二块硬盘……  
分区映射：  

**代码:**

Linux下:  
```bash
VBoxManage internalcommands createrawvmdk -filename ~/nenew.vmdk -rawdisk /dev/sda -partitions 1  
Windows下:  
vboxmanage internalcommands createrawvmdk -filename d:\\nenew.vmdk -rawdisk \\.\PhysicalDrive0 -partitions 1

```
  
附 VBoxManage internalcommands createrawvmdk 命令：  
VBoxManage internalcommands createrawvmdk 创建一个vmdk格式的硬盘  
-filename <filename> vmdk格式的硬盘所对应的vmdk文件  
-rawdisk <diskname> vmdk文件所对应的物理硬盘  
[-partitions <list of partition numbers> vmdk文件对应的物理硬盘的分区  
[-mbr <filename>] ] 将这个文件包含的引导记录写到vmdk文件  
[-register] 将这个新创建的硬盘注册到virtualbox  
[-relative] 激活这个新创建的硬盘的分区