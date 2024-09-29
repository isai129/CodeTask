### 

Ubuntu/Debian and derivatives

For Droidian and Ubuntu Touch, skip directly to the last step

Make sure you have Wayland Session enabled (Ubuntu 22.04+)

[how to enable/disable wayland on Ubuntu DesktopLinux Tutorials - Learn Linux Configuration](https://linuxconfig.org/how-to-enable-disable-wayland-on-ubuntu-22-04-desktop)

- Install pre-requisites
    

Copy

```
sudo apt install curl ca-certificates -y
```

- Add the official repository
    

Copy

```
curl https://repo.waydro.id | sudo bash
```

If the script fails to detect your distribution, you can provide a valid option by appending `-s <DISTRO>`. Currently supported values are: **mantic**, **focal**, **jammy**, **kinetic**, **lunar**, **noble**, **bookworm**, **bullseye**, **trixie**, **sid**

- Install waydroid
    

Copy

```
sudo apt install waydroid -y
```

Then start Waydroid from the applications menu.


#结束WayDroid进程，这个命令你会高频次用到

```
waydroid session stop
```

#安装lzip和sqlite

```
sudo apt install lzip sqlite
```

# Waydroid Extras Script

[](https://github.com/casualsnek/waydroid_script#waydroid-extras-script)

Script to add GApps and other stuff to Waydroid!

# Installation/Usage

[](https://github.com/casualsnek/waydroid_script#installationusage)

## Interactive terminal interface

[](https://github.com/casualsnek/waydroid_script#interactive-terminal-interface)

```
git clone https://github.com/casualsnek/waydroid_script
cd waydroid_script
python3 -m venv venv
venv/bin/pip install -r requirements.txt
sudo venv/bin/python3 main.py
```

[![image-20230430013103883](https://github.com/casualsnek/waydroid_script/raw/main/assets/img/README/image-20230430013103883.png)](https://github.com/casualsnek/waydroid_script/blob/main/assets/img/README/image-20230430013103883.png)

[![image-20230430013119763](https://github.com/casualsnek/waydroid_script/raw/main/assets/img/README/image-20230430013119763.png)](https://github.com/casualsnek/waydroid_script/blob/main/assets/img/README/image-20230430013119763.png)

[![image-20230430013148814](https://github.com/casualsnek/waydroid_script/raw/main/assets/img/README/image-20230430013148814.png)](https://github.com/casualsnek/waydroid_script/blob/main/assets/img/README/image-20230430013148814.png)

## Command Line

[](https://github.com/casualsnek/waydroid_script#command-line)

```shell
git clone https://github.com/casualsnek/waydroid_script
cd waydroid_script
python3 -m venv venv
venv/bin/pip install -r requirements.txt
# install something
sudo venv/bin/python3 main.py install {gapps, magisk, libndk, libhoudini, nodataperm, smartdock, microg, mitm}
# uninstall something
sudo venv/bin/python3 main.py uninstall {gapps, magisk, libndk, libhoudini, nodataperm, smartdock, microg}
# get Android device ID
sudo venv/bin/python3 main.py certified
# some hacks
sudo venv/bin/python3 main.py hack {nodataperm, hidestatusbar}
```

```bash
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"
```

network_proxy

```bash
adb shell settings put global http_proxy "http://127.0.0.1:7890"&&  
adb reverse tcp:7890 tcp:7890
```
