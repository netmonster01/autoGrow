import time
import datetime
import ephem
import random

#GPIO.setmode(GPIO.BOARD) 
#GPIO.setup(10, GPIO.OUT) 

# make sure "off_minutes" has a value
off_minutes = 1

while 1:
	print('in the loop')
	now = datetime.datetime.now()
	now_hours = time.localtime(time.time())[3]
	now_minutes = time.localtime(time.time())[4]
	# provide the program with information about the current location:
	# HS = Hobe Sound
	HS=ephem.Observer()
	HS.lat='27.0592'
	HS.lon='-80.1367'
	HS.date = now
	sun = ephem.Sun() 
	print('sun = '+str(sun))
	# figure out if it is daylight savings time or not:
	# isdst will be 1 if DST is currently enforced, 0 otherwise
	isdst = time.localtime().tm_isdst
	print('ist = '+str(isdst))
	# figure out when sunset is:
	sunset_hours = HS.next_setting(sun).tuple()[3]
	#sunset_hours will be in 24-hour GMT.
	if isdst == 1: #add 20 to the time for DST
		sunset_hours = sunset_hours + 20
	else: #add 19 to the time for EST
			sunset_hours = sunset_hours + 19
			sunset_minutes = HS.next_setting(sun).tuple()[4]
	# subtract 30 minutes from the time since it gets dark before actual sunset
	sunset_minutes = sunset_minutes - 30
	if sunset_minutes < 0:
		sunset_hours = sunset_hours - 1
	#sunset_mintues will be a negative number, so adding it to 60 will subtract it
	sunset_minutes = 60 + sunset_minutes
	# turn the light on if the hours and minutes match:
	if now_hours == sunset_hours and now_minutes == sunset_minutes:
		print('on')
#GPIO.output(10,True)
#also calculate a random time for the light to turn off
#this is in this "if" statement so it only calculates a random time once
#every 24 hours. 
	off_minutes = random.randint(0,59)
# turn the light off at the randomly selected minute in the 00 (midnight-1:00 AM) hour
	if now_hours == 0 and now_minutes == off_minutes:
		print('off')

	time.sleep(5)
	#GPIO.output(10,False)
# run once every 30 seconds:
