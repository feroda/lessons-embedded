#!/bin/bash

rrdtool create gyro.rrd --step 1s DS:x:GAUGE:120:U:U DS:y:GAUGE:120:U:U DS:z:GAUGE:120:U:U DS:rx:GAUGE:120:U:U DS:ry:GAUGE:120:U:U DS:rz:GAUGE:120:U:U RRA:AVERAGE:0.5:1:1200
