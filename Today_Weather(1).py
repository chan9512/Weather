from pyowm import OWM
API_key = '8190682fd9f62950487ffc8784f229f8'
owm = OWM(API_key)
#-----------------------------오늘 날씨 ------------------------------------
obs = owm.weather_at_place('Incheon')
w = obs.get_weather()
W = "관측에러"
if(w.get_status()=="Clouds"):
    W ="구름조금"
elif(w.get_status()=="Haze"):
    W = "안개있음"
elif(w.get_status()=="Clear"):
    W = "맑은하늘"
elif(w.get_status()=="Rain"):
    W = "비가내림"
print('인천_오늘(기상상태, 현재온도) :', W, "," ,w.get_temperature(unit='celsius')['temp'], "˚C")
print('오늘(최고기온) :',  w.get_temperature(unit='celsius')['temp_max'],"˚C")
print('오늘(최저기온) :',  w.get_temperature(unit='celsius')['temp_min'],"˚C")

