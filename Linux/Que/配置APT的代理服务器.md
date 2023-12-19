
### 创建新的配置文件

1.需要在`/etc/apt/apt.conf.d/`目录下创建一个新的空文件。将其命名为`proxy.conf`,或者也可以任何名字。
```bash
sudo vim /etc/apt/apt.conf.d/proxy.conf
```

2.在配置文件中配置以下内容
```bash
Acquire {
  HTTP::proxy "http://proxy_server:port/";
  HTTPS::proxy "http://proxy_server:port/";
}
```
3.如果您的代理支持身份验证，并需要用户名/密码登录，使用如下配置：
```bash
Acquire::http::Proxy "http://user:password@proxy_server:port/";
```
