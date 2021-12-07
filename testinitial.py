import numpy as np
import cv2

img = cv2.imread(r"C:\Users\Sivasthigan\PycharmProjects\droneproject\1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
cv2.bitwise_not(threshold, threshold)
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
listx = []
listy = []

lst_coordinates=[]
fx = 0
fy = 0
for i in range(0, len(contours)):
    points = {}
    c = contours[i]
    size = cv2.contourArea(c)
    if size > 10:
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        firstPathdistance = np.sqrt((fx - cX) ** 2 + (fy - cY) ** 2)
        print("fidtance of first path", firstPathdistance)
        #distance = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        print(cX)
        # points.append{[cX, cY],firstPathdistance}
        points['cX']=cX
        points['cY']=cY
        points['firstPathdistance']=firstPathdistance
        lst_coordinates.append(points)
        cv2.circle(img, (0, 0), 5, (255, 0, 0), 10)
        cv2.circle(img, (cX, cY), 5, (255, 0, 0), 10)
        listx.append(cX)
        listy.append(cY)

    #    if len(points) >= 2:
            # joins the current point and
            # the previous point in the
            # list with a line

            #cv2.line(img, points[-1], points[-2],(0, 255, 255), 5)
            # a=points[-1]


            # x1=a[0]
            # y1=a[1]
            # b=points[-2]
            # x2=b[0]
            # y2=b[1]


                #print("other distance ", distance)





        # displays the image





print(lst_coordinates)
lst_sort=[]
for i in lst_coordinates:
    lst_sort.append(i['firstPathdistance'])
max_fp_dstance=min(lst_sort)
for i in lst_coordinates:
    for k,v in i.items():
        if (i[k]==max_fp_dstance):
            mX=i['cX']
            mY=i['cY']
            print("fjdk")
            cv2.line(img, (fx, fy), (mX, mY), (0, 255, 255), 5)
            cv2.imshow('image', img)
            break




# img = np.zeros((512, 512, 3),np.uint8)

cv2.waitKey(0)