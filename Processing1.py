import cv2
import numpy as np
import functions

#########################################
img = cv2.imread("hatali.jpeg")
widthImg=800
heightImg=640
questions = 10
choices = 5
ans= [3,1,4,0,2,0,3,4,1,2]
temp=0
i=0
j=0
#########################################

img = cv2.resize(img,(widthImg,heightImg))
imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgCanny = cv2.Canny(imgGrey,50,50)
imgContours = img.copy()
imgBiggestCont = img.copy()

#Konturleri bulma
contours, hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imgContours,contours,-1,(0,255,0),1)

cv2.imshow("a",imgContours)

#Dikdörtgenleri bulma
rectCon = functions.rectContours(contours)
biggestCon= functions.getCornerPoints(rectCon[0])

#Dikdörtgenlerin köşe noktalarını bulma
if biggestCon.size != 0:
    cv2.drawContours(imgBiggestCont,biggestCon,-1,(255,0,0),10)
    functions.reOrder(biggestCon)

    biggestCon = functions.reOrder(biggestCon)

    #Perspektif alma
    pts1 = np.float32(biggestCon)
    pts2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgWarped = cv2.warpPerspective(img,matrix,(widthImg,heightImg))

    imgWarpedGray = cv2.cvtColor(imgWarped,cv2.COLOR_BGR2GRAY)
    imgBlurred = cv2.GaussianBlur(imgWarpedGray,(5,5),0)
    imgCropped = imgBlurred[5:635,40:780]
    imgThreshold = cv2.adaptiveThreshold(imgCropped,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,155,11)

    boxes = functions.split(imgThreshold)

    #cv2.imshow("a",imgThreshold)

    myPixelVaL = np.zeros((questions,choices))
    countCol = 0
    countRow = 0

    #cv2.imshow("asd",imgContours)

    #Şıklardaki siyah olmayan piksellerin değerlerini alma
    for image in boxes:
        totalPixels = cv2.countNonZero(image)
        myPixelVaL[countRow][countCol] = totalPixels
        countCol+=1
        if (countCol == choices):countRow +=1; countCol=0
    #print(myPixelVaL)

    #İşaretli şıkkın konumunu bulma
    myIndex= []
    for x in range (0,questions):
        arr = myPixelVaL[x]
        myIndexVal = np.where(arr==np.amax(arr)) #Hangi sütunda olduğunu algılama
        #print(myIndexVal[0])
        #print(myPixelVaL[x])
        myIndex.append(myIndexVal[0][0])

    kutu0 = []
    for i in range(0,5):
        kutu0.append(cv2.countNonZero(boxes[i]))

    for i in range(0,len(kutu0)):
        for j in range(i+1,len(kutu0)):
            if (cv2.countNonZero(boxes[i]) < cv2.countNonZero(boxes[j])):
                temp = kutu0[i]
                kutu0[i] = kutu0[j]
                kutu0[j] = temp

    kutu1 = []
    for i in range(5,10):
        kutu1.append(cv2.countNonZero(boxes[i]))

    for i in range(0,len(kutu1)):
        for j in range(i+1,len(kutu1)):
            if (kutu1[i]<kutu1[j]):
                temp = kutu1[i]
                kutu1[i] = kutu1[j]
                kutu1[j] = temp

    kutu2 = []
    for i in range(10,15):
        kutu2.append(cv2.countNonZero(boxes[i]))

    for i in range(0, len(kutu0)):
        for j in range(i + 1, len(kutu0)):
            if (kutu2[i] < kutu2[j]):
                temp = kutu2[i]
                kutu2[i] = kutu2[j]
                kutu2[j] = temp

    kutu3 = []
    for i in range(15, 20):
        kutu3.append(cv2.countNonZero(boxes[i]))

    for i in range(0, len(kutu0)):
        for j in range(i + 1, len(kutu0)):
            if (kutu3[i] < kutu3[j]):
                temp = kutu3[i]
                kutu3[i] = kutu3[j]
                kutu3[j] = temp

    kutu4 = []
    for i in range(20, 25):
        kutu4.append(cv2.countNonZero(boxes[i]))

    for i in range(0, len(kutu0)):
        for j in range(i + 1, len(kutu0)):
            if (kutu4[i] < kutu4[j]):
                temp = kutu4[i]
                kutu4[i] = kutu4[j]
                kutu4[j] = temp

    kutu5 = []
    for i in range(25, 30):
        kutu5.append(cv2.countNonZero(boxes[i]))

    for i in range(0, len(kutu0)):
        for j in range(i + 1, len(kutu0)):
            if (kutu5[i] < kutu5[j]):
                temp = kutu5[i]
                kutu5[i] = kutu5[j]
                kutu5[j] = temp

    kutu6 = []
    for i in range(30, 35):
        kutu6.append(cv2.countNonZero(boxes[i]))

    for i in range(0, len(kutu0)):
        for j in range(i + 1, len(kutu0)):
            if (kutu6[i] < kutu6[j]):
                temp = kutu6[i]
                kutu6[i] = kutu6[j]
                kutu6[j] = temp

    kutu7 = []
    for i in range(35, 40):
        kutu7.append(cv2.countNonZero(boxes[i]))

    for i in range(0, len(kutu0)):
        for j in range(i + 1, len(kutu0)):
            if (kutu7[i] < kutu7[j]):
                temp = kutu7[i]
                kutu7[i] = kutu7[j]
                kutu7[j] = temp

    kutu8 = []
    for i in range(40, 45):
        kutu8.append(cv2.countNonZero(boxes[i]))

    for i in range(0, len(kutu0)):
        for j in range(i + 1, len(kutu0)):
            if (kutu8[i] < kutu8[j]):
                temp = kutu8[i]
                kutu8[i] = kutu8[j]
                kutu8[j] = temp

    kutu9 = []
    for i in range(45, 50):
        kutu9.append(cv2.countNonZero(boxes[i]))

    for i in range(0, len(kutu0)):
        for j in range(i + 1, len(kutu0)):
            if (kutu9[i] < kutu9[j]):
                temp = kutu9[i]
                kutu9[i] = kutu9[j]
                kutu9[j] = temp

    kutu = []
    kutu.append(kutu0[0])
    kutu.append(kutu1[0])
    kutu.append(kutu2[0])
    kutu.append(kutu3[0])
    kutu.append(kutu4[0])
    kutu.append(kutu5[0])
    kutu.append(kutu6[0])
    kutu.append(kutu7[0])
    kutu.append(kutu8[0])
    kutu.append(kutu9[0])

    grading=[]
    aa =[]
    for i in range(0,50):
        aa.append(cv2.countNonZero(boxes[i]))
        i=+i

    total=0
    #kutu'daki değerleri toplama
    for i in range(0, len(kutu)):
        total = total + kutu[i]
        abc = total/len(kutu)

    print(abc)

    hata0 = []
    for i in range(0,len(aa)):
        if aa[i] > abc-500:
            hata0.append(1)
        i=+i

    hatatoplam0 = (sum(hata0))

    blank = []
    false = []
    #Puanlama
    for x in range(0,questions):
        if hatatoplam0 > questions:
            print ("Bir soruda hatalı işareteleme yapmışsınız."
                   " Lütfen düzeltip tekrar deneyiniz.")
            cv2.waitKey(0)
        else:
            if kutu[x] < abc-1200:
                blank.append(1)
            elif ans[x] == myIndex[x]:
                grading.append(1)
            else:
                false.append(1)

    #print(grading)
    correctNum = (sum(grading)) #Puan
    falseNum = (sum(false))
    blankNum = (sum(blank))

    print("You have ",correctNum, "correct answer ",blankNum," blank and ",falseNum," false answers.")

cv2.imshow("asd",imgCropped)
cv2.imshow("das",imgThreshold)

cv2.waitKey(0)