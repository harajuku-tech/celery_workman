# -*- coding: utf-8 -*-
from celery.task import task

@task               # tasknize
def hello(msg):
    ''' hello '''
    open("/tmp/hello.txt","a").write(msg)
