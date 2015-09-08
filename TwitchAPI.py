import urllib
import json

import pdb


class TwitchAPI:

    def get_content(self, url):
        response = urllib.urlopen(url)
        content = json.load(response)
        return content

    def get_followed_channels(self, channel):
        url = "https://api.twitch.tv/kraken/users/{0}/follows/channels?limit=100".format(
            unicode(channel, 'utf-8'))
        result = []
        content = self.get_content(url)
        while(len(content['follows']) > 0):
            result.extend(content['follows'])
            content = self.get_content(content['_links']['next'])
        return result

    def get_online_followed_channels(self, channel):
        followed = self.get_followed_channels(channel)
        result = []
        for f in followed:
            name = f['channel']['name']
            url = "https://api.twitch.tv/kraken/streams?channel={0}".format(
                name)
            content = self.get_content(url)
            if len(content['streams']) != 0:
                result.append(content['streams'])
        return result

    def get_online_followed_channels_oauth(self, token):
        url = "https://api.twitch.tv/kraken/streams/followed?oauth_token={0}".format(
            str(token))
        result = self.get_content(url)
        return result['streams']
