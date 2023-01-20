import tqdm import tqdm
import time
import RPi.GPIO as GPIO
from picamera import PiCamera
from datetime import datetime

# Using GPIO location rather than PIN

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

camera = PiCamera()

#this file will remain on Desktop at the moment

with open('videos.txt', 'r') as f:
    
    # reads the video.txt file line
    a = ""
    
    for line in f:
        
        a += "Recording " + str(line) +  "seconds" + ".\n"
        print(a)
        # Splitting name and lenght from text file
        name, length = line.strip().split()
        # going from a str to int (integer)
        length = int(length)
        # Waits for the door to close 0.5 second can be increased to 1 min/ 60sec
        while GPIO.input(23) == 1:
            time.sleep(0.5)
            print("Door is Open.")
            continue
        print("Door is closed.")
        
        #configuration camera
        camera.resolution = (800, 800)

        # Start Recording
        camera.start_recording(name)
        start_time = time.time()

        #progress bar using tqdm using lenght which is in the text video
        for i in tqdm(range(length)):
            if GPIO.input(23) == 1:
                camera.stop_recording()
                print("Recording Stopped.")
                break
            else:
                time.sleep(1)
                continue
        else:
            camera.stop_recording()

GPIO.cleanup()
