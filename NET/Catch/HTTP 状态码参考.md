

这个页面上是 HTTP 超文本传输协议的常见返回状态码的列表。根据互联网上的资料，尤其是相关 RFC 中的描述整理而成。我们会努力保证这个页面上的描述是准确无误的。如果对其中提到的内容有任何问题，欢迎到 V2EX 的 [HTTP](https://www.v2ex.com/go/http) 节点讨论。

## 1xx Informational 提示信息

### 100 Continue

服务器端确认已经收到请求头，向客户端发送 100 Continue，然后客户端就可以继续发送 request body（如果 request body 是必要的话，比如在 POST 请求中）。要触发服务器端的这种行为，那么在发起请求时就需要在 request header 中包括 Expect: 100-continue 这个请求头。如果服务器端在收到了 Expect: 100-continue 之后以 403 Forbidden 或者 405 Method Not Allowed 应答，那么客户端就不应该继续发送 request body。

如果服务器端以 417 Expectation Failed 应答，那么客户端应该在重新发起请求时不要带上 Expect 请求头，因为服务器端无法处理 Expect 请求头。

### 101 Switching Protocols

客户端向服务器端请求切换协议，服务器端同意切换。

### 102 Processing (WebDAV; [RFC 2518](https://tools.ietf.org/html/rfc2518#section-10.1))

一个 WebDAV 请求可能会包括多个涉及文件操作的子请求，需要耗费一些时间才能完成。102 状态码用于告知客户端请求已经收到并且正在处理，但是响应还没有准备好。这样可以防止客户端超时及认为请求没有成功发送。

### 103 Early Hints ([RFC 8297](https://tools.ietf.org/html/rfc8297))

在完整应答之前，用于向客户端先返回部分 HTTP 响应头用于提示重要资源的预先加载。

## 2xx Successful 请求成功

### 200 OK

表示请求成功完成的标准状态码。根据请求方法（request method）的不同，响应的内容也会不同。对于 GET 请求，那么响应内容就是被请求的资源。对于 POST 请求，响应内容通常是描述或者提供动作完成之后的结果。

### 201 Created

请求成功完成，并且结果是一个或者多个新的资源成功创建。如果创建成功的资源位于另外一个 URI 上，那么可以通过一个 Location 响应头部提示客户端跳转到新创建的 URI 上。

### 202 Accepted

请求被接受，但是处理还没有完成。通常用于客户端向服务器端提交批处理任务的情景。比如客户端提交了一个需要耗费很长时间计算的任务，服务器在接到请求但是计算结果还没有得出时可以返回 202 Accepted。之后如果客户端再次请求，数据已经计算完成时，再返回 200 OK。

### 203 Non-Authoritative Information ([RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.3.4))

203 状态码表示请求成功，但是来自源站的 200 OK 内容被中间的代理服务器做了修改。

### 204 No Content

服务器的响应中不会包括任何内容。但是响应头中可能会有一些有用的新信息，因此客户端依然可以以此更新本地缓存中的响应头。

### 205 Reset Content ([RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.3.6))

205 状态码表示服务器已经成功处理了请求，并且希望发起请求的客户端重置其「文档视图」，可能是一个用户可以输入数据的表单（form），记事本（notepad），或者画布（canvas）。这样当客户端收到这个状态码并重置之后，用户就可以继续输入其他新的数据。205 响应的正文部分应该是空的。即 Content-Length 应该为 0。

### 206 Partial Content

当客户端向服务器端通过 Range 请求头请求资源的部分内容，服务器成功响应时会使用 206 状态码。如果服务器端不支持 Range 请求，那么可能会以 416 Range Not Satisfiable 状态响应。

### 207 Multi-Status

### 208 Already Reported

### 226 IM Used

## 3xx Redirection 跳转

### 300 Multiple Choices

### 301 Moved Permanently

这次及将来所有的请求应该发送到服务器通过 Location 头部给出的新的 URI。意味着当前的这个地址已经永久性地转移到新地址。

### 302 Found (之前也被描述为 Moved Temporarily)

### 303 See Other (HTTP/1.1 新增)

### 304 Not Modified

### 305 Use Proxy (HTTP/1.1 中新增)

### 306 Switch Proxy

### 307 Temporary Redirect (HTTP/1.1 中新增)

### 308 Permanent Redirect ([RFC 7538](https://tools.ietf.org/html/rfc7538))

## 4xx Client Error 客户端错误

### 400 Bad Request

### 401 Unauthorized

### 402 Payment Required

### 403 Forbidden

### 404 Not Found

### 405 Method Not Allowed

### 406 Not Acceptable

### 407 Proxy Authentication Required

### 408 Request Timeout

### 410 Gone

### 411 Length Required ([RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.5.10))

### 412 Precondition Failed

### 413 Payload Too Large ([RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.5.11))

### 414 URI Too Long

### 415 Unsupported Media Type

### 416 Range Not Satisfiable

### 417 Expectation Failed

### 418 I'm a teapot ([RFC 2324](https://tools.ietf.org/html/rfc2324#section-2.3.2); [RFC 7168](https://tools.ietf.org/html/rfc7168#section-2.3.3))

作为一个茶壶，服务器拒绝被用来煮咖啡。

### 421 Misdirected Request

### 422 Unprocessable Entity

### 423 Locked

### 424 Failed Dependency

### 425 Too Early

### 426 Upgrade Required

### 428 Precondition Required

### 429 Too Many Requests

### 431 Request Header Fields Too Large

### 451 Unavailable For Legal Reasons

## 5xx Server Error 服务器端错误

服务器因为自身的问题而无法满足请求时会给出 5xx 系列的状态码。

### 500 Internal Server Error

### 501 Not Implemented

### 502 Bad Gateway

### 503 Service Unavailable

### 504 Gateway Timeout

### 505 HTTP Version Not Supported

服务器不支持被请求的 HTTP 协议版本。

### 506 Variant Also Negotiates

### 507 Insufficient Storage

### 508 Loop Detected

### 510 Not Extended

### 511 Network Authentication Required

## NGINX

非常流行的 Web 服务器软件 [NGINX](http://nginx.org/) 对 4xx 系列的状态进行了一些扩展，用于描述客户端请求中的问题。

NGINX 常用于反向代理其他 Web 服务，因此你有可能会在 NGINX 的日志中看到这些 NGINX 专有的状态码。

### 444 No Response

[NGINX 的内部状态码](http://nginx.org/en/docs/http/ngx_http_rewrite_module.html#return)，用于告知 Web 服务器不要向客户端返回任何信息（包括不会返回任何响应头部 response header）并立即关闭链接。

### 494 Request Header Too Large

客户端发送的请求头部（request header）太长。

### 495 SSL Certificate Error

对 400 Bad Request 的扩展，在客户端提供了不合法的证书时会返回 495 状态码。

### 496 SSL Certificate Required

对 400 Bad Request 的扩展，在需要客户端提供证书但是客户端未提供时会返回 496 状态码。

### 497 HTTP Request Sent to HTTPS Port

客户端错误地将 HTTP 明文请求发送到 HTTPS 端口时会收到 497 状态码。

### 499 Client Closed Request

在服务器发送响应之前，如果客户端就提前关闭了请求，那么这条请求会收到 499 状态码。

## Cloudflare

[Cloudflare](https://www.cloudflare.com/) 是互联网上非常流行的 CDN 服务，其对 5xx 系列状态码进行了扩展以描述其和源站（Origin）通讯时遇到的问题。

### 520 Web Server Returned an Unknown Error

源站服务器向 Cloudflare 返回了一个空的，或者未知的，或者无法解释的响应。

### 521 Web Server Is Down

源站服务器无法连接。

### 522 Connection Timed Out

Cloudflare 与源站服务器 TCP 握手过程超时。

### 523 Origin Is Unreachable

Cloudflare 无法找到源站服务器。比如，可能是在 Cloudflare DNS 中指定了错误的源站服务器地址。

### 524 A Timeout Occurred

Cloudflare 能够和源站完成 TCP 连接，但是在等待源站返回一个 HTTP 响应时超时。

### 525 SSL Handshake Failed

Cloudflare 在和配置了 SSL/TLS 的源站建立加密连接时失败。

### 526 Invalid SSL Certificate

源站的 SSL 证书无法通过 Cloudflare 的有效性验证。

Cloudflare could not validate the SSL certificate on the origin web server.

### 527 Railgun Error

527 错误意味着 Cloudflare 和源站的 Railgun 服务器的连接遇到问题。常见的原因是防火墙干扰或者网络丢包。

### 530

530 错误通常会和一个 [Cloudflare 专有的 1xxx 错误](https://support.cloudflare.com/hc/en-us/articles/360029779472-Troubleshooting-Cloudflare-1XXX-errors)同时给出。

## 中英对照词汇表

|英文|中文|
|---|---|
|Status Code|状态码|
|Request|请求|
|Response|响应|
|Request Method|请求方法|
|Request Header|请求头|
|Response Header|响应头|
|RFC|Request For Comment 缩写，互联网技术标准的定义文档|