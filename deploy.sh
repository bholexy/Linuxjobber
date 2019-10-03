#!/bin/sh

ssh kome@live.linuxjobber.com <<EOF
  cd /var/www/html/Linuxjobber
  git pull origin master
  source /myenv/bin/activate
  sudo pip install -r requirements.txt
  python3 manage.py migrate
  sudo apachectl graceful
  exit
EOF