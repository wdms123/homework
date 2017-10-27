#总是类型错误 弄了好久也没弄出来 下面是思路

import urllib.request
from bs4 import BeautifulSoup
import re


name = input('请输入你想要查询的书籍：')#查询的范式为get方式 所以用个格式化字符串就可以实现搜索功能
def ms(url):
    resquest = urllib.request.Request(url)
    response = urllib.request.urlopen(resquest)
    html0 = response.read().decode('utf-8')
    html1 = BeautifulSoup(html0,'html.parser')
    reg=r'<h3><span>中文图书</span><a href="(.*?)">(.*?)</a> '#正则匹配
    result = re.findall(reg,html1)
    for i in result:
        print(i)
 #调用函数
ms('http://opac.ncu.edu.cn/opac/openlink.php?strSearchType=title&match_flag=forward&historyCount=1&strText=%s&doctype=ALL&with_ebook=on&displaypg=20&showmode=list&sort=CATA_DATE&orderby=desc&dept=ALL')%name