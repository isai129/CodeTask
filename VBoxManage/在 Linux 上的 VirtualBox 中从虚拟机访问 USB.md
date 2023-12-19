**1：安装 VirtualBox 扩展包（在主机上）**

```
Oracle_VM_VirtualBox_Extension_Pack-7.0.12.vbox-extpack
```


**2：将用户添加到 vboxusers 组（在宿主机上）**

要在 VirtualBox 中使用 USB 驱动器，你的当前用户需要位于 `vboxusers` 组中。

我知道这听起来有点复杂，但 [将用户添加到组](https://link.zhihu.com/?target=https%3A//learnubuntu.com/add-user-group/) 是一个命令过程，将用户添加到 `vboxusers` 组可以通过以下方式完成：

```bash
sudo usermod -aG vboxusers $USER
```


**完成这两个步骤后，重启系统以使这些步骤生效**
