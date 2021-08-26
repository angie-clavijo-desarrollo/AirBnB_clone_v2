#!/usr/bin/env bash
# configurate the servers
sudo apt-get update
sudo apt-get install nginx -y
sudo ufw enable
sudo ufw app list
sudo ufw status
sudo systemctl status nginx
if not exist "/data/"{
    mkdir "/data"
    if not exist "/data/web_static/"{
        mkdir "/data/web_static/"
        if not exist "/data/web_static/releases/"{
            mkdir "/data/web_static/releases/"
            }
        }
        elif not exist "/data/web_static/shared/"{
            mkdir "/data/web_static/shared/"
        }
        elif not exist "/data/web_static/releases/test/"{
            mkdir "/data/web_static/releases/test/"
            touch index.html | echo "this test for nginx"
        }
}
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/  /data/web_static/current
chown ubuntu:ubuntu -R /data/
conf="\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
if [ "$(grep -c "location /hbnb_static {" /etc/nginx/sites-available/default)" -eq 0 ]; then
    sed -i "45i $conf" /etc/nginx/sites-available/default
fi
service nginx restart
