
# 使用 Docker 部署 Clash Premium

September 9, 2023 · 448 words · 3 min

- [订阅格式转换](https://blog.hellowood.dev/posts/%E4%BD%BF%E7%94%A8docker%E9%83%A8%E7%BD%B2clash-premium/#%E8%AE%A2%E9%98%85%E6%A0%BC%E5%BC%8F%E8%BD%AC%E6%8D%A2)
- [修改配置](https://blog.hellowood.dev/posts/%E4%BD%BF%E7%94%A8docker%E9%83%A8%E7%BD%B2clash-premium/#%E4%BF%AE%E6%94%B9%E9%85%8D%E7%BD%AE)
    - [基础配置](https://blog.hellowood.dev/posts/%E4%BD%BF%E7%94%A8docker%E9%83%A8%E7%BD%B2clash-premium/#%E5%9F%BA%E7%A1%80%E9%85%8D%E7%BD%AE)
    - [配置策略组](https://blog.hellowood.dev/posts/%E4%BD%BF%E7%94%A8docker%E9%83%A8%E7%BD%B2clash-premium/#%E9%85%8D%E7%BD%AE%E7%AD%96%E7%95%A5%E7%BB%84)
    - [配置规则集](https://blog.hellowood.dev/posts/%E4%BD%BF%E7%94%A8docker%E9%83%A8%E7%BD%B2clash-premium/#%E9%85%8D%E7%BD%AE%E8%A7%84%E5%88%99%E9%9B%86)
- [部署](https://blog.hellowood.dev/posts/%E4%BD%BF%E7%94%A8docker%E9%83%A8%E7%BD%B2clash-premium/#%E9%83%A8%E7%BD%B2)
- [客户端使用](https://blog.hellowood.dev/posts/%E4%BD%BF%E7%94%A8docker%E9%83%A8%E7%BD%B2clash-premium/#%E5%AE%A2%E6%88%B7%E7%AB%AF%E4%BD%BF%E7%94%A8)
    - [命令行](https://blog.hellowood.dev/posts/%E4%BD%BF%E7%94%A8docker%E9%83%A8%E7%BD%B2clash-premium/#%E5%91%BD%E4%BB%A4%E8%A1%8C)
    - [系统](https://blog.hellowood.dev/posts/%E4%BD%BF%E7%94%A8docker%E9%83%A8%E7%BD%B2clash-premium/#%E7%B3%BB%E7%BB%9F)

# 使用 Docker 部署 Clash Premium

Clash Premium 是 Clash 的闭源内核版本，相比 Clash 开源版本，最大的特点是支持规则集和代理服务订阅能力

## 订阅格式转换[[Proxy Provider Converter]]

大部分订阅是 base64 编码的节点，无法被 Clash 直接使用，因此需要进行订阅格式转换，具体请参考 [Clash 使用 Docker 部署](https://blog.hellowood.dev/posts/clash-%E4%BD%BF%E7%94%A8-docker-%E9%83%A8%E7%BD%B2/) 或使用在线工具直接转换：[https://acl4ssr-sub.github.io/](https://acl4ssr-sub.github.io/)

## 修改配置

### 基础配置

基础配置部分用于指定 Clash 的端口、代理模式等；使用 TUN 后可以代理 UDP 流量，开启 tracing 可以对 Clash 进行性能监控

- config.yaml

```yaml
port: 7890
socks-port: 7891
redir-port: 7892
allow-lan: true
mode: rule
log-level: info
# 控制端口
external-controller: :9090
# 访问密码，建议设置
secret: "123456"

# TUN 模式，用于代理 TCP、UDP、ICMP 流量
tun:
  enable: true
  stack: system
  auto-route: true
  auto-redir: true
  auto-detect-interface: true

# 用于性能分析
profile:
    tracing: true
```

### 配置策略组

代理提供方 `proxy-providers` 用于为策略组 `proxy-groups` 提供代理节点；这部分用于取代 Clash 中的 `proxies`

下面的配置中，`proxy-providers` 有两个提供者，类型都是 HTTP，即通过订阅链接进行拉取，同时指定了定时拉取时间和健康检查，用于检测节点的可用性; `proxy-groups` 指定了这个策略组的名称为 `PROXY`，用于为 `rule` 指定策略组名称；使用`proxy-providers` 中的 self 和 free 提供的节点作为策略组的节点；详细规则可以参考：[Proxy Groups 策略组](https://dreamacro.github.io/clash/zh_CN/configuration/outbound.html#proxy-groups-%E7%AD%96%E7%95%A5%E7%BB%84)

```yaml
proxy-providers:
  self:
    type: http
    url: "你的订阅地址"
    interval: 3600
    path: ./self.yaml
    health-check:
      enable: true
      interval: 600
      url: http://www.gstatic.com/generate_204
  # 来自 GitHub  https://github.com/Pawdroid/Free-servers    
  free:
    type: http
    url: "https://sub.xeton.dev/sub?target=clash&new_name=true&url=https%3A%2F%2Fghproxy.com%2Fhttps%3A%2F%2Fraw.githubusercontent.com%2FPawdroid%2FFree-servers%2Fmain%2Fsub&insert=false"
    interval: 3600
    path: ./free.yaml
    health-check:
      enable: true
      interval: 600
      # lazy: true
      url: http://www.gstatic.com/generate_204

proxy-groups:
  - name: "PROXY"
    type: url-test
    use:
      - self
      - free
    url: 'http://www.gstatic.com/generate_204'
    interval: 300
```

### 配置规则集

规则集用于决定流量是否走 Clash 代理，在 Clash 版本中，必须挨个列出处理规则，导致配置非常臃肿，而且不好维护；在 premium 版本中，可以通过 rule-provider 指定订阅的规则集；以下规则集来自 [https://github.com/Loyalsoldier/clash-rules](https://github.com/Loyalsoldier/clash-rules)；

`rule-providers` 部分通过分组的方式指定了规则的处理方式，便于管理；

`rules` 为 `rule-providers` 中的 rule-set 指定了策略组；如`RULE-SET,icloud,DIRECT` 为 icloud 这个规则集下面的内容指定了 DIRECT 的处理方式，即直接访问；`RULE-SET,google,PROXY` 为 google 这个规则集下面的内容指定了名为 `PROXY`的策略组进行代理

最后一行 `MATCH,DIRECT` 表示未匹配到规则的使用 DIRECT 方式，即直接访问

```yaml
rule-providers:
  reject:
    type: http
    behavior: domain
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/reject.txt"
    path: ./ruleset/reject.yaml
    interval: 86400

  icloud:
    type: http
    behavior: domain
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/icloud.txt"
    path: ./ruleset/icloud.yaml
    interval: 86400

  apple:
    type: http
    behavior: domain
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/apple.txt"
    path: ./ruleset/apple.yaml
    interval: 86400

  google:
    type: http
    behavior: domain
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/google.txt"
    path: ./ruleset/google.yaml
    interval: 86400

  proxy:
    type: http
    behavior: domain
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/proxy.txt"
    path: ./ruleset/proxy.yaml
    interval: 86400

  direct:
    type: http
    behavior: domain
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/direct.txt"
    path: ./ruleset/direct.yaml
    interval: 86400

  private:
    type: http
    behavior: domain
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/private.txt"
    path: ./ruleset/private.yaml
    interval: 86400

  gfw:
    type: http
    behavior: domain
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/gfw.txt"
    path: ./ruleset/gfw.yaml
    interval: 86400

  tld-not-cn:
    type: http
    behavior: domain
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/tld-not-cn.txt"
    path: ./ruleset/tld-not-cn.yaml
    interval: 86400

  telegramcidr:
    type: http
    behavior: ipcidr
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/telegramcidr.txt"
    path: ./ruleset/telegramcidr.yaml
    interval: 86400

  cncidr:
    type: http
    behavior: ipcidr
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/cncidr.txt"
    path: ./ruleset/cncidr.yaml
    interval: 86400

  lancidr:
    type: http
    behavior: ipcidr
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/lancidr.txt"
    path: ./ruleset/lancidr.yaml
    interval: 86400

  applications:
    type: http
    behavior: classical
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/applications.txt"
    path: ./ruleset/applications.yaml
    interval: 86400
rules:
  - RULE-SET,google,PROXY
  - RULE-SET,proxy,PROXY
  - RULE-SET,telegramcidr,PROXY
  - RULE-SET,applications,DIRECT
  - RULE-SET,private,DIRECT
  - RULE-SET,reject,REJECT
  - RULE-SET,icloud,DIRECT
  - RULE-SET,apple,DIRECT
  - RULE-SET,direct,DIRECT
  - RULE-SET,lancidr,DIRECT
  - RULE-SET,cncidr,DIRECT
  - GEOIP,LAN,DIRECT
  - GEOIP,CN,DIRECT
  - MATCH,DIRECT
```

## 部署

使用 Docker Compose 部署 Clash 和 yacd 面板

- docker-compose.yaml

需要将上面的配置合并到 `config.yaml`文件中，放到 `data/config.yaml`路径下，用于挂载到容器 `/root/.config/clash` 目录下，后续的拉取到的规则集和配置文件都会写到这个目录下

```yaml
version: "3"

services:
  clash:
    image: dreamacro/clash-premium
    container_name: clash
    hostname: clash
    privileged: true
    restart: unless-stopped
    ports:
      - 7890:7890
      - 7891:7891
      - 7892:7892
      - 9090:9090
    volumes:
      - ./data:/root/.config/clash
    environment:
      - TZ=Asia/Shanghai

  yacd:
    image: ghcr.io/haishanh/yacd:master
    container_name: yacd
    hostname: yacd
    restart: unless-stopped
    ports:
      - 9091:80
    environment:
      - TZ=Asia/Shanghai
    depends_on:
      - clash
```

## 客户端使用

通过容器方式部署的 Clash 可以以代理的方式使用，在手机/电脑或者应用程序中配置代理即可

### 命令行

开启代理

```bash
export https_proxy=http://192.168.2.2:7890 
export http_proxy=http://192.168.2.2:7890 
export all_proxy=socks5://192.168.2.2:7891
```

关闭代理

```bash
unset http_proxy
unset https_proxy
unset all_proxy
```

### 系统

在网络-代理中添加配置，指定 HTTP/HTTPS/SOCKS 代理为配置的代理即可

![homelab-clash-proxy-config-macos.png](https://img.hellowood.dev/picture/homelab-clash-proxy-config-macos.png)