import cv2

video_file = './_self-learning/img/Owl.mp4'     # 비디오파일 경로 및 파일명

cap = cv2.VideoCapture(video_file)              # 동영상 캡쳐 객체 생성
if cap.isOpened():                              # 해당 객체 초기화 확인
    fps = cap.get(cv2.CAP_PROP_FPS)             # 프레임 수 구하기
    delay = int(1000/fps)
    print('FPS: %f, Delay: %dms'%(fps, delay))

    while True:
        ret, img = cap.read()                   # 다음 프레임 읽기
        if ret:                                 # 프레임이 정상이면 실행
            cv2.imshow(video_file, img)         # 화면에 표시
            cv2.waitKey(25)                     # fps에 맞춰서 화면 지연
        else:
            break                               # 다음 프레임 없으면 종료
else:
    print("can't open video.")
cap.release()                                   # 캡쳐 자원 반납
cv2.destroyAllWindows()

# ------------------------------------------------

cap = cv2.VideoCapture(0)                       # 0번 카메라 이용

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)       # 프레임 폭
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)     # 프레임 높이
print('Original width: %d, height: %d'%(width, height))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)          # 프레임 폭 320으로 설정
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)         # 프레임 높이 240으로 설정
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)       # 재설정한 프레임 폭
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)     # 재설정한 프레임 높이
print('Resized width: %d, Height: %d'%(width, height))

if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow('camera', img)           # 프레임 이미지 표시
            if cv2.waitKey(1) != -1:            # 1ms동안 키 입력 대기
                break                           # 아무키나 눌리면 중지
        else:
            print('no frame')
            break
else:
    print("can't open camera.")
cap.release()
cv2.destroyAllWindows()