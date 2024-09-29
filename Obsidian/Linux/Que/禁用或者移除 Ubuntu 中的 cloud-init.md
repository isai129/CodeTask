
[cloud-init](https://cloud-init.io/) 堪称自定义云实例的标准，是由 Canonical 公司（Ubuntu 的创建者）开发的开源软件。

云镜像是操作系统模板，每个实例都作为每个其他实例的相同克隆开始。正是用户数据赋予每个云实例个性，而 cloud-init 是将用户数据自动应用于您的实例的工具。

**使用 cloud-init 进行配置：**

- 设置默认语言环境
- 设置主机名
- 生成和设置 SSH 私钥
- 设置临时挂载点

**适用于许多流行的操作系统：**

虽然 cloud-init 始于 Ubuntu，但它现在可用于大多数主要的 Linux 和 FreeBSD 操作系统。 对于云镜像提供商，cloud-init 会自动处理云供应商之间的许多差异 -- 例如，官方的 Ubuntu 云镜像在所有公共云和私有云中都是相同的。

非云环境，可以选择关闭它，或者彻底删除，方法如下：

## 方法 1: 通过创建文件禁用 cloud-init

这是最简单最安全的方法，在 `/etc/cloud` 目录下创建 `cloud-init.disabled` 文件重启后生效。删除该文件就可以恢复。

```shell
sudo touch /etc/cloud/cloud-init.disabled

[[init]] 6
reboot
```


## 方法 2: 移除 cloud-init 软件包及文件夹

该方法彻底移除 cloud-init。

```shell
sudo apt purge cloud-init -y

sudo rm -rf /etc/cloud && sudo rm -rf /var/lib/cloud/

reboot
```