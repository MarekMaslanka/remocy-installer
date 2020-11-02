#!/bin/sh
echo $$ > /run/lunremoted.pid
USER=`/opt/lunremote/users`
su - $USER -c 'cd /opt/lunremote/ && /opt/lunremote/lunremoted'