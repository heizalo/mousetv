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


Change log:

-Python script has been changed to continuosly recording due to issues when opening the door and closing.
-New design has been completed 
-Excel CSV files will be use to cut/snip videos as a post processing
