import cv2
import os
from datetime import datetime
import schedule

# Resolution
frame_width = 720
frame_height = 480

def save_image(frame):
    # 取得今天日期
    current_date = datetime.now().strftime("frames-%Y%m%d")

    # 檢查今天日期的資料夾是否存在，若不存在就新建一個
    current_dir = os.path.join("", current_date)
    os.makedirs(current_dir, exist_ok=True)

    # 以今天日期為檔名儲存當前frame
    frame_filename = os.path.join(current_dir, f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.png")
    cv2.imwrite(frame_filename, frame, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    print(f"👍 影像已儲存: -> {frame_filename}")

def rtsp_connect():
    try:
        # 建立RTSP串流
        cap = cv2.VideoCapture('rtsp://Admin:1234@192.168.7.21/cam0/h264')
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)

        # 檢查是否成功連接
        if not cap.isOpened():
            raise Exception("Cannot connect to Camera ~ ")
        
        # 從攝影機擷取一張影像
        ret, frame = cap.read()
        if not ret:
            raise Exception("Cannot read frames😢")
        frame = cv2.resize(frame, (frame_width, frame_height))
        
        # 顯示影像
        # cv2.imshow('monitor', frame)
    except Exception as e:
        print(f"發生錯誤：{e}")
    finally:
        # 釋放資源
        cap.release()
        cv2.destroyAllWindows()
    return frame

def record():
    # 建立 RTSP 連線
    frame = rtsp_connect()
    # 儲存影像
    save_image(frame)

if __name__ == "__main__":
    # 每天的凌晨4點到晚上7點間，每隔10秒鐘儲存當下的一個frame
    schedule.every().day.at("04:00").to("19:00").every(10).seconds.do(record)
    while True:
        schedule.run_pending()


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