## DEMO VIDEO ATTACH HERE 
## first page of project
## Introduction(ABout tutbot3,type of camera used,robot modules)
## Aim of the project
## prerequisites for the project
## Base architecture of the model(camera caliberation module -- intrinsic and extrinsic(reason), Set HSV value for detect lane, call control lane for path averaging)
## Implementation of code and the steps to execute
## Flochart of the architecture
## Conclusion
## References





## Earlier steps:
Calibration of pi camera.\
Get the image from camera and get the undistorted region of interest.

## Base architecture of the model:
The bot will follow the path with detecting yellow line on it's left and white line on it's right in particular using autorace package.\
The bot will follow the mean path between these two detected lines.\
Even if it detects any one line with it's associated color the bot will behave normal.\
![alt text](https://github.com/Reetika12795/RoboticProject_2022/blob/main/1668436334462.jpg)

## Demo Video:
https://www.youtube.com/watch?v=-YWwjlGPxko \
https://youtu.be/e2C2EWr9nHM

## Challenges:
If the yellow line is detected as white line due to poor lightning conditions the bot will face problems while taking a turn.
![alt text](https://github.com/Reetika12795/RoboticProject_2022/blob/main/Screenshot%20from%202022-11-14%2016-16-17.png)


## References:
https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/
