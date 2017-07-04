from .constants import api_url
from .errors import GiphyPyKeyError, GiphyPyError
import asyncio
import requests


class giphy_api:
    """
    Wrapper for the Giphy api. Keys can be optained from:
    https://developers.giphy.com
    """
    def __init__(self, api_key):
        """
        :param api_key: Giphy API key, required.
        """
        if not api_key:
            raise GiphyPyKeyError
        self.api_key = api_key

    async def _get(self, api_endpoint: str, **args):
        """
        Wrapper for fetching data from Giphy
        :param api_endpoint: Giphy API endpoint, usually search or translate.
        """
        args['api_key'] = self.api_key
        req_str = api_url + '/' + api_endpoint
        data = await requests.get(req_str, params=args)
        return data
# Working on
    def gif_search(self):
        """
        Main search method for Giphy's search endpoint
        """
        pass

    def gif_translate(self):
        """
        Method for Giphy's translate endpoint
        """
        pass
