#!/bin/bash
python3 -m venv myvenv;source myvenv/bin/activate
pip3 install -r requirements.txt
clear
sudo python3 src/OS_Bruteforcer.py
