

#LDM

```bash

VBoxManage internalcommands createrawvmdk -filename '/home/initial/VirtualBox VMs/hd_D.vmdk'  -rawdisk //dev/mapper/ldm_vol_DESKTOP-2JFANE7-Dg0_Volume1
VBoxManage internalcommands createrawvmdk -filename '/home/initial/VirtualBox VMs/hd_E.vmdk' -rawdisk //dev/mapper/ldm_vol_DESKTOP-2JFANE7-Dg0_Volume2

```

#NTFS

```bash

VBoxManage internalcommands createrawvmdk -filename '/home/initial/VirtualBox VMs/hd_D.vmdk'  -rawdisk //dev/sda1

VBoxManage internalcommands createrawvmdk -filename '/home/initial/VirtualBox VMs/hd_E.vmdk' -rawdisk //dev/sda2

```