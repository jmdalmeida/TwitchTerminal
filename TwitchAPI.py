import urllib
import json

import pdb


class TwitchAPI:

    BASE = "https://api.twitch.tv/kraken/"

    def get_content(self, url):
        response = urllib.urlopen(url)
        content = json.load(response)
        return content

    def get_followed_channels(self, channel):
        url = Urls.FOLLOWED_CHANNELS.format(unicode(channel, 'utf-8'))
        result = []
        content = self.get_content(url)
        while(len(content['follows']) > 0):
            result.extend(content['follows'])
            content = self.get_content(content['_links']['next'])
        return result

    def get_live_followed_channels(self, channel):
        followed = self.get_followed_channels(channel)
        followed_live = self.get_followed_names(followed)
        url = Urls.FOLLOWED_ONLINE_CHANNELS.format(",".join(followed_live))
        result = []
        result = self.get_content(url)
        return result['streams']

    def get_followed_names(self, channels):
        result = []
        for c in channels:
            result.append(c['channel']['name'])
        return result

class Urls:
    '''
    Should not be instantiated, just used to categorize
    string-constants
    '''
    BASE = "https://api.twitch.tv/kraken/"
    FOLLOWED_CHANNELS = BASE + "users/{0}/follows/channels?limit=100"
    FOLLOWED_ONLINE_CHANNELS = BASE + "streams?channel={0}"
