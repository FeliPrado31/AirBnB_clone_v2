#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static. It must

# Update upgrade and install
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# make dirs
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# create page
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html

# link files
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# give privs
sudo chown -hR ubuntu:ubuntu /data/

# write default
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=DHITmcKUGik;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

# start service
sudo service nginx start
