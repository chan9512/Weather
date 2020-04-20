from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime
import time

url = 'http://api.openweathermap.org/data/2.5/forecast?id=1843564&mode=xml&appid=8190682fd9f62950487ffc8784f229f8'

result = requests.get(url)

bs_obj = BeautifulSoup(result.text, "html.parser")
print(bs_obj)

rstlist = []
resultmsg = bs_obj.find_all('')
for code in resultmsg:
    rstlist.append(code.text)

print(rstlist)


