import tkinter as tk
import subprocess

root = tk.Tk()

def run_monitor():
    subprocess.Popen(["python", "/home/pi/Desktop/main/monitor.py"])
def run_inone():
    subprocess.Popen(["python", "/home/pi/Desktop/main/upload.py"])
def stop_program():
    root.destroy()


button1 = tk.Button(root, text="查看本地監視器", command=run_monitor)
button2 = tk.Button(root, text="上傳監視器影像", command=run_inone)
button3 = tk.Button(root, text="關閉", command=stop_program)


button1.pack()
button2.pack()
button3.pack()

root.mainloop()
