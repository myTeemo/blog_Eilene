# 光明携带者 | 雨后扬光 博客
### 博客地址
>[光明携带者](http://182.254.129.33)  

### 说明

> 一直想自己给自己搭建一个博客，学习Django之后,这种心情愈加更涨，恰逢也有相似的教程，就试着先搭建了起来，目前有了一个雏形，在后面的时间，我将继续完善这个博客网站。

### 运行环境

1. python 2.7
2. Ubuntu 14.04LTS X86_64 (腾讯云主机)
3. Nginx
4. uWSGI (2.0.15)
5. MySQL

### 使用Python开发包
1. virtualenv & virtualenvwrapper
2. Django (1.9.8)
3. django-crispy-forms (1.6.1)
4. django-formtools (2.0)
5. httplib2 (0.9.2)
6. Markdown (2.6.8)
7. MySQL-python (1.2.5)
8. olefile (0.44)
9. Pillow (4.1.1)
10. Pygments (2.2.0)
11. pytz (2017.2)

### Nginx配置

> $ sudo apt-get install update  
> $ sudo apt-get install upgrate  
> $ sudo apt-get install nginx  

创建 nginx 代理文件
> $ sudo vim /etc/nginx/conf.d/uc_nginx.conf  

```nginx
server {

# the port your site will be served on
    listen 80;
    
# the domain name it will serve for
# substitute your machine's IP address or FQDN
    server_name 服务器地址 ;     charset utf-8;

# max upload size
    client_max_body_size 75M;   # adjust to taste
# log files
    access_log /var/log/nginx/eilene.cn-access.log;
    error_log /var/log/nginx/eilene.cn-error.log;     

# Django media
    location /media  {
        alias 指向django的media目录;  
    }
# Django static
    location /static {
        alias 指向django的static目录;
    }
# Finally, send all non-media requests to the Django server.
    location / {
        uwsgi_pass 127.0.0.1:8000;
# the uwsgi_params file you installed
        include uwsgi_params; 
    }
}
```

### Uwsgi 配置
进入虚拟环境，安装uwsgi
> pip install uwsgi

安装后，可进入项目的根目录测试uwsgi
> uwsgi --http :8000 --module Eilene.wsgi

使用基于配置文件配置uwsgi，使用配置文件启动uwsgi文件，可以免去暴露端口对系统造成的潜在的危险

```uwsgi.ini
# mysite_uwsig.ini file
[uwsgi]

# project dir
chdir = 项目地址
module = 项目.wsgi

master = true
# process，启动进程数量
processes = 20 

# 基于sock的方式启动，这样可以代替http，实现更为安全的连接
socket = 127.0.0.1:8000

vacuum = true

# virtualenv dir
virtualenv = 虚拟环境的目录

```
