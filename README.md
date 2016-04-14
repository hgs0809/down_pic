# down_pic

需要很多东西
用于处理图像的模块pillow    pip install pillow
配置settings.py
启用pipe管道和图片下载管道,配置存储图片目录
ITEM_PIPELINES = {
    'down_pic.pipelines.DownPicPipeline':400,
    'scrapy.pipelines.images.ImagesPipeline': 300,
}
IMAGES_STORE = '/root/'
还有一些事情没弄明白，存储到item里面的什么  列表 or  字典 ？
pipeitem里面是怎么读取item的
