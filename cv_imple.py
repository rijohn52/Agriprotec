import cv2
from imple_class import AnimalRecogonizer   ## A class for Animal classifier
import numpy as np

model = AnimalRecogonizer("/home/sreekesh/sreek/ML_projects/HACK_IMPULSE/scripts/model.json","/home/sreekesh/sreek/ML_projects/HACK_IMPULSE/scripts/model.h5")

cap = cv2.VideoCapture(0)
cas = cv2.CascadeClassifier("/home/sreekesh/sreek/ML_projects/HACK_IMPULSE/scripts/cas.xml")  ## Considering a small area for a 

while(True):
    _,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cases = cas.detectMultiScale(gray,1.4,5) # detection of the small area
    for (x,y,w,h) in cases:
        fc = gray[y:y+h,x:x+w]
        roi = cv2.resize(fc,(50,50)) 
        res = model.predict(roi[np.newaxis,:,:,np.newaxis])
        cv2.putText(frame,res,(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
    cv2.imshow('Dectector',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()