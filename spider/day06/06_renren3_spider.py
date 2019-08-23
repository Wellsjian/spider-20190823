s = 'a=1;b=2;c=3'
s = s.replace("=",":").replace(";",",")
print(s.split(','))
