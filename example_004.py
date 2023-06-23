# 이진화
# color 이미지 >> gray 이미지 >> 이진화 >> object 검출
import cv2

# # trackbar 설정
def dummy(x):
    pass

cv2.namedWindow('Binary')
cv2.createTrackbar('threshold', 'Binary', 0, 255, dummy)
cv2.setTrackbarPos('threshold', 'Binary', 80)

img_color = cv2.imread('./image_file/red_ball.jpg', cv2.IMREAD_COLOR)

cv2.imshow('Color', img_color)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray', img_gray)
cv2.waitKey(0)

while True:
    # Trackbar 값 가져오기
    low = cv2.getTrackbarPos('threshold', 'Binary')

    # 이진화 함수 cv2.threshold(이진화_대상_이미지, threshold, 4번째 arg가 cv2.THRESH_BINARY이고 이미지의 픽셀값이 cv2.THRESH_BINARY 보다 크면 255로, )
    # ret, img_binary = cv2.threshold(img_gray, low, 255, cv2.THRESH_BINARY)
    # 검출할 부분 흰색으로 하기 위해 반전(_INV)
    ret, img_binary = cv2.threshold(img_gray, low, 255, cv2.THRESH_BINARY_INV)

    cv2.imshow('Binary', img_binary)

    # 원본이미지와 binary 이미지 and 연산
    img_result = cv2.bitwise_and(img_color, img_color, mask=img_binary)

    cv2.imshow('Result', img_result)
    if cv2.waitKey(1) & 0xFF == 27:
        break

# # 이진화 함수 cv2.threshold(이진화_대상_이미지, threshold, 4번째 arg가 cv2.THRESH_BINARY이고 이미지의 픽셀값이 cv2.THRESH_BINARY 보다 크면 255로, )
# ret, img_binary = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)
#
# cv2.imshow('Binary', img_binary)
# cv2.waitKey(0)

cv2.destroyAllWindows()
