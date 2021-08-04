import cv2

img_file = './_self-learning/img/meerkat.jpg'           # 가져올 이미지 파일의 주소와 파일명
save_img = './_self-learning/img/meerkat_gray.jpg'      # 저장할 이미지 파일의 주소와 파일명

img_real = cv2.imread(img_file)                         # 가져온 이미지 파일을 읽어들임
img_gray = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)   # 가져온 이미지 파일을 회색조로 읽어들임

if img_real is not None:                                # 제대로 이미지가 로드되었으면 실행
    cv2.imshow('showshowshow', img_real)                # 'showshowshow'라는 창에 img_real 출력
    cv2.imshow('showshowgray', img_gray)                # 'showshowgray'라는 창에 img_gray 출력

    cv2.imwrite(save_img, img_gray)                     # save_img에 img_gray의 값으로 저장

    if cv2.waitKey() == 27:                             # 아스키코드 27번(ESC)이 입력되면 실행
        cv2.destroyAllWindows()                         # 모든 창을 닫는다
else:
    print('No image file.')                             # 이미지 로드 실패 시 출력
