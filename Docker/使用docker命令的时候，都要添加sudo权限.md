
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.38/images/json: dial unix /var/run/docker.sock: connect: permission denied


1、输入
`$ sudo groupadd docker`
回显示groupadd: group 'docker' already exists

2、将docker账户给与权限
`sudo gpasswd -a <你的用户名> docker`
例如： sudo gpasswd -a caoft docker

3、重启docker
`sudo service docker restart`


