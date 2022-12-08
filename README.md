## DEMO VIDEO ATTACH HERE 
## first page of project

<p align="center">  
   <img src = "ub.png" width = 200>
</p >

# <p align="center">University of Burgundy
</p > 

# <p align="center">Master of Computer vision and Robotics</p >   
<p align="center">  
   <img src = "vibot.png" width = 80>
</p >

# <p align="center">Robotics Project</p> 

## <p align="center">Under the guidance of:</p > 

<p align="center"> Joaquin RODRIGUEZ </p >     
<p align="center"> Raphael DUVERNE </p >   
<p align="center"> Renato MARTINS </p >   
 

## <p align="center">Team Members:</p >

<p align="center">REETIKA GAUTAM</p>
<p align="center">SEIKH KEBAB</p>


## Aim of the project
The bot will follow the path with detecting yellow line on it's left and white line on it's right in particular using autorace package.\
The bot will follow the mean path between these two detected lines.\
Even if it detects any one line with it's associated color the bot will behave normal.\
The bot must be able to pass through the tunnel. \
![alt text](https://github.com/Reetika12795/RoboticProject_2022/blob/main/1668436334462.jpg)

## Introduction(ABout tutbot3,type of camera used,robot modules)
The Robot Operating System (ROS) is an open source framework with a set of software libraries and tools that help us build robot application in a fastest way possible to build a robot! ROS provides standard operating system services such as hardware abstraction, low-level device control, implementation of commonly-used functionality, message-passing between processes, and package management. For our project we will use ROS Noetic.

The type of robot we program in our project is (TurtleBot3--![image](https://user-images.githubusercontent.com/33001160/206558392-fd1ff07e-a34f-487a-8b09-8f9e70f2838f.png)
). The turtlebot3 burger has the sensor such as a 360 Laser Distance Sensor and a Raspberry Pi Camera Module, control borads such as OpenCR1.0 (for low level control) and a Single Board Computer Raspberry Pi 3B+(for high level control and running ros Nodes). \
![image](https://user-images.githubusercontent.com/33001160/206553899-782737e8-cb23-4a91-888a-da50709cfb9a.png)

For Atonomous driving the camera module that we use for navigation is the raspi cam node which needs caliberation of both intrinsic and extrinsic parameters as to remove the effect of distortion to the images.


## prerequisites for the project
The Robot has to follow the lanes with yellow on the left and white on the right and the distance between the lane remains constant throught most part of the track(even in turns and in the tunnel). \
The robot has to autonomously drive between the two colored detected lines.



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
