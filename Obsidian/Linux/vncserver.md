```bash

vnc服务器用法：

   可以在 vncserver(1) 中找到帮助，或者通过使用
      -help 如果指定，则转储此帮助消息。
      -h 是帮助的别名。
      -？ 是帮助的别名。
  
   要启动 VNC 服务器，请使用 vncserver [options] [-- session]
     [:<number>] 指定要使用的 X11 显示器。
     [-display <值>] 是 :<number> 的别名。
     [-fg] 如果启用，vncserver 将停留在前台。
     [-useold] 如果给定，仅当 VNC 服务器尚未运行时才启动。
     [-verbose] 如果指定，则启用调试输出。
     [-dry-run] 如果启用，则不会执行任何实际操作，只会执行将要执行的操作的模拟。
     [-PAMService <值>] 指定 PAM 密码验证的服务名称，在安全类型为 Plain、TLSPlain 或
                              X509普通。 默认情况下，如果存在则使用 vnc，否则使用 Tigervnc。
     [-pam_service <值>] 是 PAMService 的别名。
     [-PlainUsers <值>] 指定安全类型 Plain、TLSPlain 和 X509Plain 的授权用户列表。
     [-localhost [yes|no]] 如果启用，VNC 将仅接受来自 localhost 的连接。
     [-desktop <值>] 指定 VNC 桌面名称。
     [-rfbport <number>] 提供用于 RFB 协议的 TCP 端口。
     [-rfbunixpath <值>] 指定用于 RFB 协议的 Unix 域套接字的路径。
     [-rfbunixmode <value>] 指定Unix域套接字的模式，默认为0600。
     [-X509Key <value>] 表示 X509 证书密钥文件（PEM 格式）。 这由安全类型 X509None、X509Vnc 和 X509Plain 使用。
     [-X509Cert <value>] 表示对应的X509证书（PEM格式）。
     [-PasswordFile <值>] 指定安全类型 VncAuth、TLSVnc 和 X509Vnc 的密码文件。 默认情况下，使用 ~/.vnc/passwd。
     [-rfbauth <值>] 是PasswordFile 的别名。
     [-SecurityTypes <value>] 指定要提供的安全类型的逗号列表（None、VncAuth、Plain、TLSNone、TLSVnc、TLSPlain、X509None、X509Vnc、
                              X509 普通）。 默认情况下，仅提供 VncAuth。
     [-geometry <value>] 指定桌面几何形状，例如 <width>x<height>。
     [-wmDecoration <value>] 如果指定，则将几何图形缩小给定的 <width>x<height> 值。
     [-xdisplaydefaults] 如果给定，则从正在运行的 X 服务器获取几何图形和像素格式。
     [-xstartup [<value>]] 指定为 Xtigervnc 启动 X11 会话的脚本。
     [-noxstartup] 禁用 X 会话启动。
     [-depth <number>] 指定桌面的位深度，例如 16、24 或 32。
     [-pixelformat <值>] 定义 X11 服务器像素格式。 有效值为 rgb888、rgb565、bgr888 或 bgr565。
     [-autokill [yes|no]] 如果启用（默认），VNC 服务器将在其 X 会话终止后被终止。
     [-fp <值>] 指定以冒号分隔的字体位置列表。
     [Xtigervnc 选项...] 有关详细信息，请参见 Xtigervnc(1)。
     [-- <session>] 指定以命令或会话名称启动的 X11 会话。
  
   要列出用户的所有活动 VNC 服务器，请使用 vncserver
      -list 如果提供，则列出用户的所有活动 VNC 服务器。
     [:<number>] 指定要使用的 X11 显示器。
     [-display <值>] 是 :<number> 的别名。
     [-rfbport <number>] 提供用于 RFB 协议的 TCP 端口。
     [-rfbunixpath <值>] 指定用于 RFB 协议的 Unix 域套接字的路径。
     [-cleanstale] 如果提供，则清除用户的过时 VNC 服务器实例的 pid 和锁定文件。
  
   要终止 VNC 服务器，请使用 vncserver
      -kill 如果提供，则终止用户指定的 VNC 服务器。
     [:<number>] 指定要使用的 X11 显示器。
     [-display <值>] 是 :<number> 的别名。
     [-rfbport <number>] 提供用于 RFB 协议的 TCP 端口。
     [-rfbunixpath <值>] 指定用于 RFB 协议的 Unix 域套接字的路径。
     [-dry-run] 如果启用，则不会执行任何实际操作，只会执行将要执行的操作的模拟。
     [-verbose] 如果指定，则启用调试输出。
     [-clean] 如果指定，终止的 VNC 会话的日志文件也将被删除。
  
   要转储版本信息，请使用 vncserver
     [-version] 转储底层 Xtigervnc VNC 服务器的版本信息。
  
  
   如需进一步帮助，请参阅 vncserver(1) 和 Xtigervnc(1) 手册页。


```