import pyttsx
import datetime

def get_time():
	"""Returns the current time in normal english"""
	current_time = datetime.datetime.now().time()
	if current_time.hour > 12:
		return str(current_time.hour - 12) + ' ' + str(current_time.minute) + "PM"
	else:
		return str(current_time.hour) + ' ' + str(current_time.minute) + "AM"

def alarm():
	engine = pyttsx.init()
	engine.say(get_time())
	engine.runAndWait()


alarm()