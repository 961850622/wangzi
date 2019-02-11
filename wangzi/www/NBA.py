import requests
import pymongo
from pymongo import MongoClient
import json

data = []
headers= {
            'Accept': '*/*',
           'Accept-Language': 'zh-cn',
           'x-app-theme': 'light',
           'User-Agent': 'ZhihuHybrid osee2unifiedRelease/1202 osee2unifiedReleaseVersion/4.33.0 Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79',
           'Connection': 'keep-alive',
           'Cookie': 'ff_supports_webp=0; ff_supports_animateWebP=0; ff_supports_webp=0; _xsrf=O4g6dtlkNlZFVggeT52RWUGzFsFnijxt; d_c0=AIDCEFjZeQxLBWsK1dPkVAqvGOo_YbiFq3I=|1548505997; zst_82=1.0APDhTUGd4g4LAAAASwUAADEuMItTTFwAAAAAC9di-WDtwTLN-jsAnNAwxvCk1NM=; __utma=51854390.963672028.1528802036.1531737089.1531748942.120; __utmv=51854390.010--; _zap=afb79ae8-329d-496d-b20d-8fda4c6e8f90; q_c0=2|1:0|10:1547640733|4:q_c0|80:MS4xQkkwY0JnQUFBQUFMQUFBQVlBSlZUWjJzWmx4c2FkeG5nX3psNHdfcXcxeUNURWlNR3ZldUtBPT0=|4aec74764d917128ca67140819d2afa25b3ad84bf193bd879ad033a8849ae7e3; q_c1=9f34b250719c4746a5b67ca6a23f6bba|1537923517000|1537923517000; q_c1=9f34b250719c4746a5b67ca6a23f6bba|1547224912000|1537923517000; tgw_l7_route=6f929a6524f45e8489eb5d9c1e7595ab; z_c0="2|1:0|10:1547640733|4:z_c0|80:MS4xQkkwY0JnQUFBQUFMQUFBQVlBSlZUWjJzWmx4c2FkeG5nX3psNHdfcXcxeUNURWlNR3ZldUtBPT0=|7880aa5a3f11caad06b4af7575950a24aa42269112c3c6359ddefb9025b7b5fa"'
            }
req = requests.Session()
url = 'https://api.zhihu.com/questions/263953798'
response = req.get(url,headers=headers)
rank = response.json()
print(rank)
