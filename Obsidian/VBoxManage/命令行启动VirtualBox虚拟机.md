VBoxManage提供了一系列的虚拟机管理命令，包括创建/删除/启动/修改等等，这里不一一列举。有点像Xen的XM命令。

不过这里只关心启动虚拟机的命令：VBoxManage startvm。VBoxManage的完整命令列表可以参考这里。  
  
VBoxManage startvm子命令可以开启一台状态为关闭或者保存的虚拟机。该命令的语法为:  
VBoxManage startvm uuid>|name... \[--type gui|sdl|headless\]  
  
可以通过虚拟机的uuid或者name来指定某台虚拟机，可以通过另外一个子命令list列出系统已有的虚拟机：

```BASH
initial@vostro:~$ VBoxManage list vms
"Win10" {8906046a-7a5b-4ca9-bbbc-0eaf38536048}
"kali-linux-amd64" {ea0ca277-eb97-4c7e-a1d1-a1aea1995169}

```  
  
我系统上已经安装了一台名为Win10的虚拟机，后面括号内部的是它的UUID。  
  
VBoxManage startvm子命令可以通过–type参数指定启动的方式，其中gui就是图形化界面，这和我们平时启动的方式一样。

sdl也是图形化界面，但是少掉了部分功能，比如没有菜单等，一般用于调试过程。最后headless是在后台运行，并且默认开启vrdp服务，可以通过远程桌面工具来访问。

关于这三种启动方式的介绍可以看手册中的这一篇。所以一般我们使用gui或者headless类型启动。  
  
使用gui类型启动虚拟机：  

```bash
$ VBoxManage startvm Win10 --type gui  
```
  
执行结束后，就会启动指定的虚拟机，几乎和平时没什么区别。  
  
使用headless类型启动虚拟机:

  
```bash
$ VBoxManage startvm "Win10" --type headless
```

或者

```bash
$ VBoxHeadless --startvm "Win10"  
```
  
结果返回：

  
$ rdesktop -a 16 -N -g 1280x800 127.0.0.1:3389

  
Autoselected keyboard map en-us

  
ERROR: connect: Connection refused

  
  
翻了下手册，结果发现要获得VRDP的支持还需要安装额外的扩展包，详细说明可以参考这里。

从VirtualBox的下载页面选择相应的版本下载扩展包。下载完成后，双击即可以完成安装，或者在菜单中File-Preference-Extensions可以安装和查看已安装的扩展包。  
  
安装好再次执行上面的远程命令，这下可以看见虚拟机界面了吧。

可以通过ctrl+alt+enter切换全屏。不过我这里用rdesktop全屏后，屏幕就黑了，只有点过的地方才会恢复。

不知道是什么原因，我就干脆用TigerVNC了，同时在启动headless的时候加上-n参数{$ VBoxHeadless -n -s winxp (VBoxHeadless -s winxp --vnc --vncport 5900 --vncpass password)}，通过以下命令远程连接:

$ vncviewer localhost:5900  
  
按下F8会出现一个菜单，里面可以切换全屏。  
  
一切相关的命令：  
$ VBoxManage list runningvms # 列出运行中的虚拟机

  
$ VBoxManage controlvm XP acpipowerbutton # 关闭虚拟机，等价于点击系统关闭按钮，正常关机

  
$ VBoxManage controlvm XP poweroff # 关闭虚拟机，等价于直接关闭电源，非正常关机

  
$ VBoxManage controlvm XP pause # 暂停虚拟机的运行

  
$ VBoxManage controlvm XP resume # 恢复暂停的虚拟机

  
$ VBoxManage controlvm XP savestate # 保存当前虚拟机的运行状态
