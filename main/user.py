import tkinter as tk
import subprocess

root = tk.Tk()

def run_monitor():
    subprocess.Popen(["python", "/home/pi/Desktop/NTOU_CSE_LAB403/main/monitor.py"])
def run_inone():
    subprocess.Popen(["python", "/home/pi/Desktop/NTOU_CSE_LAB403/main/upload.py"])
def run_toESP32():
    subprocess.Popen(["python", "/home/pi/Desktop/NTOU_CSE_LAB403/RPi2Arduino/fetch_to_arduino.py"])
def stop_program():
    root.destroy()


button1 = tk.Button(root, text="查看本地監視器", command=run_monitor)
button2 = tk.Button(root, text="上傳監視器影像", command=run_inone)
button3 = tk.bitton(root, text="傳遞指令給ESP32", command=run_toESP32)
button4 = tk.Button(root, text="關閉", command=stop_program)


button1.pack()
button2.pack()
button3.pack()
button4.pack()

root.mainloop()
