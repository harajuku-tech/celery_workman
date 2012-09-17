celery_workman
========================================================================

Bourne shell script at /etc/init.d  to start or stop Celery worker accomodated in a Python virtualenv.

Install
--------

- install celery_workman to your virualenv

.. code-block:: bash


    $ pip install -e git+https://github.com/harajuku-tech/celery_workman.git#egg=celery_workman

Python daemonizing script is installed on $VIRTUALENV/bin


.. code-block:: bash

    (tact)hdknr@wzy:~$ which celery_workman.py 

    /home/hdknr/ve/tact/bin/celery_workman.py

copy bourne shell scirpt
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- or symlink

.. code-block:: bash

    $ sudo cp sample/etc/init.d/celery-workman.sh to /etc/init.d/celery-workman
    $ sudo chomod +x  /etc/init.d/celery-workman

Enable start on bool
^^^^^^^^^^^^^^^^^^^^^^

- with Debian insserv

.. code-block:: bash

    $  sudo /etc/init.d/celery_workman install

- to disable 

.. code-block:: bash

    $  sudo /etc/init.d/celery_workman uninstall


Configure /etc/init.d/celery-workman
----------------------------------------------------

- Add your Django projects in a virtualenv which is the same one as the daemonizing Python script in on.

.. code-block:: bash

    DJANGO_SAMPLE=/home/hdknr/ve/tact/src/celery-workman/sample/app
    DJANGO_FOO=/home/hdknr/ve/tact/src/hoge/app
    DJANGO_BAR=/home/hdknr/ve/tact/src/hoge/app

- Specify auto starting on OS boot:  

.. code-block:: bash


    ONSTART="SAMPLE FOO"


Start and Stop manually
--------------------------------

Syntax::

    $ sudo /etc/init.d/celery_workman  {{command}} {{project_symbol}}

- Starting

.. code-block:: bash

    $ sudo /etc/init.d/celery_workman start SAMPLE 

- Stopping

.. code-block:: bash

    $ sudo /etc/init.d/celery_workman stop SAMPLE 

- Command are configured in workers.py of your each django project.

Workers.py
--------------------------------

- configure() return list of celery management command
- check  `sample/app/workers.py <https://github.com/harajuku-tech/celery_workman/blob/master/sample/app/workers.py>`_

