# 部署在養殖現場的 Raspberry Pi
有兩個資料夾: main 和 Rpi2Arduino

## main
    user.py 可以用tkinter介面執行各功能  
    monitor.py 用RTSP查看串流的監視器畫面  
    upload.py 上傳frame到GCP VM DB  
    modify_decision.py 重設GCP VM DB中的decision table  

### video
    用來採樣監視器畫面

    自動區分日期資料夾:
    recording.py 儲存影像(每隔10分鐘錄製兩段10秒鐘的影片)
    recording_perSecond.py 儲存影像(每秒儲存一個frame)

    不會自動區分日期資料夾:
    save_mp4.py 儲存影像(馬上儲存10秒鐘的影像)
    ticktack.py 每隔10分鐘執行一次save_mp4.py

## Rpi2Arduino
    用來和投餌機的ESP32進行序列埠通訊  
    電機系使用參數: Baud rate = 115200  

    fetch_to_arduino.py 從GCP VM DB 拿投餌指令並傳遞給ESP32  


## 更新github最新的repository
    在cmd下指令
    ```
        git fetch
        git reset  --hard origin/main
    ```