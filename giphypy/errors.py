
class GiphyPyKeyError(Exception):
    def __init__(self):
        self.msg = 'Missing Giphy api_key, visit:https://developers.giphy.com\
        to obtain an api_key'

    def __str__(self):
        return self.msg


class GiphyPyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
