from operator import eq
from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime
import time
import xml.etree.ElementTree as etree
import xmltodict

today = date.today()
now = datetime.now()

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst'
z=now.minute
if(now.minute<10):
    z = str(0)+str(z)
print('현재(분): '+ str(z))
x_now=int(str(now.hour)+str(z)) #현재 시간+분/ 인트형
print('현재(시간 + 분): '+ str(x_now))
y=today.strftime('%Y%m%d')
print('현재(년도 + 날짜): '+ y)

if 2311<=x_now or x_now<=210:
    Queryparams = '?' + 'serviceKey=' + '%2B6LwXwdSiXfBWg2A2q8IXzUCjGP13kzdct07M%2Bu6z9a%2BtwEhnndllUmg%2B9dzpW9ggINqxPfYck050bxzhUAPjw%3D%3D' \
                    + '&pageNo=' + '1' \
                    + '&numOfRows=' + '70'\
                    + '&dataType=' + 'XML' \
                    + '&base_date=' + y \
                    + '&base_time=' + '2300' \
                    + '&nx=' + '56' \
                    + '&ny=' + '124'
    print('2300')
elif 211<=x_now and x_now<=510:
    Queryparams = '?' + 'serviceKey=' + '%2B6LwXwdSiXfBWg2A2q8IXzUCjGP13kzdct07M%2Bu6z9a%2BtwEhnndllUmg%2B9dzpW9ggINqxPfYck050bxzhUAPjw%3D%3D' \
                  + '&pageNo=' + '1' \
                  + '&numOfRows=' + '70' \
                  + '&dataType=' + 'XML' \
                  + '&base_date=' + y \
                  + '&base_time=' + '0200' \
                  + '&nx=' + '56' \
                  + '&ny=' + '124'
    print('0200')
elif 511<=x_now and x_now<=810:
    Queryparams = '?' + 'serviceKey=' + '%2B6LwXwdSiXfBWg2A2q8IXzUCjGP13kzdct07M%2Bu6z9a%2BtwEhnndllUmg%2B9dzpW9ggINqxPfYck050bxzhUAPjw%3D%3D' \
                  + '&pageNo=' + '1' \
                  + '&numOfRows=' + '70' \
                  + '&dataType=' + 'XML' \
                  + '&base_date=' + y \
                  + '&base_time=' + '0500' \
                  + '&nx=' + '56' \
                  + '&ny=' + '124'
    print('0500')
elif 811<=x_now and x_now<=1110:
    Queryparams = '?' + 'serviceKey=' + '%2B6LwXwdSiXfBWg2A2q8IXzUCjGP13kzdct07M%2Bu6z9a%2BtwEhnndllUmg%2B9dzpW9ggINqxPfYck050bxzhUAPjw%3D%3D' \
                  + '&pageNo=' + '1' \
                  + '&numOfRows=' + '70' \
                  + '&dataType=' + 'XML' \
                  + '&base_date=' + y \
                  + '&base_time=' + '0800' \
                  + '&nx=' + '56' \
                  + '&ny=' + '124'
    print('0800')
elif 1111<=x_now and x_now<=1410:
    Queryparams = '?' + 'serviceKey=' + '%2B6LwXwdSiXfBWg2A2q8IXzUCjGP13kzdct07M%2Bu6z9a%2BtwEhnndllUmg%2B9dzpW9ggINqxPfYck050bxzhUAPjw%3D%3D' \
                  + '&pageNo=' + '1' \
                  + '&numOfRows=' + '70' \
                  + '&dataType=' + 'XML' \
                  + '&base_date=' + y \
                  + '&base_time=' + '1100' \
                  + '&nx=' + '56' \
                  + '&ny=' + '124'
elif 1411<=x_now and x_now<=1710:
    Queryparams = '?' + 'serviceKey=' + '%2B6LwXwdSiXfBWg2A2q8IXzUCjGP13kzdct07M%2Bu6z9a%2BtwEhnndllUmg%2B9dzpW9ggINqxPfYck050bxzhUAPjw%3D%3D' \
                  + '&pageNo=' + '1' \
                  + '&numOfRows=' + '70' \
                  + '&dataType=' + 'XML' \
                  + '&base_date=' + y \
                  + '&base_time=' + '1400' \
                  + '&nx=' + '56' \
                  + '&ny=' + '124'
    print('1400')
elif 1711<=x_now and x_now<=2010:
    Queryparams = '?' + 'serviceKey=' + '%2B6LwXwdSiXfBWg2A2q8IXzUCjGP13kzdct07M%2Bu6z9a%2BtwEhnndllUmg%2B9dzpW9ggINqxPfYck050bxzhUAPjw%3D%3D' \
                  + '&pageNo=' + '1' \
                  + '&numOfRows=' + '70' \
                  + '&dataType=' + 'XML' \
                  + '&base_date=' + y \
                  + '&base_time=' + '1700' \
                  + '&nx=' + '56' \
                  + '&ny=' + '124'
    print('1700')
elif 2011<=x_now and x_now<=2310:
    Queryparams = '?' + 'serviceKey=' + '%2B6LwXwdSiXfBWg2A2q8IXzUCjGP13kzdct07M%2Bu6z9a%2BtwEhnndllUmg%2B9dzpW9ggINqxPfYck050bxzhUAPjw%3D%3D' \
                  + '&pageNo=' + '1' \
                  + '&numOfRows=' + '70' \
                  + '&dataType=' + 'XML' \
                  + '&base_date=' + y \
                  + '&base_time=' + '2000' \
                  + '&nx=' + '56' \
                  + '&ny=' + '124'
    print('2000')


url = url + Queryparams
result = requests.get(url).content

#bs_obj = BeautifulSoup(result.text, "html.parser")

#print(bs_obj)

xmlObject = xmltodict.parse(result)
allData = xmlObject['response']['body']['items']['item']








