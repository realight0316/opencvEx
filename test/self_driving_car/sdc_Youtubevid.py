import pafy
import cv2
import numpy as np

def region_of_interest(img, vertices, color3=(255,255,255), color1=255): # ROI 셋팅

    mask = np.zeros_like(img) # mask = img와 같은 크기의 빈 이미지
    
    if len(img.shape) > 2: # Color 이미지(3채널)라면 :
        color = color3
    else: # 흑백 이미지(1채널)라면 :
        color = color1
        
    # vertices에 정한 점들로 이뤄진 다각형부분(ROI 설정부분)을 color로 채움 
    cv2.fillPoly(mask, vertices, color)
    
    # 이미지와 color로 채워진 ROI를 합침
    ROI_image = cv2.bitwise_and(img, mask)
    return ROI_image

def mark_img(img, blue_threshold=110, green_threshold=110, red_threshold=110): # 흰색 차선 찾기
    #  BGR 제한 값
    bgr_threshold = [blue_threshold, green_threshold, red_threshold]

    # BGR 제한 값보다 작으면 검은색으로
    thresholds = (frame[:,:,0] < bgr_threshold[0]) \
                | (frame[:,:,1] < bgr_threshold[1]) \
                | (frame[:,:,2] < bgr_threshold[2])
    mark[thresholds] = [0,0,0]
    return mark

url = 'https://youtu.be/ipyzW38sHg0'
video = pafy.new(url)
best = video.getbest(preftype="mp4")
print("best resolution : {}".format(best.resolution))

cap = cv2.VideoCapture(best.url) 
 
# 동영상 크기(frame정보)를 읽어옴
frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
 
# 동영상 프레임을 캡쳐
frameRate = int(cap.get(cv2.CAP_PROP_FPS))
 
frame_size = (frameWidth, frameHeight)
print('frame_size={}'.format(frame_size))
print('fps={}'.format(frameRate))
 
# cv2.VideoWriter_fourcc(*'코덱')
# codec 및 녹화 관련 설정
# 인코딩 방식을 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#fourcc = cv2.VideoWriter_fourcc(*'MPEG')
#fourcc = cv2.VideoWriter_fourcc(*'X264')
 
out1Path = 'data/recode1.mp4'
# out2Path = 'data/recode2.mp4'
 
# 영상 저장하기
# out1Path : 저장할 파일명
# fourcc : frame 압축 관련 설정(인코딩, 코덱 등)
# frameRate : 초당 저장할 frame
# frame_size : frame 사이즈(가로, 세로)
# isColor : 컬러 저장 여부
out1 = cv2.VideoWriter(out1Path, fourcc, frameRate, frame_size)
# out2 = cv2.VideoWriter(out2Path, fourcc, frameRate, frame_size)

while True:
    # 한 장의 이미지를 가져오기
    # 이미지 -> frame
    # 정상적으로 읽어왔는지 -> retval
    retval, frame = cap.read()
    if not(retval):
        break  # 프레임정보를 정상적으로 읽지 못하면 while문을 빠져나가기

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)	# 회색으로 컬러 변환
    # edges = cv2.Canny(gray, 100, 200)	# Canny함수로 엣지 따기
     
    height, width = frame.shape[:2]  # 이미지 높이, 너비

    # 사다리꼴 모형의 Points
    pts1 = np.array([[(240,height-40),(width/2-50, height/2+60), (width/2+135, height/2+60), (width-50,height-40)]], dtype=np.int32)
    vertices = pts1
    roi_img = region_of_interest(frame, vertices, (0,0,255)) # vertices에 정한 점들 기준으로 ROI 이미지 생성
    cv2.imshow('check', roi_img)
    mark = np.copy(roi_img)  # roi_img 복사
    mark = mark_img(roi_img)  # 흰색 차선 찾기
    
    # 흰색 차선 검출한 부분을 원본 image에 overlap 하기
    color_thresholds = (mark[:, :, 0] == 0) & (mark[:, :, 1] == 0) & (mark[:, :, 2] > 110)
    frame[color_thresholds] = [0, 0, 255]
    
    # 동영상 파일에 쓰기
    out1.write(frame)
    # out2.write(edges)
    # cv2.line(frame,(width//2-50, height//2+60), (width//2+135, height//2+60), (0,255,255), 1)
    # cv2.line(frame,(240,height-40), (width-50,height-40), (0,255,255), 1)
    cv2.polylines(frame, [pts1], True, (0,255,255))
    
    # 모니터에 출력
    cv2.imshow('frame', frame)
    # cv2.imshow('edges', edges)
    
    key = cv2.waitKey(frameRate)  # frameRate msec동안 한 프레임을 보여준다
    
    # 키 입력을 받으면 키값을 key로 저장 -> esc == 27
    if key == 27:
        break
        
if cap.isOpened():
    cap.release()
    out1.release()
    # out2.release()
    
cv2.destroyAllWindows()