import requests

def get_total_page():
    url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1566301036883&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=40003&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=gb'.format('', 1)
    html = requests.get(url=url).json()
    print('*' * 50)
    total = html['Data']['Count']
    print(total)

get_total_page()