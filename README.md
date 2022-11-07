## Earlier steps:
Calibration of pi camera.\
Get the image from camera and get the undistorted region of interest.


## Base architecture of our model
This project primarily uses two main classes , one for the detection of the line and one for the navigation of the robot to do so. The detection class first and foremost obtains an image from the turtlebot in the real environment , performs color thresholding , masking and centroid detection to communicate the required direction for the robot to move in . The direction is determined based on the position of the centroid of the detected line with respect to the turtlebot .The direction commands are either move forward , turn left , turn right or search i.e spin on spot when no line is detected. The direction published by the detection class is used by the navigation class to publish velocity commands to the Turtlebot and successfully follow the line throughout the environment. Once the Turtlebot reaches the end of the path , it searches for a line to follow again by rotating on spot. This way it finds the same path it took and returns back to the starting point. This way travelling between these points is performed continuously and can be extremely beneficial in any material handling applications. The procedure follows the algorithm shown in the picture below.

![alt text](https://github.com/sudrag/line_follower_turtlebot/blob/master/UML/revised/ActivityDiagram_revised.png?raw=true)

## References:
https://github.com/sudrag/line_follower_turtlebot
