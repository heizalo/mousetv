This project uses an inexpensive raspberry pi 4. 

Here are some part that will be needed in order to make it work:

-Magnetic door sensor
-Raspberry pi camera CSI connector
-3d printed parts



change log:

Process on Raspberry Pi

Code written for raspberry pi, only local data at the moment. DONE
Possible router addition ( router purchased waiting for trials)


3d printed stuff for raspberry pi. POSSIBLY NEW BUILDS/PRINTS
Coming out with new prints, designs for easy attachment to the aluminum top part
Will be designing all in one enclosure for the raspberry pi, needs long jumper cord from raspberry pi to camera
Possible final design for the casing
Looking for possibilities of battery powered
   

LED strip coded. DONE

Putting camera code and light code together. DONE


Looking for a way to connect it to the network. IN PROGRESS
raspberry pi only connects to the “guest network” at the moment, need to be coded to work with universities “euroam” since it won't be able to connect to other software for remote manipulation (SSH and VNC)
At the moment, raspberry pi can not connect to WIFI
CHEAP WIFI ROUTER BOUGHT, can be remotely accessed 
Way around the network usage is local storage with flashdrive
Will try to re-route to be saved on flashdrives at the moment.

Sending data over network for storage and streaming.IN PROGRESS
DeepLabCut installation on workstations and home. DONE, need to be tested
DLC installed, waiting to test videos
OS corrupted, trying to reflash Operating system 10/06/2021
OS fully installed, data was moved over.
Final case and lights were installed
Had issues with wiring, shorts and LED being burned out
Code completed to save information on usb flash drive “/media/pi/5589-2846/” (https://pimylifeup.com/raspberry-pi-mount-usb-drive/)
Currently trying to fix preview issue from raspberry pi--FIXED ( VNC direct capture)
Fixed issue “headless” raspberry pi ( no monitor needed)
Adding hdmi_force_hotplug=1 to /boot/config.txt seems to have solved the problem. The Pi4 is running headless, and will be accessed via VNC.
Raspberry Pi, seems to get warm, will keep an eye on temperatures
Clone SD just in case.
New addition to the code, for automatic mp4 conversion normally videos are being saved as “.h264”
Code has been saved on raspberry pi  https://www.theamplituhedron.com/articles/How-to-convert-h264-to-mp4-with-MP4Box-on-Raspberry-Pi-in-Python/
Debugging at the moment

 17.	Static IP
https://www.weigu.lu/sb-computer/raspi_tips_tricks/index.html
