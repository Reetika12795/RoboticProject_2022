import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
from roadlines import *

bridge = CvBridge()
pub = rospy.Publisher('detect_lane', Image, queue_size=10)

def image_callback(msg):
    print("Received an image!")
    try:
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError:
        print('error!')
    else:
        # cv2.imwrite('camera_image1.jpeg', cv2_img)
        img = main_roadline(cv2_img)
        # print(img)
        if img.all() == None:
            print("image error")
        ros_image = bridge.cv2_to_imgmsg(img, encoding="bgr8") 
        pub.publish(ros_image)

def main():
    rospy.init_node('image_listener')
    rospy.Subscriber("/camera/image", Image, image_callback)
    # rospy.Subscriber("/camera/image_projected_compensated", Image, image_callback)
    vel_pub.publish(vel_msg)
    rospy.spin()

if __name__ == '__main__':
    main()