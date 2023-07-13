ip = '192.168.1.1'
# 用字符串自带的split()函数将ip地址（字符串‘192.168.1.1'）转换成列表ip_octets
ip_octets = ip.split('.')  # Python split() 通过指定分隔符对字符串进行切片
print(ip_octets)

ip_octets_binary = []  # 创建一个空列表ip_octets_binary
for octet in ip_octets:  # 用for循环遍历ip_octets里的元素
    binary_octet = bin(int(octet)).lstrip('0b')  # 用bin()函数转换成二进制形式
    #  bin()只能将数据类型为整数的十进制数转换成二进制,，因此这里我们要先将字符串用int()转换成整数后再来调用bin()函数
    #  bin()函数本身会在转化后的二进制数字前面加上'0b'，我们必须调用lstrip('0b')将其拿掉
    ip_octets_binary.append(binary_octet.zfill(8))  # 写入创建的空列表ip_octets_binary里面
    # zfill(8),作用是自动帮我们填充八位数的二进制数
print(ip_octets_binary)