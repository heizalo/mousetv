This project uses an inexpensive raspberry pi 4. 

Here are some part that will be needed in order to make it work:

-Magnetic door sensor
-Raspberry pi camera CSI connector
-3d printed parts

This code built was created keeping in mind that the Universities Internet security constricted us from uploading files from/to network. In order to adapt to the current restriction this script was developed.

First, power savings mode and the headless feature on a raspberry pi MUST be deactivate/activated 
Second, make sure the right GPIO is selected (no PIN)
Third, this script eventually will have a way to write files into a portable USB flash drive for easy storage and removal.
Fourth, make sure video.txt file has been updated with mouse name and time. Example file as how it can be done is shared , "example-video-txt". The name of the mouse/cohort must be included first adding ".h264" and leaving a space " " and after that adding the time in seconds "100 " 

Currently, the main OS has been cloned and stored for easy access in case the current OS gets corrupted. 


