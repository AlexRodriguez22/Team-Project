from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.rotation = 60
camera.start_preview()
camera.annotate_text = "Sensor tripped"
sleep(5)
camera.capture('/home/pi/Desktop/text.jpg')
camera.start_recording('/home/pi/Desktop/video.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()