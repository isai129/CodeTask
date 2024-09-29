Linux 世界有三种“通用”打包格式，允许在“任何” Linux 发行版上运行：Snap、Flatpak 和 AppImage。

Ubuntu 内置了 Snap，但大多数发行版和开发人员都避免使用它，因为它的闭源性质。他们更喜欢 [Fedora 的 Flatpak 打包系统](https://itsfoss.com/what-is-flatpak/)。

作为 Ubuntu 用户，你并不局限于 Snap。你还可以在 Ubuntu 系统上使用 Flatpak。

在本教程中，我将讨论以下内容：

- 在 Ubuntu 上启用 Flatpak 支持
- 使用 Flatpak 命令来管理包
- 从 Flathub 获取包
- 将 Flatpak 软件包添加到软件中心

听起来很令人兴奋？ 让我们一一看看。

### 在 Ubuntu 上安装 Flatpak

你可以使用以下命令轻松安装 Flatpak：

1. `sudo apt install flatpak`

对于 **Ubuntu 18.04 或更早版本**，请使用 PPA：

1. `sudo add-apt-repository ppa:flatpak/stable`
2. `sudo apt update`
3. `sudo apt install flatpak`

#### 添加 Flathub 仓库

你已在 Ubuntu 系统中安装了 Flatpak 支持。但是，如果你尝试安装 Flatpak 软件包，你将收到 [“No remote refs found”](https://itsfoss.com/no-remote-ref-found-flatpak/) 错误。这是因为没有添加 Flatpak 仓库，因此 Flatpak 甚至不知道应该从哪里获取应用。

Flatpak 有一个名为 “Flathub” 的集中仓库，可以从此处找到并下载许多 Flatpak 应用。

你应该添加 Flathub 仓库来访问这些应用。

1. `flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo`

![Install Flatpak in latest versions of Ubuntu and then add Flathub repo](https://img.linux.net.cn/data/attachment/album/202307/24/230051f1l2wqiwlcxpyivw.svg)

_Install Flatpak in latest versions of Ubuntu and then add Flathub repo_

安装并配置 Flatpak 后，**重启你的系统**。否则，已安装的 Flatpak 应用将不会在你的系统菜单上可见。

不过，你始终可以通过运行以下命令来运行 Flatpak 应用：

1. `flatpak run <package-name>`

### 常用 Flatpak 命令

现在你已经安装了 Flatpak 打包支持，是时候学习包管理所需的一些最常见的 Flatpak 命令了。

#### 搜索包

如果你知道应用名称，请使用 Flathub 网站或使用以下命令：

1. `flatpak search <package-name>`

![Search for a package using Flatpak Search command](https://img.linux.net.cn/data/attachment/album/202307/24/230051kcig3cgzrmio87zr.svg)

_Search for a package using Flatpak Search command_

> 🚧 除了搜索 Flatpak 包之外，在其他情况下， 指的是正确的 Flatpak 包名称，例如 `com.raggesilver.BlackBox`（上面截图中的应用 ID）。你还可以使用应用 ID 的最后一个词 `Blackbox`。

#### 安装 Flatpak 包

以下是安装 Flatpak 包的语法：

1. `flatpak install <remote-repo> <package-name>`

由于几乎所有时候你都会从 Flathub 获取应用，因此远程仓库将是 `flathub`：

1. `flatpak install flathub <package-name>`

![Install a package after searching for its name](https://img.linux.net.cn/data/attachment/album/202307/24/230051fhqi8sggp4tgsing.svg)

_Install a package after searching for its name_

在极少数情况下，你可以直接从开发人员的仓库安装 Flatpak 包，而不是 Flathub。在这种情况下，你可以使用如下语法：

1. `flatpak install --from https://flathub.org/repo/appstream/com.spotify.Client.flatpakref`

#### 从 flatpakref 安装包

这是可选的，也很少见。但有时，你会获得应用的 `.flatpakref` 文件。这**不是离线安装**。.flatpakref 包含有关从何处获取包的必要详细信息。

要从此类文件安装，请打开终端并运行：

1. `flatpak install <path-to-flatpakref file>`

![Install a Flatpak package from Flatpakref file](https://img.linux.net.cn/data/attachment/album/202307/24/230052um1hkeotfzcxx10x.svg)

_Install a Flatpak package from Flatpakref file_

#### 从终端运行 Flatpak 应用

再说一遍，这是你不会经常做的事情。大多数情况下，你将在系统菜单中搜索安装应用并从那里运行该应用。

但是，你也可以使用以下命令从终端运行它们：

1. `flatpak run <package-name>`

#### 列出已安装的 Flatpak 软件包

想要查看你的系统上安装了哪些 Flatpak 应用？ 像这样列出它们：

1. `flatpak list`

![List all the installed Flatpak packages on your system](https://img.linux.net.cn/data/attachment/album/202307/24/230052lfssbnuia7dxxmxj.svg)

_List all the installed Flatpak packages on your system_

#### 卸载 Flatpak 包

你可以通过以下方式删除已安装的 Flatpak 包：

1. `flatpak uninstall <package-name>`

如果你想**清除不再需要的剩余包和运行时**，请使用：

1. `flatpak uninstall --unused`

![Remove a Flatpak package and later, if there is any unused runtimes or packages, remove them](https://img.linux.net.cn/data/attachment/album/202307/24/230052obp5gbxy33pzhph7.svg)

_Remove a Flatpak package and later, if there is any unused runtimes or packages, remove them_

它可能会帮助你 [在 Ubuntu 上节省一些磁盘空间](https://itsfoss.com/free-up-space-ubuntu-linux/)。

### Flatpak 命令总结

以下是你在上面学到的命令的快速摘要：

|用途|命令|
|---|---|
|搜索包|`flatpak search`|
|安装包|`flatpak install`|
|列出已安装的包|`flatpak list`|
|从 flatpakref 安装|`flatpak install <package-name.flatpakref>`|
|卸载软件包|`flatpak uninstall`|
|卸载未使用的运行时和包|`flatpak uninstall --unused`|

### 使用 Flathub 探索 Flatpak 包

我知道通过命令行搜索 Flatpak 包并不是最好的体验，这就是 [Flathub 网站](https://flathub.org/en-GB) 的用武之地。

你可以在 Flathub 上浏览 Flatpak 应用，它提供了更多详细信息，例如经过验证的发布商、下载总数等。

你还将在应用页面底部获得安装应用所需的命令。

![](https://img.linux.net.cn/data/attachment/album/202307/24/230052e8mfr77mfpkonmqn.png)

![](https://img.linux.net.cn/data/attachment/album/202307/24/230053yqkbxk1zf0v8bv87.png)

### 额外信息：使用支持 Flatpak 软件包的软件中心

你可以将 Flatpak 包添加到 GNOME 软件中心，并使用它以图形方式安装软件包。

有一个专用插件可以将 Flatpak 添加到 GNOME 软件中心。

> 🚧 从 Ubuntu 20.04 开始，Ubuntu 默认的软件中心是 Snap Store，并且不支持 Flatpak 集成。因此，安装以下软件包将产生两个软件中心：一个 Snap 和另一个 DEB。

![When you install GNOME Software Flatpak plugin in Ubuntu, a DEB version of GNOME Software is installed. So you will have two software center application](https://img.linux.net.cn/data/attachment/album/202307/24/230053bm51mdp57m2x6wup.png)

_When you install GNOME Software Flatpak plugin in Ubuntu, a DEB version of GNOME Software is installed. So you will have two software center application_

1. `sudo apt install gnome-software-plugin-flatpak`

![Installing GNOME Software Plugin in Ubuntu](https://img.linux.net.cn/data/attachment/album/202307/24/230054zfkgooqclhyfptrp.svg)

_Installing GNOME Software Plugin in Ubuntu_