
User Guide
=================================
 * Example::

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
