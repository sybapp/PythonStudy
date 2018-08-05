import requests
import re


url = 'https://book.douban.com/'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

content = requests.get(url, headers=header).text
print(content)
pattern = re.compile('<a.*?href="(.*?)".*?title="(.*?)".*?author">(.*?)</div>.*?year">(.*?)</span>.*?publisher">(.*?)</span>', re.S)
results = re.findall(pattern, content)
print(results)

# for result in results:
#     url, title, author, year, publisher = result
#     print(url, title, author, year, publisher, strip())
