from pyowm import OWM
API_key = '8190682fd9f62950487ffc8784f229f8'
owm = OWM(API_key)

obs = owm.weather_at_place('Incheon')
w = obs.get_weather()

print('Incheon :', w.get_status(), w.get_temperature(unit='celsius')['temp'])
print('Incheon_Max :',  w.get_temperature(unit='celsius')['temp_max'])
print('Incheon_Min :',  w.get_temperature(unit='celsius')['temp_min'])

print(w.get_rain())