# # HSV 색공간에서 특정색 검출하기

# BGR to HSV

import numpy as np
import cv2


# color = [255, 0, 0]  # Blue in BGR
# # cv2 입력으로 사용하기 위해, 한 pixel 이미지로 변환
# pixel = np.uint8([[color]])
#
# # hsv 색공간으로 변환
# hsv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)
# # hsv 색공간 출력위해 pixel 값만 가져오기
# hsv = hsv[0][0]
#
# print(f"BGR : {color}")
# print(f"HSV : {hsv}")


# img_color = cv2.imread('./image_file/lec_005/1.jpeg')
img_color = cv2.imread('./image_file/lec_005/2.jpeg')
height, width = img_color.shape[:2]

img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)

lower_blue = (120 - 10, 30, 30)
upper_blue = (120 + 10, 255, 255)
img_mask = cv2.inRange(img_hsv, lower_blue, upper_blue)

img_result = cv2.bitwise_and(img_color, img_color, mask=img_mask)

cv2.imshow('img_color', img_color)
cv2.imshow('img_mask', img_mask)
cv2.imshow('img_result', img_result)

cv2.waitKey(0)
cv2.destroyAllWindows()


