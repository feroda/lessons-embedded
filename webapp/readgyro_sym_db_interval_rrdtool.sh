#!/bin/bash

RRDNAME=gyro.rrd

while true; do
    rrdtool update $RRDNAME N:1300:1800:1500:1050:2220:1285 
    secs=$(sqlite3 sysconfig.sqlite "SELECT value FROM setup WHERE key='gyro_seconds'")
    sleep ${secs};
done
