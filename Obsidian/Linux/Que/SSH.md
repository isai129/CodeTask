要使用SSH协议在服务器之间拷贝文件夹，可以采用以下步骤:

1. 打开终端或命令行窗口，确保本地和目标服务器都已经安装了SSH客户端和服务器。
2. 使用SSH协议连接目标服务器，通过输入以下命令行来连接：
    
    ```
    ssh username@server_ip_address
    ```
    
    这里的`username`是目标服务器的用户名，`server_ip_address`是目标服务器的IP地址。
    
3. 输入目标服务器的密码进行身份验证，成功登录到目标服务器。
4. 使用`cd`命令切换到要拷贝的文件夹所在的路径。例如，如果要拷贝`/home/username/source_folder`文件夹，可以输入以下命令：
    
    ```
    cd /home/username/source_folder
    ```
    
5. 使用`scp`命令来拷贝文件夹，输入以下命令行：
    
    ```
    scp -r source_folder_path username@target_server_ip:target_folder_path
    ```
    
    这里的`source_folder_path`是本地文件夹的路径，`target_server_ip`是目标服务器的IP地址，`target_folder_path`是目标文件夹的路径。请注意使用`-r`参数来确保递归拷贝文件夹及其所有内容。
    
6. 输入目标服务器的密码进行身份验证，开始拷贝文件夹。
7. 完成拷贝后，终端或命令行窗口会显示拷贝过程的详细信息。