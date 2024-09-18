version: '3'
services:
  nginx:
    image: nginx:1.21.6-alpine
    container_name: ftp-nginx
    ports:
      - "80:80"
    volumes:
      - ./data:/usr/share/nginx/html
      - ./nginx/conf.d:/etc/nginx/conf.d
    restart: always
  vsftpd:
    image: shourai/vsftpd-alpine:latest
    container_name: vsftp
    environment:
      - FTP_USER=admin        #自定义用户名
      - FTP_PASS=2161023252       #自定义用户密码 
      - PASV_ENABLE=YES
      - PASV_ADDRESS=192.254.8.88   #宿主机的IP
      - PASV_MIN_PORT=21100
      - PASV_MAX_PORT=21110
      - ANON_ENABLE=NO
      - NO_ANON_PASSWD=NO
      - ANON_ROOT=/var/ftp
    volumes:
      - ./data:/home/admin    #与FTP_USER保持一致,即$FTP_USER的值是什么此处的目录就是什么
    ports:
      - "20:20"
      - "21:21"
      - "21100-21110:21100-21110"
    restart: always