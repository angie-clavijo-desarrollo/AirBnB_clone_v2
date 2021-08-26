#!/usr/bin/env bash
# configurate the servers
sudo apt-get update
sudo apt-get install nginx -y
mkdir -p /data/web_static/shared /data/web_static/releases/test
echo "this test for nginx" | sudo tee /data/web_static/releases/test/index.html
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/  /data/web_static/current
chown ubuntu:ubuntu -R /data/
sed -i "41i \\\nlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n}\n" /etc/nginx/sites-available/default
service nginx restart
