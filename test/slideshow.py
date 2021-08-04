# 테스트 테스트 테스트 테스트 테스트 테스트 테스트 테스트 테스트 테스트 테스트

import glob
import os
import cv2
import sys
import matplotlib.pyplot as plt

# 1.5초
interval = 1500

base_path = '\\Users\\JH\\opencvEx'
# img_path = '\Users\JH\opencvEx\ch01\images'
img_path = os.path.join(base_path, 'ch01/images/*.jpg')
img_files = glob.glob(img_path)
img_path2 = os.path.join(base_path, 'ch01/images/dog_image/*.jpg')
img_files2 = glob.glob(img_path2)


print(len(img_files))

if not img_files:
    print("img_files : no jpg files")
    sys.exit()

# 이미지 출력창 생성
cv2.namedWindow('image', cv2.WINDOW_NORMAL) 
# 이미지 출력창 크기를 최대로
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

idx = 0

while True:
    img = cv2.imread(img_files[idx])

    if img is None:
        print('Image load failed')
        break

    cv2.imshow('image', img)
    # ESC키 입력까지 슬라이드 진행
    if cv2.waitKey(interval) == 27:
        break

    idx += 1
    if idx >= len(img_files):
        idx = 0

    cv2.destroyWindow('image')

for x in range(len(img_files2)):

    img1 = cv2.imread(img_files2[x])
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.imread(img_files2[x+1])
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    img3 = cv2.imread(img_files2[x+2])
    img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
    img4 = cv2.imread(img_files2[x+3])
    img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)

    # 두 개의 영상을 함께 출력
    plt.subplot(221), plt.axis('off'), plt.imshow(img1)
    plt.subplot(222), plt.axis('off'), plt.imshow(img2)
    plt.subplot(223), plt.axis('off'), plt.imshow(img3)
    plt.subplot(224), plt.axis('off'), plt.imshow(img4)
    plt.show()

    plt.show(block = False)
    plt.pause(1)
    plt.close("all")
    