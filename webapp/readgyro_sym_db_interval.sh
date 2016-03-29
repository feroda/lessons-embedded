#!/bin/bash

if [ ! $(id -u) -eq 0 ]; then
    echo "You must be root";
    exit 1;
fi

while true; do
    echo "$(date) $(date +%s) giro1 -- giro2 -- giro3000" >> /var/log/gyro.log;
    secs=$(sqlite3 sysconfig.sqlite "SELECT value FROM setup WHERE key='gyro_seconds'")
    sleep ${secs};
done
