from time import sleep
from picamera import PiCamera
from time import sleep
from picamera import PiCamera, Color
import datetime
import datetime as dt
import time
import schedule



#camera settings

camera = PiCamera()

def start_recording():
    
    global recording
    recording = True
    
    storage_location = "/media/pi/076F-6A73/"

    filename = storage_location + datetime.datetime.now().strftime("%Y%m%d__%H-%M-%S ") + ".h264"

    now = datetime.datetime.now()
    #current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    camera.resolution = (800, 800)


    camera.start_recording(filename)

    while recording:
        now = datetime.datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        camera.annotate_text = current_time
        camera.annotate_text_size = 60
        camera.wait_recording(1)
        
        if not recording:
            break
         
         
    camera.stop_recording()


def run_schedule():
    while schedule_running:
        schedule.run_pending()
        time.sleep(1)

def stop_schedule():
    global schedule_running
    global recording
    recording = False
    print("Schedule stopped, will resume tomorrow at" f"{start_time}")


        
#start and stop time using 24-h

start_time = "19:32"
stop_time = "19:33"

schedule.every().day.at(start_time).do(start_recording)
schedule.every().day.at(stop_time).do(stop_schedule)


schedule_running= True
print("Schedule has started, recording will start at" "" f"{start_time}", "recording will stop at" "" f"{stop_time}")
run_schedule()

