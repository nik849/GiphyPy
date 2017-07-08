import asyncio
import logging
from typing import Optional

import aiohttp

from .constants import API_URL
from .errors import GiphyPyError, GiphyPyKeyError

logger = logging.getLogger(__name__)


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
        self.params = {
            'api_key': self.api_key,
        }

    async def _get(self, api_endpoint: str, **kwargs):
        """
        Wrapper for fetching data from Giphy
        :param api_endpoint: Giphy API endpoint, usually search or translate.
        """
        req_str = API_URL + api_endpoint
        async with self.session.get(url=req_str, params=self.params) as resp:
            data = await resp.json()
        return data

    async def search(self, query: str, **kwargs):
        """
        Main search method for Giphy's search endpoint
        :param query: search term, Required
        :param limit: search result limit, not Required
        :param offset: search result offset
        :param rating: search result age rating (Y, G, PG, PG-13, R)
        :param lang: language, default=en
        """

        if kwargs:
            self.params.update(**kwargs)

        self.params['q'] = query
        data = await self._get('search', params=self.params)
        if data['meta']['status'] is not 200:
            raise GiphyPyError(str(data['meta']['msg']))

        return data

    async def translate(self, s: str):
        """
        :param s: Search term, Required
        :return: dict object
        """
        self.params.pop('q')
        self.params['s'] = s

        data = await self._get('translate', params=self.params)
        logger.debug(f'Returned: {data["meta"]["status"]}')

        if data['meta']['status'] is not 200:
            raise GiphyPyError(str(data['meta']['msg']))
        return data

    async def gif_links(self, query: str, **kwargs):
        """
        :param query: Search by query.
        :param kwargs: limit/offset/rating/lang
        :return: an array with gif links
        """
        data = await self.search(query, **kwargs)
        links = []
        for gif in data['data']:
            links.append(gif['url'])
        return links

    async def random(self, **kwargs):
        """
        :param kwargs: tag/rating/fmt
        :return: an dict object with data
        """
        if kwargs:
            self.params.update(**kwargs)

        data = await self._get('random', params=self.params)
        return data

    async def find_by_id(self, gif_id: str):
        """
        :param idx: an gif ID
        :return: dict object with data
        """
        data = await self._get(f'{gif_id}', params=self.params)
        return data
