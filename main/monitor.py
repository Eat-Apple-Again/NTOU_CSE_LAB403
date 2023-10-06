import cv2

#JUST STREAMING
#選擇攝影機
#參考 https://www.ispyconnect.com/camera/d-link
cap1 = cv2.VideoCapture('rtsp://admin:1234@192.168.7.21/cam0/h264')
cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 720)

i = 0
count = 0
while(True):
  # 從攝影機擷取一張影像
  ret1, frame1 = cap1.read()

  #resize to 720*480
  if ret1:
    frame1 = cv2.resize(frame1,(720,480))
  else:
    break
  if i == 0:
    print(frame1.shape)
    i = 1
  
  # 顯示圖片(720, 480, 3)
  cv2.imshow('monitor', frame1)


  # 若按下 q 鍵則離開迴圈
  if cv2.waitKey(100) & 0xFF == ord('q'):
    break


# 釋放攝影機
cap1.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()