import kivy
import re
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import ObjectProperty

class SWLogic(BoxLayout):
	sw_time = ObjectProperty(None)
	isStart = None
	
	def start(self):
		self.isStart = True
	
	def stop(self):
		self.isStart = False
		
	def reset(self):
		self.sw_time.text = '00:00.00'
		self.isStart = False
	
	def update(self, dt):
		if self.isStart:
			time = self.sw_time.text
			min, sec, nano = re.split('\:|\.', time)
			
			nano = int(nano) + 2
			if nano ==  100:
				sec = int(sec) + 1
				nano = '10'
				if sec < 10:
					sec = '0' + str(sec)
				
			if sec == 60:
				min = str(int(min)) + 1
				sec = '00'
				
				
			time = str(min) +':'+ str(sec) +'.'+ str(nano)
			self.sw_time.text = time

class SWApp(App):
	def build(self):
		logic = SWLogic()
		Clock.schedule_interval(logic.update, 1/45)
		return logic
		
if __name__ == "__main__":
	app = SWApp()
	app.run()
