udo1. 初始化

```bash
#安装ldmtool 
sudo apt install ldmtool -y

#使用ldmtool自动配置设备  
sudo ldmtool create all
...
[ldm_vol_initial-Vostro_Volume1] #已经配置完成设备,复制这个设备名称
[ldm_vol_DESKTOP-2JFANE7-Dg0_Volume] #已经配置完成设备,复制这个设备名称
[ldm_vol_DESKTOP-2JFANE7-Dg0_Volume1]  #已经配置完成设备,复制这个设备名称

#创建挂载点 
sudo mkdir -p /media/winraid-000
#将设备挂载到/media/winraid-000/ 
sudo mount /dev/mapper/ldm_vol_initial-Vostro_Volume1 /media/winraid-000/
sudo mount /dev/mapper/ldm_vol_DESKTOP-2JFANE7-Dg0_Volume /media/winraid-000/
sudo mount /dev/mapper/ldm_vol_DESKTOP-2JFANE7-Dg0_Volume1 /media//winraid-000/

```


2. 持久化

	systemd自动挂载

```bash
#创建服务文件 

sudo [[[[vim]]]] /etc/systemd/system/winraid-000-automount.service #创建服务文件
```

	写入内容


```js
[Unit]
Description=LDM: Mount as /media/winraid-000
After=local-fs-pre.target
Before=local-fs.target
DefaultDependencies=no

[Service]
Type=oneshot
User=root
ExecStart=/usr/bin/ldmtool create all

[Install]
WantedBy=local-fs.target
```

#启用服务

```bash
sudo systemctl enable winraid-000-automount.service  
```

#重启

```bash
$reboot
```
