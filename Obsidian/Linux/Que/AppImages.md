AppImages使用通用的软件格式，通过将整个软件打包成AppImage,一个包包含了所有的功能. 并且几乎可以在所有的linux发行版本中使用。
	[[/opt]],主要存放可选的程序。linux中/opt目录用来安装附加软件包，是用户级的程序目录.安装到/opt目录下的程序，它所有的数据、库文件等等都是放在同个目录下面。这里可以用于放置第三方大型软件（或游戏），当你不需要时，直接rm -rf掉即可。在硬盘容量不够时，也可将/opt单独挂载到其他磁盘上使用。
	[[/usr]] ,系统级的目录,可以理解为 C:/Windows/。
	linux中/usr下的/local目录为用户级的程序目录，可以理解为C:/Progrem Files/。用户自己编译的软件默认会安装到这个目录下。 这里主要存放那些手动安装的软件，即不是通过apt-get安装的软件。它和/usr目录具有相类似的目录结构。让软件包管理器来管理/usr目录，而把自定义的脚本(scripts)放到/usr/local目录下面。