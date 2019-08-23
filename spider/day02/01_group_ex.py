import re
from urllib import request
from urllib import parse
import random
import time

html = '''
<div class="animal">
    <p class="name">
        <a title="Tiger"></a>
    </p>

    <p class="content">
        Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
        <a title="Rabbit"></a>
    </p>

    <p class="content">
        Small white rabbit white and white
    </p>
</div>'''

pattern = re.compile(r"""<div class="animal">.*?<a title="(.*?)".*?content">(.*?)</p>""", re.S)
# pattern = re.compile(r'<div class="animal">.*?<a title="(.*?)".*?content">(.*?)</p>', re.S)
data_list = pattern.findall(html)
if data_list:
    for data in data_list:
        print("动物名称：",data[0].strip())
        print("动物描述：",data[1].strip())
