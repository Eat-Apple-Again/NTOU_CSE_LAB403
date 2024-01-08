import cv2
import os
from datetime import datetime

# 設定影像大小
frame_width = 720
frame_height = 480

def save_image(frame):
    # 取得當前日期
    current_date = datetime.now().strftime("frames-%Y%m%d")

    # 檢查當前日期的資料夾是否存在，若不存在則創建
    current_dir = os.path.join("", current_date)
    os.makedirs(current_dir, exist_ok=True)

    # 以當前日期為檔名儲存當前幀
    frame_filename = os.path.join(current_dir, f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.jpg")
    cv2.imwrite(frame_filename, frame)
    print(f"影像已儲存至 {frame_filename}")

while True:
    try:
        # 建立RTSP串流
        cap = cv2.VideoCapture('rtsp://Admin:1234@192.168.50.251/cam0/h264')
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
        # 檢查是否成功連接
        if not cap.isOpened():
            raise Exception("Cannot connect to Camera~")
        

        # 從攝影機擷取一張影像
        ret, frame = cap.read()
        if not ret:
            raise Exception("Cannot read frames")
        frame = cv2.resize(frame, (frame_width, frame_height))
        
        # 顯示影像
        # cv2.imshow('monitor', frame)
        
        # 儲存影像
        save_image(frame)

    except Exception as e:
        print(f"錯誤發生：{e}")
    finally:
        # 釋放資源
        cap.release()
        cv2.destroyAllWindows()

''' 備用連結
# 格式參考 https://www.ispyconnect.com/camera/d-link
D-Link:
cap = cv2.VideoCapture('rtsp://admin:451466@192.168.1.51/live/profile.0') # 印表機
cap = cv2.VideoCapture('rtsp://admin:227182@192.168.1.21/live/profile.0') # 冷氣
Dynacolor:
cap = cv2.VideoCapture('rtsp://Admin:1234@192.168.7.21/cam0/h264')
cap = cv2.VideoCapture('rtsp://Admin:1234@192.168.50.250/cam0/h264')
cap = cv2.VideoCapture('rtsp://Admin:1234@192.168.50.251/cam0/h264')
'''