# GiphyPy
 Async Python 3.6+ wrapper for Giphy API

Installation
=================================

Usage
=================================
```python
from giphypy.client import Giphy
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
```
    available functions:
        * search
        * translate
        * gif_links
        * random
        * find_by_id
        * stickers_search
        * stickers_trending
        * stickers_links
        * stickers_translate
        * stickers_random

Examples
=================================

Contribution
=================================
1. Fork or clone repository
2. Create a branch such as **feature/bug/refactor** and send a Pull request
