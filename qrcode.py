import cv2
import numpy as np
from pyzbar.pyzbar import decode

qr = cv2.imread("qr-code-kirp.png")
code = decode(qr)


for text in code:

    print(text.data)
    mydata=text.data

mydata=str(mydata)
mydataa=mydata.strip("'b")
print(mydataa)
a=mydataa.find("[")
b=mydataa.find("]")
anahtar=mydataa[(a+1):b]
testsayi=mydataa[0:(a)]
print(anahtar)
print(testsayi)








