import cv2
import rospy
import numpy as np
import matplotlib.pyplot as plt
from geometry_msgs.msg import Twist

vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
vel_msg = Twist()

def edge_img(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    canny = cv2.Canny(blur,50,150)
    return canny

def reg_of_int(image):
    height = image.shape[0]
    # print(height, 'height')
    width = image.shape[1]
    # print(width, 'width')
    x = int(height/1.3)
    # print('x',x)
    box = np.array([
                   [0,height],[0,round(x)],[width,round(x)],[width,height]
                   ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, pts = [box], color =(255,255,255))
    masked_img = cv2.bitwise_and(image,mask)
    return masked_img

def lines_visualize(image, lines):
    region = []
    line_img = np.zeros_like(image)
    if lines is not None:
        # print(f'{lines =}')
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_img, (x1,y1), (x2,y2), (0,0,255), 5)
            # print(line)
            # cv2.imwrite('detected_lines_images/x1_{}_x2_{}_y1_{}_y2_{}.jpg'.format(x1,x2,y1,y2),line_img)
    p2, q2, p1, q1 = lines[0].reshape(4)
    # print(lines, 'length->',len(lines))
    p3, q3, p4, q4 = lines[1].reshape(4)
    m_x1 = int((p1+p4)/2)
    m_y1 = int((q1+q4)/2)
    m_x2 = int((p2+p3)/2)
    m_y2 = int((q2+q3)/2)
    region = np.array([
                      [p1,q1],[p2,q2],[p3,q3],[p4,q4]
                      ])
    
    cv2.fillPoly(line_img, pts = [region], color =(0,100,0))
    cv2.line(line_img, (m_x1,m_y1), (m_x2,m_y2), (0,255,255), 5)
    return line_img, x1, y1, x2, y2

def coordinates(image, line_params):
    # print('llll',line_params,'llll')
    slope, intercept = line_params
    y1 = image.shape[0]
    y2 = int(y1*(3/5))
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return np.array([x1, y1, x2, y2])

def average_slope_intersect(image, lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        params = np.polyfit((x1, x2), (y1, y2), 1)
        slope = params[0]
        intercept = params[1]
        if slope < 0 :
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    # print(left_fit)
    # print(right_fit)
    left_fit_avg = np.average(left_fit, axis = 0)
    right_fit_avg = np.average(right_fit, axis = 0)
    if left_fit_avg.all() == None:
        left_fit_avg = np.array([[0,0]])
        print('Left side not available!')
    if right_fit_avg.all() == None:
        right_fit_avg = np.array([[0,0]])
        print('Right side not available!')
    # print(left_fit_avg,'left')
    # print(right_fit_avg, 'right')
    left_line = coordinates(image, left_fit_avg)
    right_line = coordinates(image, right_fit_avg)
    return np.array([left_line, right_line])

def main_roadline(img_):
    # img_ = cv2.imread('road.jpg')

    img = cv2.resize(img_, (640,640), interpolation = cv2.INTER_AREA)
    # cv2.imshow('original',img)
    # cv2.waitKey(0)
    lane_img = np.copy(img)

    canny = edge_img(lane_img)
    interest_img = reg_of_int(canny)
    border_lines = cv2.HoughLinesP(interest_img,cv2.HOUGH_PROBABILISTIC, np.pi/180, 100, np.array([]), minLineLength = 40, maxLineGap = 5)

    # border_lines = cv2.HoughLinesP(canny, 2, np.pi/180, 100, np.array([]), minLineLength = 40, maxLineGap = 5)    
    avg_lines = average_slope_intersect(img,border_lines)
    lines_img, a, b, c, d = lines_visualize(lane_img,avg_lines)
    combined_img = cv2.addWeighted(lane_img, 0.8, lines_img, 1, 1)

    # plt.figure()
    plt.imshow(canny)
    # plt.show()
    # cv2.imshow('reg_of_int',interest_img)
    # cv2.imshow('input',canny)
    cv2.imshow('output',combined_img)
    cv2.waitKey(1)
    return combined_img
def print_():
    print("Printing from roadlines.py")
