#!/usr/bin/env python

# Python Offline Text to Speech
import pyttsx
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

def get_time():
	"""Returns the current time in normal english"""

	current_time = datetime.datetime.now().time()
	if current_time.hour > 12:
		return "It's " + str(current_time.hour - 12) + ' ' + str(current_time.minute) + "PM"
	else:
		return "It's" + str(current_time.hour) + ' ' + str(current_time.minute) + "AM"

def alarm():
	engine = pyttsx.init()
	time = get_time()
	engine.say(time)
	engine.runAndWait()

sched = BlockingScheduler()
sched.add_job(alarm, 'cron', minute=30)
sched.start()
