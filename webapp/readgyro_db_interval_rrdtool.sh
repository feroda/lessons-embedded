#!/bin/bash

RRDNAME=gyro.rrd

while true; do
    points=$(/usr/local/MPU6050-Pi-Demo/demo_raw | grep ^a/g -m1 | xargs | cut -d' ' -f2- | sed 's/ /:/g')
    echo "Getting points [$points]"
    echo "$(date) $(date +%s) points [$points]" >> /var/log/giroscopio.log
    rrdtool update $RRDNAME N:$points
    secs=$(sqlite3 sysconfig.sqlite "SELECT value FROM setup WHERE key='gyro_seconds'")
    if [ ! -z "$secs" ]; then
        sleep $(($secs / 10));
    fi
done
