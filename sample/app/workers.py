import os
import sys
#
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

APP_DIR=os.path.dirname(__file__)
LOG_FILE="/tmp/hello.log"  #: celery worker logfile 
PID_FILE="/tmp/hello.pid"  #: celery worker PID file
PID_CAM="/tmp/hello.cam.pid"
NODE="celery"           #: celery = default node
LOG_LEVEL="DEBUG"       #: celery log level

START=[ "celery","worker",
        "--loglevel=%s" % LOG_LEVEL,
        "--pidfile=%s"  %  PID_FILE, 
        "--logfile=%s"  %  LOG_FILE ,
        "-E",            # event option for celerycam
        "--beat" , 
        "--scheduler=djcelery.schedulers.DatabaseScheduler",
      ]    

STOP= [ "celery","multi",
        "stop",NODE,
        "--pidfile=%s" % PID_FILE, 
      ]

CAM=  [ "celerycam",
        "--pidfile=%s" % PID_CAM, 
      ]

CAMSTOP=[   "celery","multi",
            "stop",NODE,
            "--pidfile=%s" % PID_CAM, 
      ]


def configure(*args):
    ''' return django-celery parameter for specified args

        - args[0] : celery_workman.py
        - args[1] : path this django project application 
        - args[2] : command
    '''
    try:
        return  globals()[ args[2].upper() ] 
    except Exception,e:
        print e
        return []
