from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime
import time


url = 'http://apis.data.go.kr/1360000/TyphoonInfoService/getTyphoonInfo'




Queryparams = '?' + 'serviceKey=' + '%2B6LwXwdSiXfBWg2A2q8IXzUCjGP13kzdct07M%2Bu6z9a%2BtwEhnndllUmg%2B9dzpW9ggINqxPfYck050bxzhUAPjw%3D%3D' \
                + '&pageNo=' + '1' \
                + '&numOfRows=' + '10'\
                + '&dataType=' + 'XML' \
                + '&fromTmFc=' + '20200420' \
                + '&toTmFc=' + '20200420'




url = url + Queryparams
result = requests.get(url)
bs_obj = BeautifulSoup(result.text, "html.parser")

rstlist = []
resultmsg = bs_obj.find_all('resultmsg')
for code in resultmsg:
    rstlist.append(code.text)

print(bs_obj)

if rstlist[0]=='NO_DATA':
    print("현재 태풍 X ")
else:
    print(bs_obj)



