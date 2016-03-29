#!/bin/bash

if [ ! $(id -u) -eq 0 ]; then
    echo "You must be root";
    exit 1;
fi

while true; do
    echo "$(date) $(date +%s) giro1 -- giro2 -- giro3000" > /var/log/gyro.log;
    sleep 1;
done
