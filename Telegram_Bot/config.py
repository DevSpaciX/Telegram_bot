from pyowm import OWM

city = ('Украинка')
owm = OWM('a9ac329033caee40838a079f890fcfa9')
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather
temperature = w.temperature('celsius')['temp']
temperature = (str(temperature))
