import numpy as np
import cv2


img = cv2.imread(r"C:\Users\Sivasthigan\PycharmProjects\droneproject\1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
cv2.bitwise_not(threshold, threshold)
contours, hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
listx = []
listy=[]

for i in range(0, len(contours)):
    c = contours[i]
    size = cv2.contourArea(c)
    if size > 12:
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.circle(img, (cX, cY), 5, (255, 0, 0), 10)
        listx.append(cX)
        listy.append(cY)

listxy = list(zip(listx,listy))
listxy = np.array(listxy)
print(listxy)

for i in range(0, len(listxy)):
    x1 = listxy[i,0]
    y1 = listxy[i,1]
    distance = 0
    secondx = []
    secondy = []
    dist_listappend = []
    sort = []
    for j in range(0, len(listxy)):
        if i == j:
            pass
        else:
            x2 = listxy[j,0]
            y2 = listxy[j,1]
            secondx.append(x2)
            secondy.append(y2)

            dist_listappend.append(distance)
            pathlength = sum(dist_listappend)

    secondxy = list(zip(dist_listappend,secondx,secondy))
    sort = sorted(secondxy, key=lambda second: second[0])
    sort = np.array(sort)




    cv2.line(img, (x1,y1), (int(sort[0,1]), int(sort[0,2])), (0,0,255), 1)

    cv2.putText(img, str(distance), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (255, 0, 0), 2, cv2.LINE_AA)

#sortDist = max(dist_listappend)

#print(sortDist)
cv2.imshow('img', img)
cv2.imwrite('connected2.png', img)
cv2.waitKey(0)