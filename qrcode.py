import cv2
import numpy as np
from pyzbar.pyzbar import decode
##### QR CODE READING
qr = cv2.imread("qr-code-kirp.png")
code = decode(qr)

##### QR Code'un içinde "Data" kısmını alma
for text in code:

    print(text.data)
    mydata=text.data

mydata=str(mydata) #DATA TO STR
mydataa=mydata.strip("'b") #CLEANING "DATA"
a=mydataa.find("[")
b=mydataa.find("]")
anahtar=mydataa[(a+1):b] #GETTING THE ANSWERS
testsayi=mydataa[0:(a)] #GETTING THE NUMBER OF QUESTIONS
ans=list(anahtar) #CONVERTING ANSWERS TO LIST
print(anahtar)
print(testsayi)












