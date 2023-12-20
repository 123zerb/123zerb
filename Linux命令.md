[TOC]

# Linux

## 系统安装

镜像下载地址

https://mirrors.163.com/

https://mirrors.163.com/centos/7.9.2009/isos/x86_64/

## 常用命令

### System

```shell script
#查看帮助命令，可以查看大部分命令的详细帮助文档
man
man docker
man cat

#关机
#立即关机
shutdown -h now
#重启
reboot
shutdown -r 

#查看内核版本
uname -a
#查看系统中全部的内核RPM包
rpm -qa | grep kernel
#查看系统版本
cat /proc/version
#查看系统发行版
lsb_release -a
cat /etc/redhat-release
cat /etc/issue
#查看cpu信息
cat /proc/cpuinfo
grep "model name" /proc/cpuinfo | cut -f2 -d:
#查看系统启动时间
last reboot
last reboot |head -1

#修改密码
passwd root

#软连接

# 查看文件最大打开数量
$ ulimit -Sn
-----
1024
-----
$ ulimit -Hn
-----
4096
-----
# 文件末尾添加
$ nano /etc/security/limits.conf
----
# End of file 
* soft nofile 65536 
* hard nofile 65536 
* soft nproc 131072 
* hard nproc 131072
----
# 修改文件/etc/secruity/limits.d/20-nproc.conf
* soft nproc 65535

# 重启服务器
$ reboot
# 查看更新后配置
$ ulimit -Sn
-----
65536
-----
$ ulimit -Hn
-----
65536
-----


#显示当前路径
pwd

#执行jar包
nohup  java -jar cloudoforce-auth.jar > /home/cloud_cof/app/logs/cloudoforce-auth_`date "+%Y-%m-%d"`_.log 2>&1 &

#修改时钟同步
ntpdate -u 192.168.1.10

#修改时钟同步
nano /etc/ntp.conf

server 192.168.1.125 prefer

#使用chrony取代ntp进行时钟同步
nano /etc/chrony.conf
server 192.168.1.125 iburst

#查看chrony同步
chronyc sources -v
#使用chrony立即同步时间
chronyc -a makestep

#使用定时任务同步时间
crontab -e
#meishifenzhong
0-59/10 * * * * /usr/sbin/ntpdate 192.168.1.12

#查看硬盘占用
df -h
#查看内存占用
free -h
#查看文件大小以M为单位显示
ls -lh
#查看文件夹大小
#查看目录总大小
du -sh
#可以查看当前目录下各文件、文件夹的大小，这个比较实用。
du -h –-max-depth=1 *

#查看cpu信息
cat /proc/cpuinfo

# 临时关闭swap分区
swapoff -a
# 要永久禁掉swap分区，打开如下文件注释掉swap那一行
nano /etc/fstab
#/dev/mapper/cl-swap     swap                    swap    defaults        0 0


# 临时关闭selinux
getenforce
setenforce 0
# 将 SELinux 设置为 permissive 模式（相当于将其禁用）
sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
# 永久关闭
nano /etc/selinux/config  
# 改：7SELINUX=enforcing     #前面的7，表示文档中第7行。方便你查找
# 为：7SELINUX=disabled
reboot

#关掉所有主机上的防火墙, 并禁止防火墙自启动
systemctl stop firewalld
systemctl disable firewalld
#防火墙开放指定端口
firewall-cmd --zone=public --add-port=端口号/tcp --permanent
#防火墙开放指定端口范围
firewall-cmd --zone=public --add-port=端口号-端口号/tcp --permanent
#添加指定需要开放的端口： 
firewall-cmd --add-port=端口号/tcp --permanent 
#防火墙关闭指定端口
firewall-cmd --remove-port=端口号/tcp --permanent
#重载入添加的端口： 
firewall-cmd --reload 
#查询指定端口是否开启成功：
firewall-cmd --query-port=端口号/tcp
#查看已开放端口
firewall-cmd --list-ports

#查看端口号
netstat  -anp  |grep   端口号
lsof -i:端口号

#查看服务是否开机启动
systemctl list-unit-files | grep nginx

#查看服务状态
systemctl status firewalld

#CentOS修改hostname
nano /etc/hostname
#CentOS修改hostname 不重启生效
hostname <newHostname>
#CentOS修改hosts
nano /etc/hosts

#.sh文件添加执行权限
#给所有用户添加执行权限
chmod a+x file.sh 
#如果给文件所有者添加可执行权限:
chmod u+x file.sh
#如果给所在组添加可执行权限:
chmod g+x file.sh
#如果给所在组以外的人添加可执行权限:
chmod o+x file.sh

#动态查看服务运行日志
journalctl -u etcd -f
journalctl -u v2ray -f

ExecStart=/usr/local/bin/v2ray -config /etc/v2ray/config.json

#关闭swap
swapoff -a
cat /etc/fstab #注释掉最后一行
#/dev/mapper/cl-swap     swap                    swap    defaults        0 0

#查看环境变量
export
printenv

#scp命令
scp [可选参数] file_source file_target 
#参数：
-r 递归复制整个目录。
#示例：
scp /root/.ssh/authorized_keys root@tt-sc2:/root/.ssh
scp -r /root/.m2 root@tt-sd2:/root/

#ssh
#debian安装ssh
sudo apt-get install openssh-server
#允许使用root账户进行ssh连接
nano /etc/ssh/sshd_confg
----
#添加：
PermitRootLogin yes
PubkeyAuthentication yes
----
#ssh连接
ssh root@tt-sd2
#使用ssh远程输入命令
ssh root@tt-sd2 "source /etc/profile"
#debug模式
ssh -vvv [host]
ssh -v [host]

#日志查看相关命令
#显示file文件里匹配nick字串前后50行
cat -n info-2021-10-20.0.log |grep -n -B50 -A50 nick

#关闭tab键提示音
vim /etc/inputrc
# set bell-style none ,这里取消注释
set bell-style none
# source使生效
source /etc/inputrc
# 退出重新登录shell

#使用socket发送信息
nc -lk [port]
nc -lk

#查找文件
find <dir> -name <fileName>

#解压缩
tar -zxvf
#压缩
tar -cvf test.tar .
#压缩排除
tar --exclude=/test.tar -cvf test.tar .

#查看linux全部用户
cat /etc/passwd |cut -f 1 -d :

#导出文件树
#只有文件夹
tree >> D:/tree.txt
#包括文件夹和文件
tree /f >> D:/tree.txt

#统计当前目录下文件的个数（不包括目录）
ls -l | grep "^-" | wc -l
#统计当前目录下文件的个数（包括子目录）
ls -lR| grep "^-" | wc -l


```

