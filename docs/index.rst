.. GiphyPy documentation master file, created by
   sphinx-quickstart on Mon Jul 10 09:06:40 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

GiphyPy
===================================

v0.0.3 (`Github`_)

GiphyPy is a Python wrapper for the Giphy API, using asyncio.
For Python 3.6x.

Getting Started
===============
1. Clone the repository.

2. At the command line::

    python install setup.py


Usage
=====
 Interactive Example::

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

Available functions:
--------------------
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





.. toctree::
   :maxdepth: 1

   installation
   user_guide
   modules
   contribution


* :ref:`modindex`
* :ref:`search`

.. _Github: https://github.com/The-PyWaiters/GiphyPy
