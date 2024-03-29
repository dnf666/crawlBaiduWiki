# 维护待爬取的列表和爬取过的列表
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, root_url):
        if root_url is None:
            return
        # 判断这个url是否需要爬取，在带爬取行列，然后又不在爬取过行列内
        if root_url not in self.new_urls and root_url not in self.old_urls:
            self.new_urls.add(root_url)

    def add_new_urls(self, new_urls):
        if new_urls is None or len(new_urls) == 0:
            return
        for url in new_urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
