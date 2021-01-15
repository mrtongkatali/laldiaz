#!/bin/bash
sudo service nginx restart
sudo systemctl daemon-reload
sudo systemctl restart laldiaz.service
