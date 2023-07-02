"""
07_3. Contours Retrieval Mode :

    contours, hierarchy = cv2.findContours(image, mode, method[, contours[, hierarchy[, offset]]])
    :param image :
    :param mode : Contour Retrieval mode (검출된 edge 정보를 계층 또는 list()로 저장하는 방식 지정)
        contour 찾은 결과를 어떻게 return 할지 결정
        findContours 함수를 이용하여, 이미지 contour를 검출하면, contour가 서로 다른 위치에 있을 수도 있고, contour 내부에 다른 contour가 있을 수 있음, 그래서
        mode 매개변수를 바꾸면서 return값인 hierarchy가 어떻게 변하는지 확인해 보자.
            1. cv.RETR_TREE : contour 내부에 다른 contour가 있으면 계층 구조로 만들어 줌
            2. cv.RETR_LIST : 모든 contour가 같은 계층의 level, 계층적인 특성이 필요 없는 경우
            3. cv.RETR_EXTERNAL : 가장 외곽에 있는 contour만 return, contour 내부의 자식 contour들은 무시
            4. cv.RETR_CCOMP : 모든 contour를 2개의 level 계층으로 재구성
                4-1 : Object 외부에 contour는 level 1
                4-2 : Object 내부에 contour는 level 2
    :param method :
    :param contours :
    :param hierarchy :
    :param offset :
"""
import cv2 as cv


# 나중에 contour 그릴 때, color image에 그리기 우해, image를 color로 불러온다.
img_color = cv.imread("./image_file/lec_007/hierarchy.png")
# binary image로 변환 위해, color image를 gray scale image로 변환 전처리
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
# convert gray scale image to binary
ret, img_binary = cv.threshold(img_gray, 127, 255, 0)
# findContours 함수에 매개변수중 mode값을 바꾸면서 return값인 hierarchy가 어떻게 변하는지 확인해 보자.
contours, hierarchy = cv.findContours(img_binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    cv.drawContours(img_color, [cnt], 0, (255, 0, 0), 3)

print(hierarchy)

cv.imshow("result", img_color)
cv.waitKey(0)
