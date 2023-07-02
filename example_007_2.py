"""
07_2. Contours Approximation method :

    contours, hierarchy = cv2.findContours(image, mode, method[, contours[, hierarchy[, offset]]])
    :param image :
    :param mode :
    :param method : Contours Approximation method (contour를 구성하는 point 검출 방법을 지정)
        cv.CHAIN_APPROX_SIMPLE : contour의 시작점과 끝점(꼭지점)을 저장
        cv.CHAIN_APPROX_NONE : contour의 모든 경계점(변)을 저장

    :param contours :
    :param hierarchy :
    :param offset :
"""
import cv2 as cv


# 나중에 contour 그릴 때, color image에 그리기 우해, image를 color로 불러온다.
img_color = cv.imread("./image_file/lec_007/test.png")
# binary image로 변환 위해, color image를 gray scale image로 변환 전처리
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
# convert gray scale image to binary
ret, img_binary = cv.threshold(img_gray, 127, 255, 0)
# findContours 함수를 사용하여, contour 검출
# contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# # CHAIN_APPROX_SIMPLE는 contour의 시작점과 끝점(꼭지점)만 저장하므로, CHAIN_APPROX_NONE보다 memory 절약 가능
contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    for p in cnt:
        cv.circle(img_color, (p[0][0], p[0][1]), 10, (255, 0, 0), -1)

cv.imshow("result", img_color)
cv.waitKey(0)
