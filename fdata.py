import cv2
import numpy as np
import pandas as pd

cap = cv2.VideoCapture('production ID 5009493.mp4')

_, mainframe = cap.read()
grayframe = cv2.cvtColor(mainframe, cv2.COLOR_BGR2GRAY)
grayframedata = grayframe[0,0:]
_, frame = cap.read()
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
framedata = frame[0,0:]
diff = mainframedata - framedata
dict = {'mainframe':mainframedata, "framedata":framedata, 'diff':diff}
df = pd.DataFrame(dict)
df.to_csv("data.csv")
print(grayframedata)
print("....................................")
print(framedata)
