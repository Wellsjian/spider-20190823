import requests

# def get_total_page():
#     url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1566301036883&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=40003&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=gb'.format('', 1)
#     html = requests.get(url=url).json()
#     print('*' * 50)
#     total = html['Data']['Count']
#     print(total)
#
# get_total_page()

def get_cookies():
    cookies = {}
    string ="OUTFOX_SEARCH_USER_ID=-1039448775@43.254.90.134; OUTFOX_SEARCH_USER_ID_NCOO=413106244.4840502; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcsA-TscoFtl8oyd5pYw; ___rl__test__cookies=1565782252253"
    for s in string.split("; "):
        print(s)
        cookies[s.split("=")[0]] = s.split('=')[1]
    print(cookies)

get_cookies()
