#!/bin/sh -e

# Start or stop Celery Worker
#
# Hideki Nara <gmail@hdknr.com>
# based on Postfix's init.d script

### BEGIN INIT INFO
# Provides:          Celery Worker Manager
# Required-Start:    postfix
# Required-Stop:     
# Should-Start:      
# Should-Stop:       
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: start and stop the Celery Worker 
# Description:       Celery Worker Manager in a specific virtualenv
### END INIT INFO

### Configure your environment 
#
DAEMON=/home/hdknr/ve/tact/bin/celery_workman.py 
USER=hdknr
NAME=paloma
#
# DJANGO_PROJECTSYMBOL : add extrat DJANGO_yourname=path_to_django_project
DJANGO_SAMPLE=/home/hdknr/ve/tact/src/celery-workman/sample/app
#DJANOG_HOGE=/....

# list project symbol which will be run  on start up
ONSTART="SAMPLE"
####

RUN=${1:-start}
PROJECTS=${2:-$ONSTART}
#
test -x $DAEMON || exit 0
id $USER > /dev/null 2>&1 || exit 0

case $RUN in
    'install' ) insserv $NAME;;
    'uninstall') insserv -r $NAME;;
    ''|'start'|'stop' | 'cam' | 'camstop') 
        for PRJ in $PROJECTS; do
            PRJ=DJANGO_$PRJ
            PRJ=`eval echo \\$$PRJ` 
            if [ "$PRJ" != "" ] ; then 
                echo "sudo -u $USER $DAEMON $PRJ $RUN";
               (sudo -u $USER $DAEMON $PRJ $RUN)& 
            fi
        done
esac

