from subprocess import run
import sys
import cv2
import  RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) #Setting the Mode to use. I am using the BCM setup
GPIO.setwarnings(False)

velocity = 100

runTime = .11
error = 0.03

stopTime = 0.1

iterations = 3

int1 = 21
int2 = 20

GPIO.setup(int1, GPIO.OUT)
GPIO.setup(int2, GPIO.OUT)

PWM1 = GPIO.PWM(21, 100)
PWM2 = GPIO.PWM(20, 100)

PWM1.start(0)
PWM2.start(0)



for i in range(0,iterations):
	cap = cv2.VideoCapture(0)
	while cap.isOpened()==False:
		print("Camera couldn't start. Trying again...")
		sleep(5)
		cap=cv2.VideoCapture(0)
	print("iter:" +  str(i))
	GPIO.output(int2,False)
	PWM1.ChangeDutyCycle(velocity)
	sleep(runTime)
	GPIO.output(int1, GPIO.LOW)
	PWM1.ChangeDutyCycle(0)
	GPIO.output(int2, False)
	sleep(0.1)
	ret, img = cap.read()
	imagename = "test.jpg"
	cv2.imwrite(imagename, img)
	run(["python", "-W", "ignore",  "detect.py", imagename])
	run(["python", "-W", "ignore", "spreadsheet.py", ])
	run(["python","-W", "ignore", "identify.py", ])
	run(["rm", "test.jpg"])
	cap.release()
	sleep(stopTime)

for i in range(0,iterations):
	cap = cv2.VideoCapture(0)
	while cap.isOpened()==False:
		print("Camera couldn't start. Trying again...")
		sleep(5)
		cap=cv2.VideoCapture(0)
	print("iter:" +str(i))
	GPIO.output(int1, False)
	PWM2.ChangeDutyCycle(velocity)
	sleep(runTime-error)
	GPIO.output(int2, GPIO.LOW)
	PWM2.ChangeDutyCycle(0)
	GPIO.output(int1, False)
	sleep(0.1)
	ret, img = cap.read()
	imagename = "test.jpg"
	cv2.imwrite(imagename, img)
	run(["python", "-W", "ignore",  "detect.py", imagename])
	run(["python", "-W", "ignore", "spreadsheet.py", ])
	run(["python","-W", "ignore", "identify.py", ])
	run(["rm", "test.jpg"])
	cap.release()
	sleep(stopTime)

for i in range(0,iterations):
	cap = cv2.VideoCapture(0)
	while cap.isOpened()==False:
		print("Camera couldn't start. Trying again...")
		sleep(5)
		cap=cv2.VideoCapture(0)
	print("iter:" +str(i))
	GPIO.output(int1, False)
	PWM2.ChangeDutyCycle(velocity)
	sleep(runTime)
	GPIO.output(int2, GPIO.LOW)
	PWM2.ChangeDutyCycle(0)
	GPIO.output(int1, False)
	sleep(0.1)
	ret, img = cap.read()
	imagename = "test.jpg"
	cv2.imwrite(imagename, img)
	run(["python", "-W", "ignore",  "detect.py", imagename])
	run(["python", "-W", "ignore", "spreadsheet.py", ])
	run(["python","-W", "ignore", "identify.py", ])
	run(["rm", "test.jpg"])
	cap.release()
	sleep(stopTime)

for i in range(0,iterations):
	cap = cv2.VideoCapture(0)
	while cap.isOpened()==False:
		print("Camera couldn't start. Trying again...")
		sleep(5)
		cap=cv2.VideoCapture(0)
	print("iter:" +str(i))
	GPIO.output(int2,False)
	PWM1.ChangeDutyCycle(velocity)
	sleep(runTime-error/2)
	GPIO.output(int1, GPIO.LOW)
	PWM1.ChangeDutyCycle(0)
	GPIO.output(int2, False)
	sleep(0.1)
	ret, img = cap.read()
	imagename = "test.jpg"
	cv2.imwrite(imagename, img)
	run(["python", "-W", "ignore",  "detect.py", imagename])
	run(["python", "-W", "ignore", "spreadsheet.py", ])
	run(["python","-W", "ignore", "identify.py", ])
	run(["rm", "test.jpg"])
	cap.release()
	sleep(stopTime)

GPIO.cleanup()
