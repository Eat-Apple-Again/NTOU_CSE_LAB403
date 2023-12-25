import cv2
import os
from datetime import datetime

# 建立RTSP串流
# cap = cv2.VideoCapture('rtsp://admin:451466@192.168.1.51/live/profile.0') # 印表機
# cap = cv2.VideoCapture('rtsp://admin:227182@192.168.1.21/live/profile.0') # 冷氣
cap = cv2.VideoCapture('rtsp://Admin:1234@192.168.7.21/cam0/h264')

while True:
    try:
        # 從攝影機擷取一張影像
        ret, frame = cap.read()

        if ret:
            # 取得當前日期
            current_date = datetime.now().strftime("frames-%Y%m%d")

            # 檢查當前日期的資料夾是否存在，若不存在則創建
            current_dir = os.path.join("", current_date)
            os.makedirs(current_dir, exist_ok=True)

            # 以當前日期為檔名儲存當前幀
            frame_filename = os.path.join(current_dir, f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.jpg")
            cv2.imwrite(frame_filename, frame)

            # 顯示當前幀
            #cv2.imshow('Frame', frame)

            # 每秒1 fps，按q退出
            if cv2.waitKey(1000) & 0xFF == ord('q'):
                break
        else:
            break
    except Exception as e:
        print(f"錯誤發生：{e}")

# 釋放資源
cap.release()
cv2.destroyAllWindows()