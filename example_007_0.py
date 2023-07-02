"""
07_0. Contour : 특정 영역의 경계를 따라 같은 픽셀 강도를 갖는 지점을 연결하는 선
    모양 분석, 오브젝트 검출에 상용

    contours, hierarchy = cv2.findContours(image, mode, method[, contours[, hierarchy[, offset]]])
    :param image : black and white 의 binary image (실 image를 binary값으로 변환하거나, cany edge detect 사용하여 binary값으로 전처리)
    :param mode : Contour Retrieval mode (검출된 edge 정보를 계층 또는 list()로 저장하는 방식 지정)
    :param method : Contours Approximation method (contour를 구성하는 point 검출 방법을 지정 )
    :param contours : object의 외곽선 x, y 좌표 저장한 list() 객체
    :param hierarchy : contours의 구조 저장한 list() 객체
    :param offset : 지정한 크기만큼 contour를 구성하는 point 좌표를 이동하여 저장 (RoI를 사용하여, image 일부에서 contour를 추출한 후, 전체 image에서의 좌표를 구할 때 유용)
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

cv.imshow("result", img_color)
cv.waitKey(0)
