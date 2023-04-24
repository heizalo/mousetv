# MouseTV project:
![testIR](https://user-images.githubusercontent.com/89796977/213597478-f91575fc-635d-4f5d-a935-2c39b58a0d6b.GIF)


This is a work in progress will include a changelog as the project keeps on growing. 

In the most recent version of our Python script, we've changed it to continuously record video to address issues we encountered with door opening and closing. Additionally, we have implemented functionality to save recordings in separate folders with timestamps, making organization and access much more convenient.

Change log:
tqdm added for progressbar

This project uses an inexpensive Raspberry Pi 4.
Using a python script for triggers and the recording in an operant chamber.
This could be paired with DLC or SLEAP as a post process

Here are some part that will be needed in order to make it work:

-Magnetic door sensor
-Raspberry pi camera CSI connector
-3d printed parts

Change log:

-New scripts were generated for run and record 
-schedule library has been added for scheduled recordings
-Python script has been changed to continuosly recording due to 
issues when opening the door and closing.

-New design has been completed 

-Excel CSV files will be use to cut/snip videos as a post processing

-tqdm has been removed

![exploded view](https://user-images.githubusercontent.com/89796977/213819772-2a9da793-c162-4670-8b96-57fcdda6b1e4.jpg)
