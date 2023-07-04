from time import sleep
from picamera import PiCamera, Color
import datetime
import time
import schedule

# camera settings
camera = PiCamera()

def start_recording():
    global recording
    recording = True
    storage_location = "/media/pi/076F-6A73/"
    filename = storage_location + datetime.datetime.now().strftime("%Y%m%d__%H-%M-%S ") + ".h264"
    camera.start_preview(alpha=200)
    camera.resolution = (800, 800)
    camera.start_recording(filename)
    while recording:
        now = datetime.datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        camera.annotate_text = current_time
        camera.annotate_text_size = 60
        camera.wait_recording(1)
        print("recording has started")
        
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

def stop_schedule():
    global recording
    recording = False
    print("Schedule stopped, will resume tomorrow at", start_time)

# start and stop time using 24-h
start_time = "20:36"
stop_time = "20:37"

schedule.every().day.at(start_time).do(start_recording)

recording = False
print("Schedule has started, recording will start at", start_time, "recording will stop at", stop_time)

while True:
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    if current_time == stop_time:
        stop_schedule()
        break
        print("break")
    time.sleep(1)
    
    
camera.stop_recording()
camera.stop_preview()
