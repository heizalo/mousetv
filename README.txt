This project uses an inexpensive raspberry pi 4. 

Here are some part that will be needed in order to make it work:

-Magnetic door sensor
-Raspberry pi camera CSI connector
-3d printed parts

This code built was created keeping in mind that the Universities Internet security constricted us from uploading files from/to network. In order to adapt to the current restriction this script was developed. The main idea here, is to use opening the door as a trigger to either continue to record or skip to the next name on the video.txt file.

First, power savings mode and the headless feature on a raspberry pi MUST be deactivate/activated 
Second, make sure the right GPIO is selected (no PIN)
Third, this script eventually will have a way to write files into a portable USB flash drive for easy storage and removal.
Fourth, make sure video.txt file has been updated with mouse name and time. Example file as how it can be done is shared , "example-video-txt". The name of the mouse/cohort must be included first adding ".h264" and leaving a space " " and after that adding the time in seconds "100 " 

Currently, the main OS has been cloned and stored for easy access in case the current OS gets corrupted. 

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

MouseTV project:

This project was created to be able to record and keep track of mice running set schedules, males and females. 


Let's start with the set up and things that you might need in order to have the Raspberry Pi set up:
Version of  Raspberry Pi, we are using the(Legacy) OS normally known as Debian 10 (buster) (https://www.raspberrypi.com/software/operating-systems/)
The easiest way to get it burned/flashed is using Raspberry Pi Imager ( https://www.raspberrypi.com/software/ ) Follow instructions 
Upon hours of testing, it was noticed the power saving mode was putting the Pi to sleep. Power saving mode must be deactivated 

  on terminal:
  go to $sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
  add lines
  @xset s noblank
  @xset s off
  @xset dpms
  
  Go to $sudo nano /etc/lightdm/lightdm.conf
  Add below line in to SeatDefault (or Seat:* in newer LightDM versions) section.
  SeatDefaults]
  xserver-command=X -s 0 -dpms
  Restart your Raspberry Pi.
  
  Lastly, network disabling (power saving mode as well)
  Check ,
  sudo iw wlan0 get power_save
  if it is "on" then execute
  sudo iw wlan0 set power_save off


Normally, there is not a need for a monitor to be connected at all times to the raspberry pi and for that it is necesary to have a "headless" pi, without it, it will not boot if not connected to a monitor. 
Adding hdmi_force_hotplug=1 to /boot/config.txt seems to have solves the problem.

Our interface for running the script is using SSH although due to having new people come into our lab we have opted for using VNC viewer which has a nice UI and facilitates easier connections to each raspberry pi

There are few libraries that will need to be updated as time goes by, this part will be updated with time.

