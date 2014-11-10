.. image:: http://pledgie.com/campaigns/14583.png?skin_name=chrome
    :alt: Click here to lend your support to: reddit-homebrewing and make a donation at www.pledgie.com!
    :target: http://www.pledgie.com/campaigns/14583


reddit Homebrewing app.  Handles the registration and contest results
from the annual homebrewing contest.  

Installation
------------

1. Install libmemcached.

.. code:: bash

   # OS X
   $ brew install libmemcached

2. Create a virtual environment and start it up.

.. code:: bash

   $ virtualenv .
   New python executable in ./bin/python
   Installing setuptools, pip...done.
   $ . bin/activate

3. Install dependencies!

.. code:: bash

   (reddit-homebrewing) $ pip install -r requirements.txt
