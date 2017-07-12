GiphyPy
=======

Async Python 3.6+ wrapper for Giphy API

|Build Status|

Installation
============

::

    1. Clone the repository
    2. `pip install -r requirements.txt`
    3. `python setup.py install`

Usage
=====

.. code:: python

    from giphypy.client import Giphy
    import asyncio

    loop = asyncio.get_event_loop()

    # Create an instance of giphy class.
    # If you want to get stickers information
    # just change stickers argument of class
    # for example stickers=True
    giphy = Giphy(token, loop=loop)

    async def main():
        # data will return an dict object with data
        data = await giphy.search('apple')
        print(data)

    loop.run_until_complete(main())

::

    available functions:
        * search
        * translate
        * gif_links
        * random
        * find_by_id
        * trending
        * stickers_search
        * stickers_trending
        * stickers_links
        * stickers_translate
        * stickers_random

Contribution
============

1. Fork or clone repository
2. Create a branch such as **feature/bug/refactor** and send a Pull request

.. |Build Status| image:: https://travis-ci.org/The-PyWaiters/GiphyPy.svg?branch=master
   :target: https://travis-ci.org/The-PyWaiters/GiphyPy
