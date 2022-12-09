import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
# from roadlines import *
bridge = CvBridge()
pub = rospy.Publisher('eql_img', Image, queue_size=10)
def image_callback(msg):
    print("Received an image!")
    try:
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError:
        print('error!')
    else:
        # cv2.imwrite('camera_image1.jpeg', cv2_img)
        # print('hi')
        # gray = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
        # eql_img_gray = hisEqulColor` (gray)
        # bgr_pub_img = cv2.cvtColor(eql_img_gray, cv2.COLOR_GRAY2BGR)
        img_eq = hisEqulColor(cv2_img)
        ros_image = bridge.cv2_to_imgmsg(img_eq, encoding="bgr8") 
        pub.publish(ros_image)

# def equalize_hist(img):
#     tmp = cv2.equalizeHist(img)
#     return tmp
# def hisEqulColor(img):
#     ycrcb=cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
#     channels=cv2.split(ycrcb)
#     # print (len(channels))
#     cv2.equalizeHist(channels[0],channels[0])
#     cv2.merge(channels,ycrcb)
#     cv2.cvtColor(ycrcb,cv2.COLOR_YCR_CB2BGR,img)
#     return img

def hisEqulColor(img):
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    channels=cv2.split(hsv)
    # print (len(channels))
    cv2.equalizeHist(channels[2])
    cv2.merge(channels,hsv)
    cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR,img)
    return img

def main():
    rospy.init_node('image_listener')
    # rospy.Subscriber("/camera/image", Image, image_callback)
    rospy.Subscriber("/camera/image_projected_compensated", Image, image_callback)
    rospy.spin()
if __name__ == '__main__':
    main()