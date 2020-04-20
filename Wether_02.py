import json
from datetime import datetime
from urllib.request import urlopen

def get_sky_info(data):
    try:
        weather_info = data['response']['body']['items']['item']
        if weather_info[3]['category']=='SKY':
            return weather_info[3]['fcstValue']
        elif weather_info[5]['category']=='SKY':
            return weather_info[5]['fcstValue']
    except KeyError:
        print('API 호출 실패!')

def get_base_time(hour):
    hour = int(hour)
    if hour<3:
        temp_hour = '20'
    elif hour<6:
        temp_hour = '23'
    elif hour<9:
        temp_hour = '02'
    elif hour<12:
        temp_hour = '05'
    elif hour<15:
        temp_hour = '08'
    elif hour<18:
        temp_hour = '11'
    elif hour<21:
        temp_hour = '14'
    elif hour<24:
        temp_hour = '17'

    return temp_hour + '00'

def get_weather():
    servicekeys = "%2B6LwXwdSiXfBWg2A2q8IXzUCjGP13kzdct07M%2Bu6z9a%2BtwEhnndllUmg%2B9dzpW9ggINqxPfYck050bxzhUAPjw%3D%3D"
    now = datetime.now()
    now_date = now.strftime('%Y%m%d')
    now_hour = int(now.strftime('%H'))

    if now_hour < 6:
        base_date = str(int(now_date) - 1)
    else:
        base_date = now_date
    base_hour = get_base_time(now_hour)

    numOfRows = '6'
    base_date = base_date
    base_time = base_hour
    nx = 1
    ny = 1
    dataType = 'json'
    api_url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst?serviceKey=%2B6LwXwdSiXfBWg2A2q8IXzUCjGP13kzdct07M%2Bu6z9a%2BtwEhnndllUmg%2B9dzpW9ggINqxPfYck050bxzhUAPjw%3D%3D&pageNo=1&numOfRows=10&dataType=XML&base_date=20200411&base_time=0500&nx=1&ny=1'

    data = urlopen(api_url).read().decode('utf8')
    json_data = json.loads(data)
    sky = get_sky_info(json_data)
    return sky
    #print(data)
weather = get_weather()
print(weather)