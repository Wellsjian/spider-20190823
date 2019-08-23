import csv

# writerow([])
with open('test.csv','w',newline='') as f:
  writer = csv.writer(f)
  writer.writerow(['步惊云', '30'])
  writer.writerow(['超哥哥', '25'])

# writerows([(),(),(),()])
with open('test.csv','a',newline='') as f:
  writer = csv.writer(f)
  writer.writerows([('聂风','30'),('梦','28')])















