# videoAppComplete.py
This is a motion detecting program that opens your video camera (likely your built-in one, not externals) detects motion differences, highlights them with boxes, and also captures the times there was motion in the video capture into a csv file.
- Requirement:
	- Open a video capture, capture motion in this video capture, draw boxes around the objects that are moving, and capture start and end times of objects movement into a file.
- Packages Used:
	- OpenCV via cv2
	- Pandas
- Data Source:
	- N/A.
	
# plotting.py
This is a program calls videoAppComplete to run, and once the capture is done, this program captures the DataFrame generated from videoAppComplete and visualizes the motion captures.

Output Graph:
![alt text](https://github.com/ctrios67/Python/blob/master/ActualPrograms/OpenCV_App/sample.png "Visual Example")

- Requirement:
	- Plot a time series graph of the motions captured in videoAppComplete.
- Packages Used:
	- bokeh
- Data Source:
	- Dataframe from videoAppComplete.
	
# Disclaimer
1.) Installing OpenCV is a pain in the ass, please conduct thorough research before doing so. Installation took me almost 3-4 days of dedicated work figuring what I did wrong with the installation on my Mac.
2.) Where I live in NYC, light barely hits my house, so every time I try this app I get crazy results. OpenCV works best in WELL LIT areas.