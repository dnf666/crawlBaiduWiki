import urllib


class HtmlDownloader(object):
    def downloader(self, new_url):
        if new_url is None:
            return None
        # python3 urllib.request 代替urllib2
        response = urllib.request.urlopen(new_url)
        if response.getcode() != 200:
            return None
        return response.read()