import asyncio
from typing import Optional

import requests

import aiohttp

from .constants import API_URL
from .errors import GiphyPyError, GiphyPyKeyError


class Giphy:
    """
    Wrapper for the Giphy api. Keys can be optained from:
    https://developers.giphy.com
    """
    def __init__(self, api_key, loop: Optional[asyncio.BaseEventLoop] = None,
                 session: aiohttp.ClientSession = None):
        """
        :param api_key: Giphy API key, required.
        """
        if not api_key:
            raise GiphyPyKeyError

        self.api_key = api_key
        self.loop = loop or asyncio.get_event_loop()
        self.session = session or aiohttp.ClientSession(loop=self.loop)

    async def _get(self, api_endpoint, params):
        """
        Wrapper for fetching data from Giphy
        :param api_endpoint: Giphy API endpoint, usually search or translate.
        """
        params.update({'api_key': self.api_key})
        req_str = API_URL + api_endpoint
        print(req_str)
        async with self.session.get(url=req_str, params=params) as resp:
            data = await resp.json()
            print(data)
        return data

    async def search(self, q, limit=None, offset=None, rating=None, lang=None):
        """
        Main search method for Giphy's search endpoint
        :param q: search term, Required
        :param limit: search result limit, not Required
        :param offset: search result offset
        :param rating: search result age rating (Y, G, PG, PG-13, R)
        :param lang: language, default=en
        """
        params = {'q': q}
        if limit:
            params.update({'limit': limit})
        if rating:
            params.update({'rating': rating})
        if offset:
            params.update({'offset': offset})
        if lang:
            params.update({'lang': lang})

        data = await self._get('search', params=params)
        if data['meta']['status'] is not 200:
            raise GiphyPyError(str(data['meta']['msg']))
        return data

    async def translate(self):
        """
        Method for Giphy's translate endpoint
        """
        pass
