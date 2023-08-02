import speedtest
import matplotlib .pyplot as plt
import time

list_download_speed = []
list_upload_Speed = []

for i in range(5):
    st = speedtest.Speedtest()
    download = round(st.download()/1000000, 2)
    list_download_speed.append(download)
    
    upload = round(st.upload()/1000000, 2)
    list_upload_Speed.append(upload)
    
    time.sleep(30)
    print(list_download_speed)
    print(list_upload_Speed)
    
    
x = [1,2,3,4,5]

plt.plot(x,list_download_speed,label = "Download Speed")
plt.plot(x,list_upload_Speed, label="Upload Speed")

plt.legend()
plt.title("Upload And Download Speed")
plt.show()
    