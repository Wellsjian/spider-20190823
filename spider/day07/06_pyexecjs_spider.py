import execjs

with open('baidufanyi.js', 'r') as obj:
    data = obj.read()


js_obj = execjs.compile(data)
sign = js_obj.eval('e("hello")')
print(sign)