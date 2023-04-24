from picamera import PiCamera
import time
import schedule

def start_recording():
    
    print("Starting to record...")
    storage_location = "/mnt/usb1/"
    
    # filename includes time and date
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    filename = f"{timestamp}.h264"

    # Initialize PiCamera object
    camera = PiCamera()

    # Set camera resolution and framerate the res
    camera.resolution = (640, 480)
    #camera.framerate = 20

    # Start recording
    camera.start_recording(filename)

    # Record for in secods 60 sec = 1 min
    camera.wait_recording(60)

    # Stop recording and release camera, camera.close has to be set so it can record once again
    camera.stop_recording()
    camera.close()

    print("Recording has stopped.")

# Schedule "day" can be replaced with monday, tues... these can be removed if only 1 day per week needs to be active
schedule.every().monday.at("19:12").do(start_recording)
schedule.every().tuesday.at("19:12").do(start_recording)
schedule.every().wednesday.at("19:12").do(start_recording)
schedule.every().thursday.at("19:12").do(start_recording)
schedule.every().friday.at("19:12").do(start_recording)


start_recording()

# while loop running scheduled script
while True:
    schedule.run_pending()
    time.sleep(1)
