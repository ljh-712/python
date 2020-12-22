import requests
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
url = 'https://www.lagou.com/jobs/list_?px=default&city=%E5%85%A8%E5%9B%BD#order'
resp = requests.get(url,headers=header)

print(resp.text)
import re
infos = re.findall('<div class="el">(.*?)</div>',resp.text,re.S)
print(infos)