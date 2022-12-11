# Autorace Thresholding
![Screenshot from 2022-12-11 14-44-41](https://user-images.githubusercontent.com/116564367/206907234-a2d777c3-6863-4c02-b242-e3ebadca1817.png)


This mothod takes image from turtlebot camera and creates warped image of the lane [warping points provided might change due to different scenario and screen size].

File for getting warping points is available run the below code to get warping points change video source accordingly-

Go to file directory and run -

```
python3 warp_point.py
```

After getting warp points, update it in 'autoracedetectlanethresholding.py' 'widthTop, heightTop, widthBottom, heightBottom = 38, 353, 71, 400'

Then run -

```
python3 autoracedetectlanethresholding.py
```

In main autorace package, change the topic in detect lane to subscribe to the topic that this package is publishing 'my_detect_lane'



https://user-images.githubusercontent.com/116564367/206907734-14dd6f7b-5183-494a-b848-92b84ffb8687.mp4


