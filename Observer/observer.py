import sys
import os

class Subject:
	def registerObserver(self, observer):
		"registerObserver not implemented"
		
	def removeObserver(self, observer):
		"removeObserver not implemented"
	
class Observer:
	def update(self, temp, humidity, pressure):
		raise NotImplementedError("update not implemented")

class DisplayElement:
	def display(self):
		raise NotImplementedError("display not implemented")

try:
	class WeatherData (Subject):
		observerList = []
		temp = 0.0
		humidity = 0.0
		pressure = 0.0
		
		def __init__ (self):
			pass
		
		def registerObserver(self, observer):
			self.observerList.append(observer)
		def measureChanged(self):
			for o in self.observerList:
				o.update(self.temp, self.humidity, self.pressure)
		def setMeasurement(self, temp, humidity, pressure):
			self.temp = temp
			self.humidity = humidity
			self.pressure = pressure
			self.measureChanged()
	
		
	class CurrentConditionDisplay (Observer, DisplayElement):
		def __init__ (self, subject):
			self.weatherData = subject
			self.weatherData.registerObserver(self)
		def update (self, temp, hu, press):
			self.temp = temp
			self.humidity = hu
			self.pressure = press
			self.display()
		def display(self):
			print "Current Condition: temp %d himidity %d pressure %d" % (self.temp, self.humidity, self.pressure)
	
	
	weatherCenter = WeatherData()
	currentDisplay = CurrentConditionDisplay(weatherCenter)

	weatherCenter.setMeasurement(10, 20, 100)
	
except NotImplementedError as err:
	print err


