timeshift的介绍

Timeshift 是一款自由开源工具，可创建文件系统的增量快照。可以使用 RSYNC 或 BTRFS 两种方式创建快照。

项目地址：

[https://github.com/teejee2008/timeshift](https://github.com/teejee2008/timeshift)



# timeshift的安装配置

安装并配置timeshift

安装

```bash
sudo apt install timeshift
```

完成之后看一下：

```bash
$ sudo timeshift

Timeshift v21.09.1 by Tony George (teejeetech@gmail.com)

Syntax:

  timeshift --check
  timeshift --create [OPTIONS]
  timeshift --restore [OPTIONS]
  timeshift --delete-[all] [OPTIONS]
  timeshift --list-{snapshots|devices} [OPTIONS]

Options:

List:
  --list[-snapshots]         List snapshots
  --list-devices             List devices

Backup:
  --check                    Create snapshot if scheduled
  --create                   Create snapshot (even if not scheduled)
  --comments <string>        Set snapshot description
  --tags {O,B,H,D,W,M}       Add tags to snapshot (default: O)

Restore:
  --restore                  Restore snapshot
  --clone                    Clone current system
  --snapshot <name>          Specify snapshot to restore
  --target[-device] <device> Specify target device
  --grub[-device] <device>   Specify device for installing GRUB2 bootloader
  --skip-grub                Skip GRUB2 reinstall

Delete:
  --delete                   Delete snapshot
  --delete-all               Delete all snapshots

Global:
  --snapshot-device <device> Specify backup device (default: config)
  --yes                      Answer YES to all confirmation prompts
  --btrfs                    Switch to BTRFS mode (default: config)
  --rsync                    Switch to RSYNC mode (default: config)
  --debug                    Show additional debug messages
  --verbose                  Show rsync output (default)
  --quiet                    Hide rsync output
  --scripted                 Run in non-interactive mode
  --help                     Show all options

Examples:

timeshift --list
timeshift --list --snapshot-device /dev/sda1
timeshift --create --comments "after update" --tags D
timeshift --restore 
timeshift --restore --snapshot '2014-10-12_16-29-08' --target /dev/sda1
timeshift --delete  --snapshot '2014-10-12_16-29-08'
timeshift --delete-all 

Notes:

  1) --create will always create a new snapshot
  2) --check will create a snapshot only if a scheduled snapshot is due
  3) Use --restore without other options to select options interactively
  4) UUID can be specified instead of device name
  5) Default values will be loaded from app config if options are not specified

```



配置

默认安装后，在第一次运行前，我们需要修改 timeshift 的配置文件，否则 timeshift 会默认找到一个 ext4 分区作为备份区。

看一下目前的硬盘情况：

```bash
$ sudo lsblk -f
NAME        FSTYPE   FSVER LABEL UUID                                 FSAVAIL FSUSE% MOUNTPOINTS
loop0       squashfs 4.0                                                    0   100% /snap/core20/1974
loop1       squashfs 4.0                                                    0   100% /snap/core20/2015
loop2       squashfs 4.0                                                    0   100% /snap/lxd/24322
loop3       squashfs 4.0                                                    0   100% /snap/snapd/19457
loop4       squashfs 4.0                                                    0   100% /snap/snapd/20290
sda                                                                                  
├─sda1      vfat     FAT32       7966-FD09                                           
└─sda2      ext4     1.0         af5ad2ce-a4e2-45f9-a148-93bc788543a4                
nvme0n1                                                                              
├─nvme0n1p1 vfat     FAT32       03E9-5207                                 1G     1% /boot/efi
├─nvme0n1p2 swap     1           ae8e8afe-f92d-4a57-b9ea-df6ff74109f3                [SWAP]
├─nvme0n1p3 ext4     1.0         33a3f11c-546b-404a-95fe-1a9a765dfe25   85.7G     7% /
└─nvme0n1p4 xfs                  ef3311c1-5b6b-4a47-bc53-9f66f17744e9  128.4G     1% /timeshift

```

Copy

这里的 `/dev/nvme0n1p4` 是我为 timeshift 预留的分区，存放在 nvme 磁盘上，以保证备份和恢复的速度。

```bash
$ sudo lsblk -f
NAME        FSTYPE   LABEL UUID                                 FSAVAIL FSUSE% MOUNTPOINT
loop0       squashfs                                                  0   100% /snap/core18/2128
loop1       squashfs                                                  0   100% /snap/lxd/21029
loop2       squashfs                                                  0   100% /snap/snapd/12704
nvme0n1                                                                        
├─nvme0n1p1 vfat           72C9-B4E4                             504.9M     1% /boot/efi
├─nvme0n1p2 ext4           a83415e6-ed69-4932-9d08-1e87d7510dc1  689.1G     1% /
└─nvme0n1p3 ext4           9b22569d-9410-48cc-b994-10257b2d0498   81.5G     0% /run/timeshift/backup
```

记录 nvme0n1p4的 uuid ，然后修改配置, `sudo vi /etc/timeshift/timeshift.json` 打开后设置 backup_device_uuid 为 nvme0n1p3 的 uuid :

```json
{
  "backup_device_uuid" : "ef3311c1-5b6b-4a47-bc53-9f66f17744e9",
  "parent_device_uuid" : "",
  "do_first_run" : "true",
  "btrfs_mode" : "false",
  "include_btrfs_home" : "false",
  "stop_cron_emails" : "true",
  "schedule_monthly" : "false",
  "schedule_weekly" : "false",
  "schedule_daily" : "false",
  "schedule_hourly" : "false",
  "schedule_boot" : "false",
  "count_monthly" : "2",
  "count_weekly" : "3",
  "count_daily" : "5",
  "count_hourly" : "6",
  "count_boot" : "5",
  "snapshot_size" : "0",
  "snapshot_count" : "0",
  "exclude" : [
  ],
  "exclude-apps" : [
  ]
}

```

执行timeshift命令，就能看到配置生效了：

```bash
 sudo timeshift --list
First run mode (config file not found)
Selected default snapshot type: RSYNC
Mounted '/dev/nvme0n1p4' at '/run/timeshift/backup'
Device : /dev/nvme0n1p4
UUID   : ef3311c1-5b6b-4a47-bc53-9f66f17744e9
Path   : /run/timeshift/backup
Mode   : RSYNC
Status : No snapshots on this device
First snapshot requires: 0 B


No snapshots found
```


# 创建timeshift快照

通过create命令创建timeshift快照进行备份

常见快照的命令为：

```bash
sudo timeshift --create --comments "first backup after timeshift install 2023-12-8"
```

Copy

tags的类型:

- O: Ondemand，默认值，一般用于手工创建快照
- B: Boot
- H: Hourly
- D: Daily
- W: Weekly
- M: Monthly

### 示例
这是创建的第一个快照，操作系统和 timeshift 安装完成之后的第一个快照：

```bash
$ sudo timeshift --create --comments "first backup after timeshift install 2023-12-8"
First run mode (config file not found)
Selected default snapshot type: RSYNC

/dev/nvme0n1p4 is mounted at: /run/timeshift/backup, options: rw,relatime,attr2,inode64,logbufs=8,logbsize=32k,noquota

------------------------------------------------------------------------------
Estimating system size...
Creating new snapshot...(RSYNC)
Saving to device: /dev/nvme0n1p4, mounted at path: /run/timeshift/backup
Synching files with rsync...
Created control file: /run/timeshift/backup/timeshift/snapshots/2023-12-08_01-59-41/info.json
RSYNC Snapshot saved successfully (30s)
Tagged snapshot '2023-12-08_01-59-41': ondemand

```



完成后查看：

```bash
$ sudo timeshift --create --comments "first backup after timeshift install 2023-12-8"
First run mode (config file not found)
Selected default snapshot type: RSYNC

/dev/nvme0n1p4 is mounted at: /run/timeshift/backup, options: rw,relatime,attr2,inode64,logbufs=8,logbsize=32k,noquota

------------------------------------------------------------------------------
Estimating system size...
Creating new snapshot...(RSYNC)
Saving to device: /dev/nvme0n1p4, mounted at path: /run/timeshift/backup
Synching files with rsync...
Created control file: /run/timeshift/backup/timeshift/snapshots/2023-12-08_01-59-41/info.json
RSYNC Snapshot saved successfully (30s)
Tagged snapshot '2023-12-08_01-59-41': ondemand
 
```

