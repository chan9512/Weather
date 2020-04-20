from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime
import time


today = date.today()
now = datetime.now()

url = 'http://apis.data.go.kr/1360000/MidFcstInfoService/getMidLandFcst'

x_now=int(str(now.hour)+str(now.minute)) #현재 시간+분/ 인트형

if x_now>=600 and x_now<1800:
    today_string = today.strftime('%Y%m%d') + '0600'
    Queryparams = '?' + 'ServiceKey=' + '%2B6LwXwdSiXfBWg2A2q8IXzUCjGP13kzdct07M%2Bu6z9a%2BtwEhnndllUmg%2B9dzpW9ggINqxPfYck050bxzhUAPjw%3D%3D' \
                + '&pageNo=' + '1' \
                + '&numOfRows=' + '10'\
                + '&dataType=' + 'XML' \
                + '&regId=' + '11B00000' \
                + '&tmFc=' + today_string
    print('0600~1800')
else:
    today_string = today.strftime('%Y%m%d') + '1800'
    Queryparams = '?' + 'ServiceKey=' + '%2B6LwXwdSiXfBWg2A2q8IXzUCjGP13kzdct07M%2Bu6z9a%2BtwEhnndllUmg%2B9dzpW9ggINqxPfYck050bxzhUAPjw%3D%3D' \
                  + '&pageNo=' + '1' \
                  + '&numOfRows=' + '10' \
                  + '&dataType=' + 'XML' \
                  + '&regId=' + '11B00000' \
                  + '&tmFc=' + today_string
    print('1800~0600')

url = url + Queryparams
result = requests.get(url)

bs_obj = BeautifulSoup(result.text, "html.parser")

CommerceInfor = {}
rn_3alist = []
rn_3plist = []
rn_4alist = []
rn_4plist = []
rn_3a = bs_obj.find_all('rnst3am')
rn_3p = bs_obj.find_all('rnst3pm')
rn_4a = bs_obj.find_all('rnst4am')
rn_4p = bs_obj.find_all('rnst4pm')
for code in rn_3a:
    rn_3alist.append(code.text+'%')
for code in rn_3p:
    rn_3plist.append(code.text+'%')
for code in rn_4a:
    rn_4alist.append(code.text+'%')
for code in rn_4p:
    rn_4plist.append(code.text+'%')
CommerceInfor['3일뒤 오전 강수확률'] = rn_3alist
CommerceInfor['3일뒤 오후 강수확률'] = rn_3plist
CommerceInfor['4일뒤 오전 강수확률'] = rn_4alist
CommerceInfor['4일뒤 오후 강수확률'] = rn_4plist
df = pd.DataFrame(CommerceInfor)
df = df[['3일뒤 오전 강수확률','3일뒤 오후 강수확률','4일뒤 오전 강수확률','4일뒤 오후 강수확률']]
print(df)
print(bs_obj)





