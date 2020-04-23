from pyowm import OWM
API_key = '8190682fd9f62950487ffc8784f229f8'
owm = OWM(API_key)
#-----------------------------오늘 날씨 ------------------------------------
obs = owm.weather_at_place('Incheon')
w = obs.get_weather()

print('인천_오늘(기상상태, 현재온도) :', w.get_status(), w.get_temperature(unit='celsius')['temp'])
print('오늘(최고기온) :',  w.get_temperature(unit='celsius')['temp_max'])
print('오늘(최저기온) :',  w.get_temperature(unit='celsius')['temp_min'])

print(w.get_rain())