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