import cv2
import json

# JUST STREAMING
# 參考 https://www.ispyconnect.com/camera/d-link
# cap = cv2.VideoCapture('rtsp://admin:451466@192.168.1.51/live/profile.0') # 印表機
# cap = cv2.VideoCapture('rtsp://admin:227182@192.168.1.21/live/profile.0') # 冷氣
# cap = cv2.VideoCapture('rtsp://Admin:1234@192.168.7.21/cam0/h264') # 現場Dynacolor

with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)
camera_config = config_data['camera_config']

# 建立RTSP連線
cap = cv2.VideoCapture(camera_config['dynacolor02'])

i = 0
while(True):
  # 從攝影機擷取一張影像
  ret1, frame1 = cap.read()

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
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()