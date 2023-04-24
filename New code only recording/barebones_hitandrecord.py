from picamera import PiCamera
import time
import datetime
import schedule

    
time_to_record = int(input("How long will you need to record?  "))
cohort_name = input("What is the cohort name?  ")

print("Starting to record...")

#location
storage_location = "/mnt/usb1/"

    

filename = storage_location + cohort_name + datetime.datetime.now().strftime("%Y%m%d__%H-%M-%S ") + ".h264"

# camera settings
camera = PiCamera()


camera.resolution = (640, 480)
#camera.framerate = 20

# Start recording
camera.start_recording(filename)

#just a conversion, min to seconds   
time_conversion = (time_to_record * 60)

camera.wait_recording(time_conversion)

# Stop recording and release resources
camera.stop_recording()
camera.close()

print("Recording stopped.")




