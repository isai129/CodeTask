### **Dockerd 代理**

在执行`docker pull`时，是由守护进程`dockerd`来执行。因此，代理需要配在`dockerd`的环境中。而这个环境，则是受`systemd`所管控，因此实际是`systemd`的配置。

在这个`proxy.conf`文件（可以是任意`*.conf`的形式）中，添加以下内容：

```bash
[Service]
Environment="HTTP_PROXY=http://127.0.0.1:7890"
Environment="HTTPS_PROXY=http://127.0.0.1:7890"
Environment="NO_PROXY=localhost,127.0.0.1,.example.com"
```

###### 重启Docker

```bash
sudo systemctl daemon-reload && 
sudo systemctl restart docker
```
######  检查Docker有没有使用代理

```bash
systemctl show --property=Environment docker
```

出现

```bash
Environment=HTTP_PROXY=http://127.0.0.1:7890 HTTPS_PROXY=http://127.0.0.1:7890
```


此时Docker就已经自动实现代理.



__________________________________________________________________________________

### **Container 代理**


在[容器](https://cloud.tencent.com/product/tke?from_column=20065&from=20065)运行阶段，如果需要代理上网，则需要配置 `~/.docker/config.json`。以下配置，只在Docker 17.07及以上版本生效。

```javascript
{
 "proxies":
 {
   "default":
   {
     "httpProxy": "http://127.0.0.1:7890",
     "httpsProxy": "http://127.0.0.1:7890",
     "noProxy": "localhost,127.0.0.1,.example.com"
   }
 }
}
```


这个是用户级的配置，除了 `proxies`，`docker login` 等相关信息也会在其中。而且还可以配置信息展示的格式、插件参数等。

此外，容器的网络代理，也可以直接在其运行时通过 `-e` 注入 `http_proxy` 等环境变量。这两种方法分别适合不同场景。`config.json` 非常方便，默认在所有配置修改后启动的容器生效，适合个人开发环境。在CI/CD的自动构建环境、或者实际上线运行的环境中，这种方法就不太合适，用 `-e` 注入这种显式配置会更好，减轻对构建、部署环境的依赖。当然，在这些环境中，最好用良好的设计避免配置代理上网.

### **Docker Build 代理**

虽然 `docker build` 的本质，也是启动一个容器，但是环境会略有不同，用户级配置无效。在构建时，需要注入 `http_proxy` 等参数。

```javascript
docker build . \
    --build-arg "HTTP_PROXY=http://proxy.example.com:8080/" \
    --build-arg "HTTPS_PROXY=http://proxy.example.com:8080/" \
    --build-arg "NO_PROXY=localhost,127.0.0.1,.example.com" \
    -t your/image:tag
```

复制

**注意**：无论是 `docker run` 还是 `docker build`，默认是网络隔绝的。如果代理使用的是 `localhost:3128` 这类，则会无效。这类仅限本地的代理，必须加上 `--network host` 才能正常使用。而一般则需要配置代理的外部IP，而且代理本身要开启 Gateway 模式。

