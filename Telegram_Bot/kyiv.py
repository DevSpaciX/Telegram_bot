from pyowm import OWM

city1 = ('Киев')
owm = OWM('a9ac329033caee40838a079f890fcfa9')
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city1)
w = observation.weather
temperature = w.temperature('celsius')['temp']
temperature1 = (str(temperature))
