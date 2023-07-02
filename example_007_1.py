"""
07_1. Contour 그리기

    contours, hierarchy = cv2.drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]])
    :param image : contour를 그릴 대상 color image
    :param contours : image 위에 그릴 contour가 저장한 list() 또는 vector 객체
    :param contourIdx : image 위에 그릴 특정 contour의 index (-1 : 모든 contour)
    :param color : contour의 색상 지정

"""
import cv2 as cv


# 나중에 contour 그릴 때, color image에 그리기 우해, image를 color로 불러온다.
img_color = cv.imread("./image_file/lec_007/test.png")
# binary image로 변환 위해, color image를 gray scale image로 변환 전처리
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
# convert gray scale image to binary
ret, img_binary = cv.threshold(img_gray, 127, 255, 0)
# findContours 함수를 사용하여, contour 검출
contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

###############################################
# # 모든 contour가 그려지게 contourIdx = -1
# cv.drawContours(img_color, contours, -1, (0, 255, 0), 3)
# # contourIdx = 0 그리기
cv.drawContours(img_color, contours, 0, (0, 255, 0), 3)
# # contourIdx = 1 그리기, 선색깔 (255, 0, 0)
cv.drawContours(img_color, contours, 1, (255, 0, 0), 3)

###############################################


cv.imshow("result", img_color)
cv.waitKey(0)

# # contour 그리기
