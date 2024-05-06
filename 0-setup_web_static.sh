#!/usr/bin/env bash
#set task 0 good
sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
sudo bash -c 'echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html'

sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
config="/etc/nginx/sites-available/default"
new_location="\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"

sudo sed -i "/listen 80 default_server;$/a$new_location" "$config"
sudo service nginx restart
