import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 50) #50Hz
#DutyCycle to 5%  Full Left

print "Start"
pwm.start(3)

while True:
       for angle in range(3, 15):
	print angle
	pwm.ChangeDutyCycle(angle)        
	time.sleep(0.5)

print "finish"

pwm.stop()
GPIO.cleanup()

delay_period = 0.01

#while True:
#	pwm.ChangeDutyCycle(0)
#	time.sleep(5)
#	pwm.ChangeDutyCycle(50)
#	time.sleep(5)
#	pwm.ChangeDutyCycle(100)

def setServo(angle):
	duty = float(angle) / 10.0 + 2.5
	print "angle: %d duty:%d" % (angle, duty)
	pwm.ChangeDutyCycle(angle)

#while True:
#	for angle in range(5, 100):
#		setServo(angle)
#		time.sleep(delay_period)
#	for angle in range(5, 100):
#		setServo(100 - angle)
#		time.sleep(delay_period)


