import requests
#import json

response = requests.get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
text = response.text
file_1 = open('write_method.txt', 'w', encoding='utf-8')
file_1.write(text)
file_1.close()
file_1 = open('write_method.txt', 'r', encoding='utf-8')
new_list = []
line = file_1.readline()
while  line:
  remote_addr = line.split(' ')[0]
  l = line.split('"')[1]
  request_type = l.split(' ')[0]
  l1 = l.split(' ')[1]
  requested_resource = l1.split(' ')[0]
  thistuple = (remote_addr, request_type, requested_resource)
  new_list.append(thistuple)
  del thistuple
  line = file_1.readline()
file_1.close()
print(new_list)