### NC

```
# 参数说明：
-g<网关> 设置路由器跃程通信网关，最多可设置8个。
-G<指向器数目> 设置来源路由指向器，其数值为4的倍数。
-h 在线帮助。
-i<延迟秒数> 设置时间间隔，以便传送信息及扫描通信端口。
-l 使用监听模式，管控传入的资料。
-n 直接使用IP地址，而不通过域名服务器。
-o<输出文件> 指定文件名称，把往来传输的数据以16进制字码倾倒成该文件保存。
-p<通信端口> 设置本地主机使用的通信端口。
-r 乱数指定本地与远端主机的通信端口。
-s<来源位址> 设置本地主机送出数据包的IP地址。
-u 使用UDP传输协议。
-v 显示指令执行过程。
-w<超时秒数> 设置等待连线的时间。
-z 使用0输入/输出模式，只在扫描通信端口时使用。
```

```shell
# nc安装
yum install nc -y
# 开启端口监听
nc -l [port]
```



### GIT

```shell
#git 
#修改远程仓库
git remote set-url origin [url]
#删除远程仓库
git remote rm origin
#
git remote add origin [url]
#proxy配置
#socks5
git config --global http.proxy socks5://127.0.0.1:10808 
git config --global https.proxy socks5://127.0.0.1:10808
#http
git config --global http.proxy http://192.168.0.9:10809
git config --global https.proxy http://192.168.0.9:10809
#取消配置
git config --global --unset http.proxy
git config --global --unset https.proxy
#查看当前代理
git config --global --get http.proxy
git config --global --get https.proxy

#设置用户名
git config --global user.name "username"
git config user.name "username"
#查看用户名
git config --global user.name
git config user.name

#设置邮箱
git config --global user.email "email"
git config user.email "email"
#查看邮箱
git config --global user.email
git config user.email

#长路径限制
git config --global core.longpaths true

#拉取远程仓库所有分支代码
git clone xxx
git branch -r | grep -v 'HEAD' | while read remote; do git branch --track "${remote#origin/}" "$remote"; done
git fetch --all
git pull --all

#首次clone拉取全部子模块
git clone --recurse-submodule <git url>
#首次拉取子模块
git submodule update --init --recursive
#更新子模块
git submodule update --recursive --remote
```



### YUM

