#/bin/bash

cd "$(dirname "$0")"
sudo cp phoniebox_volume.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl start phoniebox_volume
sudo systemctl status phoniebox_volume
sudo systemctl enable phoniebox_volume