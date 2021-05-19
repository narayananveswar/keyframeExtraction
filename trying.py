import cv2
import numpy as np
import pandas as pd 

cap = cv2.VideoCapture('production ID 5009493.mp4')

_, mainframe = cap.read()
#convert the main to gray scale 
mainframe = cv2.cvtColor(mainframe, cv2.COLOR_BGR2GRAY)
mainframedata = mainframe[0,0:]
_, frame = cap.read()
#convert next frame to gray
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
framedata = frame[0,0:]
#processing 
datatocompare = mainframedata + 20
comparison = datatocompare > framedata
print(comparison.all()) 
diff = np.remainder(mainframedata, framedata)
dict = {'mainframe':mainframedata, "framedata":framedata,"datatocompare":datatocompare, 'comparison':comparison}
df = pd.DataFrame(dict)
df.to_csv("data.csv")

if not comparison.all():
    cv2.imshow('frame', frame)
    cv2.imwrite("check.jpg", frame)

print("hai")
cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()