```shell
yum install epel-release net-tools vim nano unzip zip wget ftp -y
#清除软件包缓存
yum clean all
#缓存源
yum mackecache
#升级所有包同时，也升级软件和系统内核；
yum -y update
#只升级所有包，不升级软件和系统内核，软件和内核保持原样。
yum -y upgrade
#查看哪些包可以更新
yum check-update
#使用YUM查找软件包 
yum search 
#列出所有可安装的软件包 
yum list <name>
#搜索源中可安装的软件包（更全）
yum list all |grep <name>
#搜索所有包(最全)
yum list <name> --showduplicates | sort -r
yum list all --showduplicates | grep <name> |sort -r
#列出所有可更新的软件包 
yum list updates 
#列出所有已安装的软件包 
yum list installed 
yum list installed |grep <name>
#列出所有已安装但不在 Yum Repository 内的软件包 
yum list extras 
#使用YUM获取软件包信息 
yum info 
#列出所有软件包的信息 
yum info 
#列出所有可更新的软件包信息 
yum info updates 
#列出所有已安装的软件包信息 
yum info installed 
#列出所有已安装但不在 Yum Repository 内的软件包信息 
yum info extras 
#列出软件包提供哪些文件 
yum provides
#安装不同版本rpm包
yum list nginx --showduplicates #查看所有包

nginx-mod-http-geoip.x86_64            1:1.22.1-1.amzn2.0.2          amzn2extra-nginx1
nginx-mod-http-geoip.x86_64            1:1.22.1-1.amzn2.0.2          @amzn2extra-nginx1

yum -y install [服务名]-[版本号]  #这里要注意删除1: 也要拼接.x86_64
yum install nginx-mod-http-geoip-1.22.0-1.amzn2.0.2.x86_64
yum install nginx-1.16.1-1.el7.ngx.x86_64 #所需版本对应的包名
yum install kubelet-1.22.2-0
#yum删除
yum remove
#下载rpm包到本地
yumdownloader --resolve --destdir=[保存路径] [包名，也可以指定版本号]
yumdownloader --resolve --destdir=/home/app/tt nginx-mod-http-geoip-1.22.0-1.amzn2.0.2.x86_64
#查看安装的文件
rpm -ql 
rpm -qa|grep <name>
#rpm安装
rpm -ivh 包路径/包名
#rpm升级
rpm -Uvh nginx-mod-http-geoip-1.22.0-1.amzn2.0.2.x86_64.rpm
#卸载软件本体不卸载依赖
rpm -e --nodeps <name>
```

### apt-get

```shell
# 更新源
apt update
# 查找
apt search <keyword>
# 已安装的软件
apt list --installed
# 更新指定软件
apt update <package_name>

# 安装ping
apt-get install iputils-ping
```



### 集群配置免密登录

```shell script
#在每台机器上执行：
[root@tt-sc1 .ssh]# ssh-keygen -t rsa
[root@tt-sc2 .ssh]# ssh-keygen -t rsa
[root@tt-sc3 .ssh]# ssh-keygen -t rsa
#主节点：
[root@tt-sc1 .ssh]# cp id_rsa.pub authorized_keys
#所有从节点：
[root@tt-sc2 .ssh]# ssh-copy-id -i /root/.ssh/id_rsa.pub root@tt-sc1
[root@tt-sc3 .ssh]# ssh-copy-id -i /root/.ssh/id_rsa.pub root@tt-sc1
#将主节点的authorized_keys分发到所有机器
[root@tt-sc1 .ssh]# scp /root/.ssh/authorized_keys root@tt-sc2:/root/.ssh
[root@tt-sc1 .ssh]# scp /root/.ssh/authorized_keys root@tt-sc3:/root/.ssh
```

### 配置JDK环境变量

```Shell script
#删除原来的openJDK
#查看rpm安装的java环境
[root@tt-sc1 ~]# rpm -qa|grep java
#全部删除
[root@tt-sc1 ~]# yum -y remove java-1.7.0-openjdk-headless-1.7.0.221-2.6.18.1.el7.x86_64
#解压jdk
[root@tt-sc1 ~]# tar -zxvf jdk-8u161-linux-x64.tar.gz
#移动目录
[root@tt-sc1 ~]# mv jdk1.8.0_161/ /usr/local/
#配置环境变量
[root@tt-sc1 ~]# nano /etc/profile
#在文件末尾添加：
export JAVA_HOME=/usr/local/jdk1.8.0_161
export JRE_HOME=$JAVA_HOME/jre
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.$
export PATH=$PATH:/opt/bin:/sbin:$JAVA_HOME/bin:$PATH
export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
#使配置生效
[root@tt-sc1 ~]# source /etc/profile

```

### 配置网卡重启自动链接

```Shell script
[root@tt-sc1 ~]# cd /etc/sysconfig/network-scripts/
#编辑
[root@tt-sc1 network-scripts]# nano ifcfg-ens33
#将
ONBOOT=no
#改为
ONBOOT=yes
#重启网卡
[root@tt-sc1 network-scripts]# service network restart
```

