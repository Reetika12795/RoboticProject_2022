# #!/usr/bin/env python

# import cv2
# import numpy as np
# import rospy
# from sensor_msgs.msg import Image,CompressedImage
# from cv_bridge import CvBridge
# # import rospkg


# # rospack = rospkg.RosPack()
# # packagePath = rospack.get_path('turtlebot3_autorace_detect')



# mainVideo = cv2.VideoWriter('detect_lane.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 20, (640,480))
# EqualizedVideo = cv2.VideoWriter('hist_equalized.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 20, (640,480))
# # YellowMaskVideo = cv2.VideoWriter('video_from_ros/test.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 20, (640,480))
# # WhiteMaskVideo = cv2.VideoWriter(packagePath+'/video/WhiteMaskVideo.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 15, (640,80 ))


# def fnShutDown():   
#     mainVideo.release()
#     EqualizedVideo.release()


# class rosCameraVideo:
#     def __init__(self):


#         self.Mainvideo = rospy.Subscriber('/detect/image_lane/compressed',CompressedImage,callback=self.CallBackMain)
#         self.EqualizedVideo = rospy.Subscriber('/eql_img',CompressedImage,callback=self.CallBackhisteql)
#         # self.Yellowmask = rospy.Subscriber('/image/yellow/compressed',CompressedImage,callback=self.CallBackYellow)
#         # self.WhiteMask = rospy.Subscriber('/image/white/compressed',CompressedImage,callback=self.CallBackMainWhite)

#         self.cvBridge = CvBridge()

#     def CallBackMain(self,msg):
#         image = self.cvBridge.compressed_imgmsg_to_cv2(msg,'bgr8')
#         if image is not None:        
#             mainVideo.write(image)

#     def CallBackhisteql(self,msg):
#         image = self.cvBridge.compressed_imgmsg_to_cv2(msg,'bgr8')
#         if image is not None:        
#             EqualizedVideo.write(image)

#     # def CallBackYellow(self,msg):
#     #     image = self.cvBridge.compressed_imgmsg_to_cv2(msg,'bgr8')
#     #     if image is not None:        
#     #         image = cv2.merge([image,image,image])
#     #         YellowMaskVideo.write(image)

#     # def CallBackMainWhite(self,msg):
#     #     image = self.cvBridge.compressed_imgmsg_to_cv2(msg,'bgr8')
#     #     if image is not None:   
#     #         image = cv2.merge([image,image,image])     
#     #         WhiteMaskVideo.write(image)

# if __name__ == '__main__':
#     rospy.init_node('video_record')
    
#     try:
#         vi = rosCameraVideo()
#         rospy.on_shutdown(fnShutDown)
#         rospy.spin()
#     except rospy.ROSException() as e:
#         print(e)


#!/usr/bin/env python
import cv2
import numpy as np
import rospy
from sensor_msgs.msg import Image,CompressedImage
from cv_bridge import CvBridge

mainVideo = cv2.VideoWriter('detect_lane.mp4', cv2.VideoWriter_fourcc('m','p','4','v'), 15, (640,480))
def fnShutDown():
    mainVideo.release()
class rosCameraVideo:
    def __init__(self):
        self.Mainvideo = rospy.Subscriber('/detect/image_lane/compressed',CompressedImage,callback=self.CallBackMain)
        self.cvBridge = CvBridge()
    def CallBackMain(self,msg):
        image = self.cvBridge.compressed_imgmsg_to_cv2(msg,'bgr8')
        
        if image is not None:  
            print("hehe")  
            # cv2.imshow('see',image)    
            # cv2.waitKey(1)
            mainVideo.write(image)


if __name__ == '__main__':
    rospy.init_node('video_record')
    try:
        vi = rosCameraVideo()
        rospy.on_shutdown(fnShutDown)
        rospy.spin()
    except rospy.ROSException() as e:
        print(e)