# import the open weather data wrapper module
from pyowm import OWM
owm = OWM('38e787bc0a0a5c1c55f1c5723ac60301')

# Implement these classes: Factory, WeatherData, Wind, Humidity, Temperature
from abc import ABC, abstractmethod

class WeatherData(ABC):

    def __init__(self, location):
        self.location = location

    @abstractmethod
    def output(self):
        pass

class Wind(WeatherData):

    def __init__(self, location, wind_speed):
        super().__init__(location)
        self.wind_speed = wind_speed
    
    def output(self):
        print(f"Wind speed of {self.wind_speed} meter/sec in {self.location}")

class Temperature(WeatherData):

    def __init__(self, location, temperature):
        super().__init__(location)
        self.temperature = temperature
    
    def output(self):
        print(f"Temperature of {self.temperature}C in {self.location}")

class Humidity(WeatherData):

    def __init__(self, location, humidity):
        super().__init__(location)
        self.humidity = humidity

    def output(self):
        print(f"Humidity of {self.humidity}% in {self.location}")

class Factory:

    def __init__(self):
        self.mgr = owm.weather_manager()

    def createData(self, location, type):
        
        observation = self.mgr.weather_at_place(location)
        w = observation.weather

        if (type == "wind"):
            wind_speed = w.wind()["speed"]
            return Wind(location, wind_speed)
        elif (type == "temperature"):
            temperature = w.temperature('celsius')["temp"]
            return Temperature(location, temperature)
        elif (type == "humidity"):
            humidity = w.humidity
            return Humidity(location, humidity)
        else:
            print("Invalid type")

# Create factory object
factory = Factory()

# Create a WeatherData object of each type (Wind, Temperature, Humidity) at
# different locations so we can test our factory's createData instance method
weatherdata = [factory.createData("Hamilton,ON,CA","wind"), \
               factory.createData("Toronto,ON,CA","humidity"), \
               factory.createData("Ottawa,ON,CA","temperature")]

# Call the output method for each WeatherData object
for data in weatherdata:
    data.output()

# When I run the above code with my factory object and WeatherData objects
# implemented, I get the following:
#
#   Wind speed of 6.7 meter/sec in Hamilton,ON,CA
#   Humidity of 35% in Toronto,ON,CA
#   Temperature of 30.71C in Ottawa,ON,CA
#