### 安装maven

```shell script
#下载安装包<http://maven.apache.org/download.cgi>  [apache-maven-3.6.3-bin.tar.gz]
#上传到服务器
#解压
[root@tt-sc1 ~]# tar -zxvf apache-maven-3.6.3-bin.tar.gz
#复制到 /usr/local 目录下
[root@tt-sc1 ~]# mv  apache-maven-3.6.3/ /usr/local/
#配置环境变量
#配置环境变量
[root@tt-sc1 ~]# nano /etc/profile
#在文件末尾添加：
export MAVEN_HOME=/usr/local/apache-maven-3.6.1
#在export PATH中添加
$MAVEN_HOME/bin
#使配置生效
[root@tt-sc1 ~]# source /etc/profile
```

### 安装Postgresql

默认安装的postgresql不允许外部链接访问。

```shell
# 修改配置文件允许外部链接访问
$ nano /var/lib/pgsql/data/pg_hba.conf
# 末尾添加一行
----
host  all   all           0.0.0.0/0  md5
----
#重启
$ systemctl restart postgresql.service
```

默认用户名密码：postgres/postgres

```shell
# 默认链接数据库需要使用postgres用户
$ sudo -u postgres psql
psql (9.2.24)
Type "help" for help.
postgres=# ALTER USER postgres WITH PASSWORD 'postgres';
```



### 安装git

可直接使用yum安装也可以用源码安装

```shell script
#yum安装 yum install git
#源码安装 https://github.com/git/git/releases
#下载git-2.30.1.tar.gz
#删除老版本git
[root@master home]# yum -y remove git
#安装编译所需
[root@master home]# yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel gcc perl-ExtUtils-MakeMaker
#解压
[root@master home]# tar -zxvf git-2.30.1.tar.gz 
[root@master home]# cd git-2.30.1/
#编译
[root@master git-2.30.1]# make prefix=/usr/local/git all
#安装 安装目录/usr/local/git
[root@master git-2.30.1]# make prefix=/usr/local/git install
#修改环境变量
[root@master git-2.30.1]# nano /etc/profile
#export PATH添加/usr/local/git/bin
export PATH=$PATH:/opt/bin:/sbin:$JAVA_HOME/bin:$MAVEN_HOME/bin:/usr/local/git/bin:$PATH
#使配置生效
[root@master git-2.30.1]# source /etc/profile
#验证
[root@master git-2.30.1]# git --version

```

### awk命令

awk是**行处理器**

```shell
# 打印一行的第三个字段
awk '{print $3}'
```

### conda 命令

```shell
# 创建环境
conda create [env]
# 环境列表
conda env list
# 切换环境
conda activate [env]

# 配置环境的环境变量，如果切换到没有指定这个环境变量的环境则保留值
conda env config vars set LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/app/.conda/envs/let/lib
```

### less命令

```shell
less [文件] 
/[搜索文本]
```



## 操作系统密码修改

### 需求

1. 密码复杂度要求
2. 密码定期更换
3. 登录失败处理

### 操作系统密码

#### 修改账户密码策略

