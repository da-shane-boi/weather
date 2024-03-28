#!/bin/bash

sudo apt install python3-venv
python3 -m venv ~/.config/weather/env
source ~/.config/weather/env/bin/activate
pip install -r requirements.txt
pyinstaller main.py -F -n weather -y
sudo cp dist/weather /usr/bin/
cp uninstall.sh ~/.config/weather/