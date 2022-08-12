.. image:: https://www.pushsafer.com/de/assets/logos/logo.png
    :alt: Pushsafer.com
    :width: 100%
    :align: center

``MicroPython-pushsafer`` aims at providing comprehensive MicroPython bindings for the API
of the `Pushsafer Notification Service`_ as documented here__.

USAGE: exactly the same way as in python-pushsafer. Using pushsafer in micropython is painless.

.. _Pushsafer Notification Service: https://www.pushsafer.com/ 
.. __: https://www.pushsafer.com/en/pushapi

Forked from: https://github.com/appzer/python-pushsafer


Installation
------------



You can install it directly from GitHub:


    bash

    git clone https://github.com/appzer/python-pushsafer.git\

    cd python-pushsafer


 GitHub: https://github.com/appzer/python-pushsafer

Overview
--------


    micropython

    from pushsafer import Client

    client = Client("<privatekey>")
    resp = client.send_message("Message", "Hello", "323", "1", "4", "2", "https://www.pushsafer.com", "Open Pushsafer", "0", "2", "60", "600", "1", "", "", "")
    print(resp)


Params
------

   micropython

   client.send_message(
                       "Message",
                       "Title",
                       "Device or Device Group ID",
                       "Icon",
                       "Sound",
                       "Vibration",
                       "URL",
                       "URL Title",
                       "Time2Live",
                       "Priority",
                       "Retry",
                       "Expire",
                       "Answer",
                       "Image 1",
                       "Image 2",
                       "Image 3")
	
API
---

You can access the full API documentation here__.

.. __: https://www.pushsafer.com/en/pushapi
