from sense_hat import SenseHat
import time, numpy, datetime

# This script will graph and log the environment sensors.
# Temp, Humidity, and Pressure.
# Logs are the date, and then a squished-together time, like 231409 (11:14:09 PM)
# The data in logs shows the exact time (down to millisecond) the data was captured and graphed.

sense = SenseHat()
sense.clear()
time.sleep(1)
sense.set_rotation(180)

B = (10, 10, 255)
# humidity
R = (255, 5, 5)
# temp
G = (10, 255, 10)
# pressure
O = (0, 0, 0)

now = datetime.datetime.now()

day=now.day
month=now.month
year=now.year
hour=now.hour
minute=now.minute
second=now.second
msecond=now.microsecond

name = str(month) + "-" + str(day) + "-" + str(year) + "--" + str(hour) + str(minute) + str(second)
f = open("/home/pi/Documents/" + name + ".log", 'w')
f.write("Logging started at " + str(hour) + ":" + str(minute) + ":" + str(second) + " on " + str(month) + ":" + str(day) + ":" + str(year))
f.close()
def showMeters(number, noomber, nember):
	dater = round(number,0) / 8
	# round(dater,0)
	noom = 0
	arr = []
	while noom < round(dater,0):
		arr += [G]
		noom += 1
	# neum = 0
	while len(arr) < 8:
		arr +=  [O]
		# neum += 1
	daterse = round(noomber,0) / 8
	# round(daters,0)
	noomer = 0
	arrte = []
	while noomer < round(daterse,0):
		arrte += [R]
		noomer += 1
	# neum = 0
	while len(arrte) < 8:
		arrte +=  [O]
		# neum += 1
	daterste = round((round(nember,0) / 120),0)
	# round(daterste,0)
	noomee = 0
	arrtee = []
	while noomee < daterste:
		arrtee += [B]
		noomee += 1
	# neum = 0
	while len(arrtee) < 8:
		arrtee +=  [O]
		# neum += 1
	memes = [O, O, O, O, O, O, O, O]
	inerf= numpy.vstack((arr, arr, memes, arrte, arrte, memes, arrtee, arrtee))
	sense.set_pixels(inerf)

while True:
	now = datetime.datetime.now()
	pressure = sense.get_pressure()	
	temp = sense.get_temperature()
	humidity = sense.get_humidity()
	showMeters(humidity, temp, pressure)
	time.sleep(.05)
	day=now.day
	month=now.month
	year=now.year
	hour=now.hour
	minute=now.minute
	second=now.second
	msecond=now.microsecond
	f = open("/home/pi/Documents/" + name + ".log", 'a')
	f.write('\n' + "Data at: " + str(hour) + ":" + str(minute) + ":" + str(second) + ":" + str(msecond))
	f.write('\n' + "Humidity: " + str(humidity))
	f.write('\n' + "Temperature: " + str(temp))
	f.write('\n' + "Pressure: " + str(pressure))
	f.write('\n')
	f.close()
