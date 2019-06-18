from baike_spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    pass

    def __init__(self):
        # 初始化url的管理器
        self.urls = url_manager.UrlManager()
        # 初始化html下载器
        self.downloader = html_downloader.HtmlDownloader()
        # 初始化html的解析器
        self.parser = html_parser.HtmlParser()
        # 初始化html的输出器
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        # 添加单个url
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                # 从url管理器拿出url
                new_url = self.urls.get_new_url()
                # 根据url下载页面正文
                html_con = self.downloader.downloader(new_url)
                # 解析下载下来的正文，得到数据和相关的url
                new_urls, new_data = self.parser.parse(new_url, html_con)
                print('craw %d : %s' % (count, new_url))
                # 将相关的url加入url管理器
                self.urls.add_new_urls(new_urls)
                # 将数据收集起来
                self.outputer.collect_data(new_data)
                if count == 1000:
                    break

                count = count + 1
            except:
                print('craw fail')
        # 将数据展示
        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
