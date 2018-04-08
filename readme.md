### 逻辑
先尝试 nmap 探测端口是否存在漏洞

如果存在则 telnet 连接并关闭 vstack 配置。

### 依赖
需要 nmap 和 IPy
以 centos 为例
```
yum -y install epel-release
yum -y install python-pip
yum -y install nmap
pip install virtualenv

virtualenv ./env
source env/bin/activate
pip install -r requirement.txt
```

### 配置

在脚本的开始修改基本配置
```
threads = 128 # 并发数
ips = "192.168.12.0/24" # 扫码的地址段
password = "123456" # 密码
en_password = "654321" # enable 密码
#######################################
```

### 执行结果
```
# python disable_smart_install.py 
192.168.12.6 smart install disabled
 192.168.12.24 smart install disabled
192.168.12.18 smart install disabled
 192.168.12.20 smart install disabled
192.168.12.14 smart install disabled
192.168.12.22 smart install disabled
192.168.12.13 smart install disabled
192.168.12.17 smart install disabled
192.168.12.15 smart install disabled
192.168.12.21 smart install disabled
192.168.12.19 smart install disabled
192.168.12.23 smart install disabled
192.168.12.5 smart install disabled
192.168.12.11 smart install disabled
```