```shell
#密码有效期
#修改：/etc/login.defs
PASS_MAX_DAYS  #密码最长有效期
PASS_MIN_DAYS  #密码最短存留期
PASS_MIN_LENS  #密码长度最小值
PASS_WARN_AEG  #密码有效期警告
#修改为如下配置：
PASS_MAX_DAYS 30    #密码有效期为30天
PASS_MIN_DAYS 1     #密码最短修改时间为1天
PASS_MIN_LEN 8      #密码最小长度为8位
PASS_WARN_AGE 7   #密码过期提前7天提示修改

#以上只对之后新增的用户有效，如果要修改已存在的用户密码规则，需要使用chage命令
#修改已有账户密码时间
chage -M 30 -m 1 -W 7 <username>
-m：密码可更改的最小天数。为零时代表任何时候都可以更改密码。
-M：密码保持有效的最大天数。
-w：账户密码到期前，提前收到警告信息的天数。
-E：帐号到期的日期。过了这天，此帐号将不可用。
-d：上一次更改的日期。
-i：停滞时期。如果一个密码已过期这些天，那么此帐号将不可用。
-l：例出当前的设置。由非特权账户来确定他们的密码或帐号何时过期。

#测试操作
#备份
cp login.defs login.defs.bak
#修改/etc/login.defs
PASS_MAX_DAYS   7    
PASS_MIN_DAYS   1
PASS_MIN_LEN    8
PASS_WARN_AGE   7


[root@master ~]# chage -l xm
最近一次密码修改时间					：6月 02, 2021
密码过期时间					：6月 09, 2021
密码失效时间					：从不
帐户过期时间						：从不
两次改变密码之间相距的最小天数		：1
两次改变密码之间相距的最大天数		：7



#密码复杂度 方法1
#修改：/etc/pam.d/system-auth
password requisite pam_cracklib.so #行替换成如下：
password  requisite pam_cracklib.so retry=3  difok=3 minlen=8 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1

retry 尝试次数 
difok 最少不同字符 
minlen 最小密码长度 
ucredit 最少大写字母 
lcredit 最少小写字母 
dcredit 最少数字 
ocredit 最少特殊符号

#密码复杂度 方法2 （使用这个方法）
#如果/etc/pam.d/system-auth中有下面这一行，使用这个方式：
password    requisite     pam_pwquality.so try_first_pass local_users_only retry=3 authtok_type=
#修改：/etc/security/pwquality.conf
difok=3 
minlen=8 
dcredit=-1 
ucredit=-1 
lcredit=-1 
ocredit=-1

retry=N：定义登录/修改密码失败时，可以重试的次数；
Difok=N：定义新密码中必须有几个字符要与旧密码不同。但是如果新密码中有1/2以上的字符与旧密码不同时，该新密码将被接受；
minlen=N：定义用户密码的最小长度；
dcredit=N：定义用户密码中必须包含多少个数字；
ucredit=N：定义用户密码中必须包含多少个大写字母；
lcredit=N：定义用户密码中必须包含多少个小些字母；
ocredit=N：定义用户密码中必须包含多少个特殊字符（除数字、字母之外）；
其中 =-1表示，至少有一个

#测试操作
#备份
cp pwquality.conf pwquality.conf.bak
#编辑
nano pwquality.conf
#测试
#创建新用户
adduser test
#设置密码测试：
passwd test
----
更改用户 test 的密码 。
新的 密码：123456
无效的密码： 密码包含少于 1 的大写字母
重新输入新的 密码：
抱歉，密码不匹配。
新的 密码：T123456
无效的密码： 密码包含少于 1 的小写字母
重新输入新的 密码：
抱歉，密码不匹配。
新的 密码：Tt123456
无效的密码： 密码包含少于 1 的非字母或数字字符
重新输入新的 密码：
抱歉，密码不匹配。
新的 密码：Tt123456.
无效的密码： 密码未通过字典检查 - 过于简单化/系统化
重新输入新的 密码：
抱歉，密码不匹配。
新的 密码：Tt20210602.
重新输入新的 密码：Tt20210602.
passwd：所有的身份验证令牌已经成功更新。

```

### 登录失败处理

```shell
#口令至少5次内不能重复
#修改：/etc/pam.d/system-auth
#在password    sufficient    pam_unix.so这一行最后添加 remember=5
password    sufficient    pam_unix.so sha512 shadow nullok try_first_pass use_authtok
remember=5
auth required pam_tally2.so onerr=fail deny=3 unlock_time=1800 even_deny_root root_unlock_time=30

#限制本地登录失败次数
#修改：/etc/pam.d/login
#在第二行增加如下内容
auth  required  pam_tally2.so  deny=3  unlock_time=1800 even_deny_root root_unlock_time=1800

#限制ssh登录失败次数
#修改：/etc/pam.d/sshd
#在第二行增加如下内容：
auth  required  pam_tally2.so  deny=3  unlock_time=1800 even_deny_root root_unlock_time=1800

#参数解释：
even_deny_root  也限制root用户； 
deny            设置普通用户和root用户连续错误登陆的最大次数，超过最大次数，则锁定该用户 
unlock_time      设定普通用户锁定后，多少时间后解锁，单位是秒； 
root_unlock_time  设定root用户锁定后，多少时间后解锁，单位是秒；

# 在#%PAM-1.0的下面，即第二行，添加内容，一定要写在前面。如果写在后面，虽然用户被锁定，但是只要用户输入正确的密码，还是可以登录的。
#此处使用的是 pam_tally2 模块，如果不支持 pam_tally2 可以使用 pam_tally 模块。另外，不同的pam版本，设置可能有所不同，具体使用方法，可以参照相关模块的使用规则。
#用户锁定期间，无论在输入正确还是错误的密码，都将视为错误密码，并以最后一次登录为锁定起始时间，若果用户解锁后输入密码的第一次依然为错误密码，则再次重新锁定。

#查看用户登录失败的次数（以root为例）
pam_tally2 --user root
#解锁指定用户（以root为例）
pam_tally2 -r -u root




#测试操作
#限制本地登录失败次数
#备份
cp /etc/pam.d/login /etc/pam.d/login.bak
#修改 这里测试先不限制root用户
nano /etc/pam.d/login
----
#%PAM-1.0
auth  required  pam_tally2.so  deny=3  unlock_time=1800
----
#本地登录失败三次后使用正确密码登录成功...
#尝试其他方式修改：
#经过多次尝试发现/etc/pam.d/login这个文件限制的是本地tty登录。图形界面登录不受限制。


#限制ssh登录失败次数
#备份
cp /etc/pam.d/sshd /etc/pam.d/sshd.bak
#修改 这里测试先不限制root用户
nano /etc/pam.d/sshd
----
#%PAM-1.0
auth       required     pam_tally2.so  deny=3  unlock_time=1800
----
#使用错误密码登录三次后使用正确密码，提示SSH服务器拒绝了密码
#查看用户状态
pam_tally2 --user xm
-----
Login           Failures Latest failure     From
xm                  4    06/02/21 15:58:00  192.168.1.89
-----
#使用命令解锁用户
pam_tally2 -r -u xm
#使用正确密码登录成功

```

