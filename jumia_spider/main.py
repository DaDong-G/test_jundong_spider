from spider_plus.core.engine import Engine
from . spiders  import  BaiduSpider


if __name__ == '__main__':
    print('kaishi')
    spider = BaiduSpider()  # 实例化爬虫对象
    engine = Engine(spider)  # 传入爬虫对象
    engine.start()  # 启动引擎