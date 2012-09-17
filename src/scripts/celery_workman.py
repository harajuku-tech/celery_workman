''' 
Celery Worker Manger:

    - execute absolute path to celery_workman.py
    - give your django application path to the first argument
::

    $ /home/foo/ve/bar/bin/celery_workman.py /home/foo/ve/bar/src/yourproject/app start

'''
if __name__ == '__main__':
    import sys,os
    if len(sys.argv) < 2:
        sys.stderr.write('you need path of your django application')
        sys.exit(1) 

    sys.argv[1] = os.path.abspath( sys.argv[1]  )
    sys.path.append(os.path.dirname(sys.argv[1]))    #: Important
    sys.path.append(sys.argv[1])    #: Important

    from django.core.management import execute_manager
    import imp
    try:
        imp.find_module('settings') # Assumed to be in the same directory.
    except ImportError:
        import sys
        sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
        sys.exit(1)
    
    import settings
    import workers
    
    if __name__ == "__main__":
        sys.argv = [ os.path.abspath(sys.argv[0])] + workers.configure(*sys.argv) 
        execute_manager(settings)
