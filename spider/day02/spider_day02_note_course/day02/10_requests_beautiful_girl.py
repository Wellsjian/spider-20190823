import requests

url = 'https://b-ssl.duitang.com/uploads/item/201702/28/20170228090601_jnLUR.jpeg'
headers = {'User-Agent':'Mozilla/5.0'}

res = requests.get(url=url,headers=headers)
html = res.content

filename = url[-10:]
with open(filename,'wb') as f:
  f.write(html)
















