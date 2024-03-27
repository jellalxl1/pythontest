import requests
from bs4 import BeautifulSoup

# 定义爬取网页的URL
url = 'https://www.baidu.com'

# 发送HTTP GET请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 在这里编写你的爬虫逻辑
    # 使用BeautifulSoup选择器来提取所需的数据
    # 例如，提取所有<a>标签的文本内容和链接
    for link in soup.find_all('a'):
        text = link.text
        href = link.get('href')
        print(f'Text: {text}, Href: {href}')
else:
    print('请求失败')