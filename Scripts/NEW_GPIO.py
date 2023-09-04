from picamera import PiCamera
import time
import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(x, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # "x" can be changed to the PIN that we will be using. Remember to use PIN # and not GPIO #


# Initialize PiCamera
camera = PiCamera()

# Set camera resolution and framerate (the higher the frame the higher the size of the file)
camera.resolution = (800, 800)
camera.framerate = 30


def start_recording(should_record):

    if should_record == False:
        return

    print("Starting to record...")
    
    storage_location = "/mnt/usb1/"
    filename = storage_location + datetime.datetime.now().strftime("%Y%m%d__%H-%M-%S ") + ".h264"
  
    # Start recording + filename which is the date and time
    camera.start_recording(filename)

while True:
    if GPIO.input(x)==False:
        start_recording(True)
        
    elif GPIO.input(x)==True:
        camera.stop_recording()
        print('Signal stopped, video recording is completed')
    time.sleep(1)

camera.close()
GPIO.cleanup()
print('Ready for the next video') #testing to see if resources have been freed.