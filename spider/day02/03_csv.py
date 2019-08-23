import csv

#写一行 writerow
with open('text.csv', 'w', encoding='utf-8', newline="") as obj:
    writer = csv.writer(obj)
    writer.writerow(['jian', 80])
    writer.writerow(['yuan', 90])


#写多行 writerows

with open('text.csv', 'a', encoding='utf-8', newline="") as obj:
    writer = csv.writer(obj)
    writer.writerows([('风', 80), ('梦', 90)])






