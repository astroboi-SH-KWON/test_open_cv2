import cv2
import os

# 이미지 불러오기
img_color = cv2.imread('./image_file/billiard.jpg', cv2.IMREAD_COLOR)  # cv2.IMREAD_COLOR, cv2.IMREAD_GRAYSCALE
                                                        # , cv2.IMREAD_UNCHANGED (투명도 정보 가진 이미지 파일)

# print(type(img_color))
# print(img_color)

cv2.namedWindow('Show Image')  # 생략 가능
cv2.imshow('Show Image', img_color)  # 'Show Image' 윈도우 식별자

cv2.waitKey(0)  # 초단위 기다리기. 0은 무한대

# gray_scale로 변환
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

cv2.imshow('Show GrayScale Image', img_gray)
cv2.waitKey(0)

os.makedirs('./image_file/', exist_ok=True)
# 이미지 저장
cv2.imwrite('./image_file/savedimage.jpg', img_gray)

cv2.destroyAllWindows()  # 윈도우 자원 닫기