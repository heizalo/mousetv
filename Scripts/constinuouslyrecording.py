from time import sleep
from picamera import PiCamera
from time import sleep
from picamera import PiCamera, Color
import datetime
import datetime as dt


#camera settings

camera = PiCamera()

storage_location = "/media/pi/ECFE-5DD5/"

filename = storage_location + datetime.datetime.now().strftime("%Y%m%d__%H-%M-%S ") + ".h264"

now = datetime.datetime.now()
#current_time = now.strftime("%Y-%m-%d %H:%M:%S")

camera.start_preview(alpha=200)

camera.resolution = (800, 800)


camera.start_recording(filename)

while True:
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    camera.annotate_text = current_time
    camera.annotate_text_size = 60
    camera.wait_recording(1)
    
    if input()=='q':
        break

    
camera.stop_recording()
camera.stop_preview()
