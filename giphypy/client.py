from .constants import api_url
from .errors import GiphyPyKeyError, GiphyPyError
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

    def gif_search(self, q, limit=None, offset=None, rating=None, lang=None):
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

        data = self._get('search', params)
        if data['meta']['status'] != 200:
            raise GiphyPyError(str(data['meta']['msg']))
        return data

    def gif_translate(self):
        """
        Method for Giphy's translate endpoint
        """
        pass
