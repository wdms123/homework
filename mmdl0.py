import requests
import json


url = 'https://os.ncuos.com/api/user/token'
headers = {'Cookie':'_ga=GA1.2.1493961910.1509086245; _gid=GA1.2.1310392178.1509086245; _gat=1',
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
           'Referer':'https://os.ncuos.com/loginBox/login',
           'Content-type':'application/json'}
payload = {'username': '8002117345', 'password': '022110'}
response = requests.post(url, data=json.dumps(payload), headers=headers)
html = response.text
finally_result = json.loads(html)
print(finally_result)