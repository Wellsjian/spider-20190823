import re

html = '''<div class="animal">
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

pattern = re.compile('<div class="animal">.*?title="(.*?)".*?class="content">(.*?)</p>',re.S)

# 问题1
r_list = pattern.findall(html)
print(r_list)

# 问题2
for r in r_list:
    print('*' * 50)
    print('动物名称:',r[0].strip())
    print('动物描述:',r[1].strip())

print('*' * 50)