### 问题

经过多次尝试发现/etc/pam.d/login这个文件限制的是本地tty登录。图形界面登录不受限制。

图形界面的登录错误次数目前没有找到限制方式。只要输入正确密码就可以登录成功

## 数据库密码

### 配置口令复杂度要求

```shell
#编辑配置文件my.cnf
vim /etc/my.cnf
#在[mysqld]下写入相关配置
[mysqld]
plugin-load=validate_password.so
validate-password=FORCE_PLUS_PERMANENT
validate_password_policy=2

#重启mysql
systemctl restart mysqld

#检查是否开启
mysql
mysql> show global variables like 'validate_password%';
-----
+--------------------------------------+--------+
| Variable_name                        | Value  |
+--------------------------------------+--------+
| validate_password_check_user_name    | OFF    |
| validate_password_dictionary_file    |        |
| validate_password_length             | 8      |
| validate_password_mixed_case_count   | 1      |
| validate_password_number_count       | 1      |
| validate_password_policy             | STRONG |
| validate_password_special_char_count | 1      |
+--------------------------------------+--------+
7 rows in set (0.01 sec)
-----


validate_password_dictionary_file：密码策略文件，策略为STRONG才需要
validate_password_length：密码最少长度 
validate_password_mixed_case_count：大小写字符长度，至少1个
validate_password_number_count ：数字至少1个  
validate_password_special_char_count：特殊字符至少1个
```

### 问题

数据库密码定期更换，是否只是需要制度管理。

mysql中没有强制定期更换的策略

## CentOS 7 安装Docker

配置yum源

```shell
cd /etc/yum.repos.d/
#aliyun
wget https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
#官方源
wget https://download.docker.com/linux/centos/docker-ce.repo

yum clean all
yum makecache
```

安装

```shell
# 关闭防火墙
systemctl stop firewalld
systemctl disable firewalld

yum install -y docker-ce

systemctl enable docker
systemctl start dokcer

# root 安装后让其他用户有docker权限
# 方式一修改docker.sock的权限
cd /var/run
sudo chmod o+rw docker.sock
# 方式二将用户加入docker用户组
sudo gpasswd -a $USER docker
sudo newgrp

```

### 安装docker-compose v1

```shell
wget https://github.com/docker/compose/releases/download/1.29.2/docker-compose-Linux-x86_64
mv docker-compose-Linux-x86_64 /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

### 安装docker-compose v2

```shell
wget https://github.com/docker/compose/releases/download/v2.12.0/docker-compose-linux-x86_64

mkdir -p $HOME/.docker/cli-plugins

curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-`uname -s`-`uname -m` > $HOME/.docker/cli-plugins/docker-compose

chmod +x $HOME/.docker/cli-plugins/docker-compose
```



### docker中使用gpu

需要安装NVIDIA Container Toolkit

如果不安装的话使用`--gpus`参数会报错

```
docker: Error response from daemon: could not select device driver "" with capabilities: [[gpu]].
```

官方安装文档

```shell
https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html
```



## Debian 11 root账户登录

```shell
nano /etc/ssh/sshd_config
----
#添加配置项
#允许root用户登录
PermitRootLogin yes
#允许用密码登录
PasswordAuthentication yes
```

```shell
nano /etc/pam.d/gdm-password
----
#注释配置
#auth   required        pam_succeed_if.so user != root quiet_success
```

重启ssh

```shell
systemctl restart ssh
```

## Debian 11 安装nfs

```shell
$ apt install -y nfs-common nfs-kernel-server
# 创建共享目录
$ mkdir /data/share
$ nano /etc/export
-----
/data/share     192.168.32.0/24(rw,sync,no_root_squash)
-----
$ systemctl restart nfs-server
$ showmount -e 192.168.32.11
----
Export list for 192.168.32.11:
/data/share 192.168.32.0/24
----
```

## KVM

### 准备

```shell
# 关闭防火墙
systemctl stop firewalld
systemctl disable firewalld
# 关闭selinux
sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config

