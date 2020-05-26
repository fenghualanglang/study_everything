

import requests

url = 'https://edge.ivideo.sina.com.cn/177439740.mp4?KID=sina,viask&Expires=1590163200&ssig=a3ZOZKkH%2B%2F&reqid='

tt = requests.get(url)
with open('che.mp4', 'ab') as f:
    f.write(tt.content)