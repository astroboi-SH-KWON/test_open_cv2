# # 웹캠에서 실시간으로 특정색 물체 추적하기

import cv2 as cv
import numpy as np

size_webcam = 30

hsv = 0
lower_blue1 = 0
upper_blue1 = 0
lower_blue2 = 0
upper_blue2 = 0
lower_blue3 = 0
upper_blue3 = 0


def nothing(x):  # nothing 이라는 callBack 함수 정의 (트랙바 생성위해 필수)
    pass


def mouse_callback(event, x, y, flags, param):
    global hsv, lower_blue1, upper_blue1, lower_blue2, upper_blue2, lower_blue3, upper_blue3, threshold  # # 전역변수 threshold 추가

    # 마우스 왼쪽 버튼 누를시 위치에 있는 픽셀값을 읽어와서 HSV로 변환합니다.
    if event == cv.EVENT_LBUTTONDOWN:
        print(img_color[y, x])
        color = img_color[y, x]

        one_pixel = np.uint8([[color]])
        hsv = cv.cvtColor(one_pixel, cv.COLOR_BGR2HSV)
        hsv = hsv[0][0]

        # # 트랙바에서 threshold 값 가져오기
        threshold = cv.getTrackbarPos('threshold', 'img_result')

        # HSV 색공간에서 마우스 클릭으로 얻은 픽셀값과 유사한 필셀값의 범위를 정합니다.
        if hsv[0] < 10:
            print("case1")
            lower_blue1 = np.array([hsv[0]-10+180, threshold, threshold])
            upper_blue1 = np.array([180, 255, 255])
            lower_blue2 = np.array([0, threshold, threshold])
            upper_blue2 = np.array([hsv[0], 255, 255])
            lower_blue3 = np.array([hsv[0], threshold, threshold])
            upper_blue3 = np.array([hsv[0]+10, 255, 255])
            #     print(i-10+180, 180, 0, i)
            #     print(i, i+10)

        elif hsv[0] > 170:
            print("case2")
            lower_blue1 = np.array([hsv[0], threshold, threshold])
            upper_blue1 = np.array([180, 255, 255])
            lower_blue2 = np.array([0, threshold, threshold])
            upper_blue2 = np.array([hsv[0]+10-180, 255, 255])
            lower_blue3 = np.array([hsv[0]-10, threshold, threshold])
            upper_blue3 = np.array([hsv[0], 255, 255])
            #     print(i, 180, 0, i+10-180)
            #     print(i-10, i)
        else:
            print("case3")
            lower_blue1 = np.array([hsv[0], threshold, threshold])
            upper_blue1 = np.array([hsv[0]+10, 255, 255])
            lower_blue2 = np.array([hsv[0]-10, threshold, threshold])
            upper_blue2 = np.array([hsv[0], 255, 255])
            lower_blue3 = np.array([hsv[0]-10, threshold, threshold])
            upper_blue3 = np.array([hsv[0], 255, 255])
            #     print(i, i+10)
            #     print(i-10, i)

        print(hsv[0])
        print("@1", lower_blue1, "~", upper_blue1)
        print("@2", lower_blue2, "~", upper_blue2)
        print("@3", lower_blue3, "~", upper_blue3)


cv.namedWindow('img_color')
cv.setMouseCallback('img_color', mouse_callback)

# # cv2의 트랙바 추가하여, 세츄레이션과 벨류값 조정하기
cv.namedWindow('img_result')
cv.createTrackbar('threshold', 'img_result', 0, 255, nothing)
# # 트랙바 초기값 threshold 30으로 셋팅
cv.setTrackbarPos('threshold', 'img_result', 30)

# # 웹캠 객체 생성
cap = cv.VideoCapture(0)

while True:
    # img_color = cv.imread('./image_file/lec_005/1.jpeg')
    # # 웹캠 객체에서 image 불러오기
    ret, img_color = cap.read()
    # # 웹캡 image 너무 커서, resize
    img_color = cv.resize(img_color, (16 * size_webcam, 9 * size_webcam))
    height, width = img_color.shape[:2]
    img_color = cv.resize(img_color, (width, height), interpolation=cv.INTER_AREA)

    # 원본 영상을 HSV 영상으로 변환합니다.
    img_hsv = cv.cvtColor(img_color, cv.COLOR_BGR2HSV)

    # 범위 값으로 HSV 이미지에서 마스크를 생성합니다.
    img_mask1 = cv.inRange(img_hsv, lower_blue1, upper_blue1)
    img_mask2 = cv.inRange(img_hsv, lower_blue2, upper_blue2)
    img_mask3 = cv.inRange(img_hsv, lower_blue3, upper_blue3)
    img_mask = img_mask1 | img_mask2 | img_mask3

    # 마스크 이미지로 원본 이미지에서 범위값에 해당되는 영상 부분을 획득합니다.
    img_result = cv.bitwise_and(img_color, img_color, mask=img_mask)

    cv.imshow('img_color', img_color)
    cv.imshow('img_mask', img_mask)
    cv.imshow('img_result', img_result)

    # cv.resizeWindow('img_color', 50, 50)
    # cv.resizeWindow('img_mask', 50, 50)
    # cv.resizeWindow('img_result', 50, 50)

    # ESC 키누르면 종료
    if cv.waitKey(1) & 0xFF == 27:
        break


cv.destroyAllWindows()