# 安装依赖
yum install qemu-kvm libvirt virt-install bridge-utils -y
# 配置网卡
cd /etc/sysconfig/netowrk-scripts
# 拷贝当前网卡，作为桥接网卡
cp ifcfg-ens33 ifcfg-br0
# 修改原网卡配置
nano ifcfg-ens33
----
# 注释掉下面四个配置
#IPADDR=192.168.0.50
#PREFIX=24
#GATEWAY=192.168.0.1
#DNS1=192.168.1.1
#添加桥接网卡配置
BRIDGE=br0
----
# 修改桥接网卡配置
nano ifcfg-br0
----
# 修改以下字段
TYPE=Bridge
BOOTPROTO=static
NAME=br0
DEVICE=br0
----
# 重启网卡
systemctl restart network

# 检查KVM模块是否加载  
lsmod |grep kvm  
# 启动libvritd服务
systemctl start libvirtd  
# 此时可以看到两个网卡
brctl show
```

### 安装虚拟机

```shell
virt-install --name=test01 --memory=1024,maxmemory=1024 --vcpus=1,maxvcpus=2 --os-type=linux --os-variant=rhel7 --location=/home/CentOS-7-x86_64-DVD-1810.iso --disk path=/kvm/study01.img,size=10 --bridge=br0 --graphics=none --console=pty,target_type=serial  --extra-args="console=tty0 console=ttyS0"

virt-install --virt-type=kvm --name=test1 --vcpus=4 --memory=8192 --location=/home/CentOS-7-x86_64-DVD-2009.iso --disk path=/home/kvm/test1.qcow2,size=40,format=qcow2 --network bridge=br0 --graphics none --extra-args='console=ttyS0' --force
```

**参数说明**

```
--name 指定虚拟机的名称
--memory 指定分配给虚拟机的内存资源大小
maxmemory 指定可调节的最大内存资源大小，因为KVM支持热调整虚拟机的资源
--vcpus 指定分配给虚拟机的CPU核心数量
maxvcpus 指定可调节的最大CPU核心数量
--os-type 指定虚拟机安装的操作系统类型
--os-variant 指定系统的发行版本
--location 指定ISO镜像文件所在的路径，支持使用网络资源路径，也就是说可以使用URL
--disk path 指定虚拟硬盘所存放的路径及名称，size 则是指定该硬盘的可用大小，单位是G
--bridge 指定使用哪一个桥接网卡，也就是说使用桥接的网络模式
--graphics 指定是否开启图形
--console 定义终端的属性，target_type 则是定义终端的类型
--extra-args 定义终端额外的参数
```

### 常用命令

```shell
#查看kvm虚拟机状态
virsh list --all 
#KVM虚拟机开机
virsh start <name>
#virsh关机
virsh shutdown <name>
#强制关闭电源
virsh destroy <name>
#通过配置文件启动虚拟机
virsh create /etc/libvirt/qemu/<name>.xml 
#配置开机自启动虚拟机
virsh autostart <name>
#导出KVM虚拟机配置文件
virsh dumpxml <name> > /etc/libvirt/qemu/<name>.xml
#删除kvm虚拟机 该命令只是删除wintest01的配置文件，并不删除虚拟磁盘文件。
virsh undefine <name>
#查看虚拟机存放位置
virsh domblklist <name>
#修改虚拟机配置文件
virsh edit <name>

#内存热扩容
virsh setmem --domain centos8-3 --size 2048M --live --config


#克隆虚拟机
virt-clone -o <old name> -n <new name> -f <new disk path>
virt-clone -o guest-pod01-bj -n guest-pod02-bj -f /home/data/kvm/guest-pod02-bj.qcow2

# Active console session exists for this domain
#方案1
% ps aux | grep console
% kill 
#方案2
% /etc/init.d/libvirt-bin restart
#方案3
% ps aux | grep kvm
% kill 对应的虚拟机进程


```

### 虚拟机迁移

[参考链接](https://blog.51cto.com/u_11233559/2311004)

#### 宿主机内迁移

```shell
#关闭虚拟机
#查看虚拟机存放路径
virsh domblklist <name>
Target     Source
------------------------------------------------
hda        /home/data/kvm/guest-pod04-bj.qcow2
hdb        -

