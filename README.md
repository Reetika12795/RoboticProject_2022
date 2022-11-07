## Earlier steps:
Calibration of pi camera.\
Get the image from camera and get the undistorted region of interest.


## Base architecture of our model
This project primarily uses two main steps , one for the detection of the line and one for the navigation of the robot to do so. The detection part first and foremost obtains an image from the turtlebot in the real environment , performs color thresholding , masking and centroid detection to communicate the required direction for the robot to move in . The direction is determined based on the position of the centroid of the detected lines with respect to the turtlebot. The direction published by the detection class is used by the navigation class to publish velocity commands to the Turtlebot and successfully follow the line throughout the environment.

![alt text](https://github.com/sudrag/line_follower_turtlebot/blob/master/UML/revised/ActivityDiagram_revised.png?raw=true)

## References:
https://github.com/sudrag/line_follower_turtlebot
