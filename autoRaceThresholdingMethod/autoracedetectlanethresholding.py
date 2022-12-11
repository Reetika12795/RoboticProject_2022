import cv2
import numpy as np
import rospy
from sensor_msgs.msg import Image,CompressedImage
from cv_bridge import CvBridge as bridge

pub = rospy.Publisher('my_detect_lane', Image, queue_size=10)

def warpImg(img,points,w,h,inv = False):
    pts1 = np.float32(points)
    pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
    if inv:
        matrix = cv2.getPerspectiveTransform(pts2, pts1)
    else:
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgWarp = cv2.warpPerspective(img,matrix,(w,h))
    return imgWarp

def getLaneCurve(img):

    hT, wT, c = img.shape
    widthTop, heightTop, widthBottom, heightBottom = 38, 353, 71, 400
    points = np.float32([(widthTop, heightTop), (wT-widthTop, heightTop),
                      (widthBottom , heightBottom ), (wT-widthBottom, heightBottom)])
    imgWarp = warpImg(img,points,wT,hT)
    histValues = np.sum(imgWarp, axis=0)
    print(np.max(histValues))
    if np.max(histValues) < 55000:
        ret,thresh1 = cv2.threshold(img,180,255,cv2.THRESH_BINARY)
        ret2,thresh2 = cv2.threshold(imgWarp,75,255,cv2.THRESH_BINARY)
    else:
        ret,thresh1 = cv2.threshold(img,180,255,cv2.THRESH_BINARY)
        ret2,thresh2 = cv2.threshold(imgWarp,180,255,cv2.THRESH_BINARY)

    # ret,thresh1 = cv2.threshold(img,180,255,cv2.THRESH_BINARY)
    # ret2,thresh2 = cv2.threshold(imgWarp,75,255,cv2.THRESH_BINARY)

    ros_image = bridge.cv2_to_imgmsg(thresh2, encoding="bgr8") 
    pub.publish(ros_image)
    
    cv2.imshow('thresh', thresh1)
    cv2.imshow('warp_thresh', thresh2)


def callback(img):
    getLaneCurve(img)

def main():
    rospy.init_node('detect_lane', anonymous=True)
    sub = rospy.Subscriber('/camera/image/compressed',CompressedImage,callback)
    rospy.spin()

if __name__ == '__main__':
    main()

