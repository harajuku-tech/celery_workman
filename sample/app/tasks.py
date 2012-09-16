# -*- coding: utf-8 -*-
from celery.task import task

@task               # tasknize
def hello(msg):
    ''' hello '''
    open("/tmp/msg.txt","a").write(msg)
