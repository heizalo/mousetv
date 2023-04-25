from picamera import PiCamera
import time
import schedule
import datetime


#boolean operator (true or false) start_recording first passes throught should_record, if should_record is True then
#then it proceeds to record as normal, if False then it will not skipping the recording when script is executed
#if not should_record is equivalent to if should_record ==false, this uses a double negative sort of like saying
#if not recording then skip 

def start_recording(should_record):
    if not should_record:
        return

    print("Starting recording...")
    
    storage_location = "/mnt/usb1/"
    filename = storage_location + datetime.datetime.now().strftime("%Y%m%d__%H-%M-%S ") + ".h264"
  

    # Initialize PiCamera object
    camera = PiCamera()

    # Set camera resolution and framerate
    camera.resolution = (640, 480)
    #camera.framerate = 20

    # Start recording
    camera.start_recording(filename)

    # Record for 60 seconds
    camera.wait_recording(60)

    # Stop recording and release resources
    camera.stop_recording()
    camera.close()

    print("Recording stopped.")

# Schedule "day" can be replaced with monday, tues...
schedule.every().day.at("20:45").do(start_recording, True)

# Run the scheduling loop
while True:
    schedule.run_pending()
    time.sleep(1)