#把文件迁移到指定位置
mv /home/data/kvm/guest-pod04-bj.qcow2 /data/kvm/
#编辑虚拟机配置文件，修改文件路径
virsh edit guest-pod04-bj
-----
  <devices>
    <emulator>/usr/libexec/qemu-kvm</emulator>
    <disk type='file' device='disk'>
      <driver name='qemu' type='qcow2'/>
      # 编辑到新路径
      <source file='/data/kvm/guest-pod04-bj.qcow2'/>
      <target dev='hda' bus='ide'/>
      <address type='drive' controller='0' bus='0' target='0' unit='0'/>
    </disk>
-----
#启动虚拟机
virsh start guest-pod04-bj
```

### 重启网卡后

宿主机重启网卡后需要重新挂载虚拟机网卡，首先使用`ifconfig`命令查看虚拟机网卡名称一般为vnet0,vnet1等。然后使用brctl命令查看网桥状态，并将虚拟机网卡挂载到网桥

```shell
#查看网桥状态
brctl show 

[root@bogon network-scripts]# brctl show
bridge name	bridge id		STP enabled	interfaces
br0		8000.80615f1c8db8	no		ens11f0
virbr0		8000.525400e86f50	yes		virbr0-nic

#添加虚拟网卡到网桥
[root@bogon network-scripts]# brctl addif br0 vnet0
[root@bogon network-scripts]# brctl addif br0 vnet1
[root@bogon network-scripts]# brctl addif br0 vnet2
[root@bogon network-scripts]# brctl addif br0 vnet3
[root@bogon network-scripts]# brctl addif br0 vnet4
[root@bogon network-scripts]# brctl addif br0 vnet5

[root@bogon network-scripts]# brctl show
bridge name	bridge id		STP enabled	interfaces
br0		8000.80615f1c8db8	no		ens11f0
							vnet0
							vnet1
							vnet2
							vnet3
							vnet4
							vnet5
virbr0		8000.525400e86f50	yes		virbr0-nic


```

| 参数                      | 说明                   | 示例                      |
| :------------------------ | :--------------------- | :------------------------ |
| `addbr <bridge>`          | 创建网桥               | **brctl** addbr br10      |
| `delbr <bridge>`          | 删除网桥               | **brctl** delbr br10      |
| `addif <bridge> <device>` | 将网卡接口接入网桥     | **brctl** addif br10 eth0 |
| `delif <bridge> <device>` | 删除网桥接入的网卡接口 | **brctl** delif br10 eth0 |
| `show <bridge>`           | 查询网桥信息           | **brctl** show br10       |
| `stp <bridge> {on|off}`   | 启用禁用 STP           | **brctl** stp br10 off/on |
| `showstp <bridge>`        | 查看网桥 STP 信息      | **brctl** showstp br10    |
| `setfd <bridge> <time>`   | 设置网桥延迟           | **brctl** setfd br10 10   |
| `showmacs <bridge>`       | 查看 mac 信息          | **brctl** showmacs br10   |



## 问题

### SSH连接卡主不动

[参考链接](https://serverfault.com/questions/210408/cannot-ssh-debug1-expecting-ssh2-msg-kex-dh-gex-reply)

[参考链接](https://github.com/johnnian/Blog/issues/44)

- 使用xshell连接卡在：

```shell
Host '' resolved to .
Connecting to ...
Connection established.
To escape to local shell, press Ctrl+Alt+].
```

- 使用命令行ssh连接没有反应
- ssh debug卡在

```shell
debug3: send packet: type 50
debug2: we sent a publickey packet, wait for reply
```

​		或

```shell
debug3: send packet: type 30
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
```

可能的原因是网卡或VPN MTU长度不匹配。

查看mtu：

windows：

```powershell
netsh interface ipv4 show subinterfaces
```

linux:

```shell
ifconfig
```

修改mtu：

windows：

```shell
netsh interface ipv4 set subinterface "接口名" mtu=[mtu值] store=persistent
```

linux：

```shell
# 临时修改
ifconfig [网卡名] mtu 1200
# 永久修改
vi /etc/sysconfig/network-scripts/ifcfg-[网卡名]
----
MTU=1200            #MTU设置
----

systemctl restart network
```

确定 mtu长度可以使用ping命令，如果成功则长度合适，长度不合适的话会返回`需要拆分数据包但是设置 DF。`

```shell
ping -f -l [mtu] [ip]
```



# Anolis 龙蜥 

## 问题

### 安装系统时无法识别硬盘

可能是因为内核版本问题导致无法识别raid卡的虚拟硬盘。



