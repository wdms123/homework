import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
def fip(url):
    request=urllib.request.Request(url)
    response=urllib.request.urlopen(request)
    html=response.read().decode('utf-8')
    result0 = BeautifulSoup(html, 'html.parser')
    result1 = result0.find_all('ul', {'class': {'newslist'}})
    result2 = result0.find_all('ul', {'class': {'txt'}})
    return result1
    return result2
result3=fip('http://news.ncu.edu.cn/')
for finally_result0 in result3:
    print(finally_result0.get_text())





