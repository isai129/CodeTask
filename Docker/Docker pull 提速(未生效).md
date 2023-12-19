```bash
initial@initial-Vostro:/etc/docker$ ls
initial@initial-Vostro:/etc/docker$ sudo vim daemon.json
[sudo] initial 的密码： 
initial@initial-Vostro:/etc/docker$ cat daemon.json 
{
    "max-concurrent-downloads":20,
    "max-concurrent-uploads":20,
    "registry-mirrors": [
        "https://<changme>.mirror.aliyuncs.com",
        "https://dockerproxy.com",
        "https://mirror.baidubce.com",
        "https://docker.m.daocloud.io",
        "https://docker.nju.edu.cn",
        "https://docker.mirrors.sjtug.sjtu.edu.cn"
  ]
}

initial@initial-Vostro:/etc/docker$ sudo systemctl daemon-reload 
initial@initial-Vostro:/etc/docker$ sudo systemctl restart docker


```

##### Docker Registry Mirror 配置

创建或修改 `/etc/docker/daemon.json`:

```json
{
    "max-concurrent-downloads":20,
    "max-concurrent-uploads":20,
    "registry-mirrors": [
        "https://dockerproxy.com",
        "https://docker.m.daocloud.io",
        "https://docker.nju.edu.cn",
        "https://docker.mirrors.sjtug.sjtu.edu.cn"
  ]
}

```