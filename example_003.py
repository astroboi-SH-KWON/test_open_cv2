## 카메라로 부터 영상 가져오기
import cv2
import os

# 카메라에서 영상 캡처 가져오기
# cap = cv2.VideoCapture(0)  # 0은 첫번째 카메라, 2대 이상이면 1, 2, 3 ...
# cap_1 = cv2.VideoCapture(1)
# cap_2 = cv2.VideoCapture(2)

# 저장된 동영상 파일 불러 오기 (단, 영상 저장 코드 주석 처리)
cap = cv2.VideoCapture('./video_file/output.avi')


# os.makedirs('./video_file/', exist_ok=True)
# 이미지, 영상 저장
# 코덱 지정 (코덱명 : XVID)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# writer = cv2.VideoWriter('./video_file/output.avi', fourcc, 60.0, (640, 480))

# # 이미지 하나만 불러오기
# ret, img_color = cap.read()
# cv2.imshow("Color", img_color)
# cv2.waitKey(0)  # 기다리기

# 동영상 불러오기 (여러장 이미지 불러 오기)
while True:
    ret, img_color = cap.read()

    if ret == False:
        # continue  # 카메라가 이미지 못 불러오면 while 문 다시 시작
        break  # 저장된 동영상 끝나면 break

    # gray_scale 이미지 추가
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Color", img_color)
    cv2.imshow("Gray", img_gray)

    # writer.write(img_color)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC 키 입력시 break the loop
        break

# 객체 메모리 해제
cap.release()
# writer.release()
cv2.destroyAllWindows()
