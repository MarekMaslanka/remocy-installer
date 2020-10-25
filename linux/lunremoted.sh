#!/bin/sh
USER=`id -un 1000`
XAUTHORITY=`su - $USER -c '/usr/bin/xauth info' | grep Authority | awk '{print $3}'`
export XAUTHORITY=$XAUTHORITY
su - $USER -c 'cd /opt/lunremote/ && /opt/lunremote/lunremoted'
