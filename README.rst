httpie-ntlm
===========

NTLM auth plugin for `HTTPie <https://github.com/jkbr/httpie>`_.


Installation
------------

.. code-block:: bash

    $ pip install httpie-ntlm


You should now see ``ntlm`` under ``--auth-type`` in ``$ http --help`` output.


Usage
-----

.. code-block:: bash

    $ http --auth-type=ntlm --auth='domain\\username:password' example.org


You can also use `HTTPie sessions <https://github.com/jkbr/httpie#sessions>`_:

.. code-block:: bash

    # Create session
    $ http --session=logged-in --auth-type=ntlm --auth='domain\\username:password' example.org

    # Re-use auth
    $ http --session=logged-in POST example.org hello=world

Requirements
------------

- requests-ntlm_

.. _requests-ntlm: https://github.com/requests/requests-ntlm/
