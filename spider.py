import requests
from lxml import etree
import time

def parse_list_page(url):
    html = requests.get(url)
    sel = etree.HTML(html.text)
    detail_links = sel.xpath('.//div[@id="page_list"]/ul/li/a/@href')
    for detail_link in detail_links:
        parse_one_page(detail_link)

def parse_one_page(url):
    html = requests.get(url)
    sel = etree.HTML(html.text)
    title = sel.xpath('.//div[@class="con_l"]/div/h4/em/text()')[0]
    address = sel.xpath('.//span[@class="pr5"]/text()')[0].strip()
    price = sel.xpath('.//div[@class="day_l"]/span/text()')[0]
    lord = sel.xpath('.//a[@class="lorder_name"]/text()')[0]
    sex = sel.xpath('.//span[contains(@class,"member")]/@class')[0].split('_')[1]
    if sex == 'boy':
        sex = '男'
    else:
        sex = '女'
    data = {'标题':title,
            '地址':address,
            '价格':price,
            '房东姓名':lord,
           '房东性别':sex}
    #print('"标题":{},"地址":{},"价格":{},"房主姓名":{},"房主性别":{}'.format(title,address,price,lord,sex))
    print(data)

base_url = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'
urls = [base_url.format(i) for i in range(1,6)]
for url in urls:
    parse_list_page(url)
    time.sleep(5)

