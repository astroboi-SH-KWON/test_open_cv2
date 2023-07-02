"""
07_4. Contour 특징 사용하기 :
    1. 영역 크기 cv.contourArea : contour로 둘러싸인 영역의 pixel 수 return
    2. 근사화 : 곡석을 직선(일차함수)로 바꿈
    3. 무게 중심 : moments 함수를 사용하여 영역의 무게 중심을 그린다.
    4. 경계 사각형(Bounding Rectangle) : Object를 둘러싸는 최소 직사각형
    5. Convex Hull : contour를 모두 포함하는 block 다각형 그리기
                    block 다각형은 다각형을 구성하는 점끼리 연결했을 때, 다각형의 외부로 선분이 나가기 않는 것 의미
    6. Convexity Defects : 5.의 block 다각형 내부의 오목하게 들어간 부분

"""
import cv2 as cv
import numpy as np

# 나중에 contour 그릴 때, color image에 그리기 우해, image를 color로 불러온다.
img_color = cv.imread("./image_file/lec_007/test.png")
# binary image로 변환 위해, color image를 gray scale image로 변환 전처리
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
# convert gray scale image to binary
ret, img_binary = cv.threshold(img_gray, 127, 255, 0)
# findContours 함수에 매개변수중 mode값을 바꾸면서 return값인 hierarchy가 어떻게 변하는지 확인해 보자.
contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    cv.drawContours(img_color, [cnt], 0, (255, 0, 0), 3)

cv.imshow("result", img_color)
cv.waitKey(0)

print("1. 영역 크기 cv.contourArea ::::::::::::::::::::::::::::::::::::::::::::::")
### 1. 영역 크기 cv.contourArea ###################################################
for cnt in contours:
    area = cv.contourArea(cnt)
    print(f"contourArea : {area}")
### 1. 영역 크기 cv.contourArea ###################################################

print("\n2. 근사화 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
### 2. 근사화 ###################################################
for cnt in contours:
    epsilon = 0.02 * cv.arcLength(cnt, True)
    approx = cv.approxPolyDP(cnt, epsilon, True)

    cv.drawContours(img_color, [approx], 0, (0, 255, 255), 5)

cv.imshow("result", img_color)
cv.waitKey(0)
### 2. 근사화 ###################################################

print("\n3. 무게 중심 cv.moments ::::::::::::::::::::::::::::::::::::::::::::::::::")
### 3. 무게 중심 cv.moments ###################################################
for cnt in contours:
    M = cv.moments(cnt)

    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    cv.circle(img_color, (cx, cy), 10, (0, 0, 255), -1)
    epsilon = 0.02 * cv.arcLength(cnt, True)
    approx = cv.approxPolyDP(cnt, epsilon, True)

cv.imshow("result", img_color)
cv.waitKey(0)
### 3. 무게 중심 cv.moments ###################################################

print("\n4. 경계 사각형(Bounding Rectangle)  ::::::::::::::::::::::::::::::::::::::::")
### 4. 경계 사각형(Bounding Rectangle) ###################################################
for cnt in contours:
    x, y, w, h = cv.boundingRect(cnt)
    cv.rectangle(img_color, (x, y), (x+w, y+h), (0, 255, 0), 3)

cv.imshow("result", img_color)
cv.waitKey(0)

for cnt in contours:
    # # minAreaRect : 도형의 방향을 고려하여, bbox 생성
    rect = cv.minAreaRect(cnt)
    box = cv.boxPoints(rect)
    box = np.intp(box)
    cv.drawContours(img_color, [box], 0, (0, 0, 255), 3)

cv.imshow("result", img_color)
cv.waitKey(0)
### 4. 경계 사각형(Bounding Rectangle) ###################################################

print("\n5. Convex Hull : contour를 모두 포함하는 block 다각형 그리기  :::::::::::::::::::::")
### 5. Convex Hull : contour를 모두 포함하는 block 다각형 그리기 ##############################
for cnt in contours:
    hull = cv.convexHull(cnt)
    cv.drawContours(img_color, [hull], 0, (255, 0, 255), 5)

cv.imshow("result", img_color)
cv.waitKey(0)
### 5. Convex Hull : contour를 모두 포함하는 block 다각형 그리기 ###############################

print("\n6. Convexity Defects : 5.의 block 다각형 내부의 오목하게 들어간 부분  :::::::::::::::::::::")
### 6. Convexity Defects : 5.의 block 다각형 내부의 오목하게 들어간 부분 ##############################
for cnt in contours:
    hull = cv.convexHull(cnt, returnPoints=False)
    defects = cv.convexityDefects(cnt, hull)

    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])

        print(f"fixpt_depth :{d}")

        if d > 500:
            cv.line(img_color, start, end, [0, 255, 0], 5)
            cv.circle(img_color, far, 5, [0, 0, 255], -1)

        cv.imshow("result", img_color)
        cv.waitKey(0)
### 6. Convexity Defects : 5.의 block 다각형 내부의 오목하게 들어간 부분 ###############################