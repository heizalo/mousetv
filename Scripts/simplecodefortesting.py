import time
import RPi.GPIO as GPIO
from picamera import PiCamera

# Set up the GPIO pins for the door sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)


camera = PiCamera()

with open('videos.txt', 'r') as f:
    # Read the file line by line
    string = ""
    
    for line in f:
        
        
        string += "Recording " + str(line) +  "seconds" + ".\n"
        
        print(string)
                
        # Split the line into the name and length
        name, length = line.strip().split()
        # Convert the length to a number (in seconds)
        length = int(length)

        # Wait for the door to close
        while GPIO.input(23) == 1:
            time.sleep(0.2)
            print("recording")
            
            if GPIO.input(23) == 1:
                print(f"Door is open, the next name on the list, {name} will start recording")
                break

        #configuration camera
        camera.resolution = (800, 800)
        # Start recording the video
        camera.start_recording(name)
        
        # Record for the specified length
        camera.wait_recording(length)
        # Stop recording
        camera.stop_recording()
        
        #if GPIO.input(23) == 0:
         #   time.sleep(10)
          #  print("Recording ended please Ctrl + C to end for the day")
# Clean up the GPIO pins
GPIO.cleanup()