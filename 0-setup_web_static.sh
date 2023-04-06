#!/usr/bin/env bash
# Bash script that sets up my web servers for the deployment of web_static.

if ! command -v nginx &> /dev/null; then
    echo "Nginx is not installed, installing now..."
    sudo apt-get -y update
    sudo apt-get -y install nginx
    echo "Nginx installed successfully"
else
    echo "Nginx is already installed"
fi

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

new_string="server_name _;\n\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tindex index.html;\n\t}\n"

sed -i "s|server_name _;|${new_string}|" /etc/nginx/sites-available/default

sudo service nginx restart
