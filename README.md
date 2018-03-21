# nirBot
nir的全能型日用机器人

安装ss
```shell
$apt-get update
$apt-get install software-properties-common -y
$add-apt-repository ppa:max-c-lv/shadowsocks-libev -y
$apt-get update
$apt install shadowsocks-libev
$ss-local -s ******** -p 1 -l 1080 -k "*****" -m chacha20-ietf-poly1305
```
下载机器人
```shell
$pip3 install --upgrade pip
$pip3 install itchat
$pip3 install python-telegram-bot
$apt-get install git
$git clone https://github.com/Niracler/nirBot.git
```
安装代理
```shell
$apt-get install proxychains
$vim /etc/proxychains.conf
$vim /usr/bin/proxychains 
# socks5    127.0.0.1    1080
$git clone https://github.com/rofl0r/proxychains-ng.git 
#如果clone 不下来就下载zip 我就存在下载不动的情况  
  
$cd proxychains-ng  
  
$./configure --prefix=/usr --sysconfdir=/etc #此处的prefix路径一定是/usr 如果换成其他会出现$couldnt locate libproxychains4.so  
$make #需要gcc环境  
$make install  
$sudo make install-config (installs proxychains.conf)  
```
启动机器人
```shell
$cd nirBot/
$proxychains4 python3 main.py
```

下面是关于虚拟环境的用法

启动虚拟环境
```
$ source venv/bin/activate　
```

安装python包
```
$ pip install -r requirements.txt
```

