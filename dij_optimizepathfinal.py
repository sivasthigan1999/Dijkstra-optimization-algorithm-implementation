import numpy as np
import cv2

img = cv2.imread(r"C:\Users\Sivasthigan\PycharmProjects\droneproject\1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
cv2.bitwise_not(threshold, threshold)
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
listx = []
listy = []
point=[]
points = []
lst_sort=[]

value = {}
megalist=[]


lst_coordinates=[]
fx = 0
fy = 0
index=0
w=0

for i in range(0, len(contours)):

    c = contours[i]
    size = cv2.contourArea(c)
    if size > 11:
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        points.append([cX,cY])

        cv2.circle(img, (fx, fy), 5, (255, 0, 0), 10)
        cv2.circle(img, (cX, cY), 5, (255, 0, 0), 10)
dictlis=[]
dictlis1=[]
for p in range(len(points)):
    dictlis.append([p+1,points[p]])
    dictlis1.append([p+1,points[p]])
print(dictlis)





for i in range(len(points)):

    grap = {}

    print('points',points)
    print('dictlis',dictlis)
    for j in points:

        points1 = {}
        Pathdistance = np.sqrt((fx-j[0]) ** 2 + (fy - j[1]) ** 2)
        #print('2nd time', fx, fy)
        #print("fidtance of first path", Pathdistance)
        points1['cX']=j[0]
        points1['cY']=j[1]
        points1['Pathdistance']=Pathdistance
        lst_coordinates.append(points1)
        #print(points1)
    print(lst_coordinates)
    #print(points1)


    for k in lst_coordinates:
        lst_sort.append(k['Pathdistance'])
    lst_sort.sort()
    max_fp_dstance = min(lst_sort)
    #print(lst_sort)


    for z in range(len(dictlis)):
        grap[str(dictlis[z][0])] =lst_coordinates[z]['Pathdistance']

    print('graph',grap)

    #megalist.append(graph)
    #print('mega',megalist)
    x = 0
    for t in lst_coordinates:
        # xx = i['cX']
        # yy = i['cY']
        # point.append([xx,yy])
        # print(point)
        index = index + 1
        for k, v in t.items():
            if (t[k] == max_fp_dstance):
                mX = t['cX']
                mY = t['cY']
                x = index
                break
        if (index == x):
            break
    fx=mX
    fy=mY

    value[str(w)] = grap
    for q in range (len(dictlis)):
        if dictlis[q][1]==[fx,fy]:

            #q=q+1
            #print(q)
            w=dictlis[q][0]
            print(w)
            break



    print(fx,fy)
    lst_coordinates.clear()
    lst_sort.clear()
    points.remove([fx,fy])
    dictlis.remove([w,[fx,fy]])
    #graph.clear()

print(value)

new1={}

for u,v in value.items():
    new = {}

    #print(v)
    for i,j in v.items():


        if j<250:
            print(i,j)
            new[str(i)]=j
    print(new)
    new1[str(u)]=new
   #new.clear()
    #print(new1)
print(new1)






import sys
from heapq import heapify, heappush, heappop
def dijkstra(graph,src,dest):
    inf=sys.maxsize #to initialize the infinite function.
    node_data = {}
    for i in range(8):
        node_data[str(i)] = {'cost': inf, 'pred': []}
    #node_data[src]['cost']=0
    node_data[src]['cost'] = 0
    visited=[] #accesed elements
    temp=src
    for i in range (4): #5= total no of vertices-1
        if temp not in visited:
            visited.append(temp)
            min_heap=[]
            for j in graph[temp]:
                if j not in visited:
                    cost=node_data[temp]['cost']+graph[temp][j]
                    if cost<node_data[j]['cost']:
                        node_data[j]['cost']=cost
                        node_data[j]['pred']=node_data[temp]['pred']+list(temp)
                    heappush(min_heap,(node_data[j]['cost'],j))
        heapify(min_heap)
        temp=min_heap[0][1]
    print('shortest Distance :'+str(node_data[dest]['cost']))
    print('shortest path: '+str(node_data[dest]['pred']+list(dest)))
    l=node_data[dest]['pred']+list(dest)
    point1 = [[0, 0]]

    for o in l:

        for n in dictlis1:

            if int(o)==n[0]:
                print(n)
                point1.append(n[1])

        print(o)
        if len(point1) >= 2:
            cv2.line(img, point1[-1], point1[-2],(0, 255, 255), 5)
    print(point1)
    #cv2.line(img, point1[-1], point1[-2], (0, 255, 255), 5)
    cv2.imshow('image', img)
    cv2.waitKey(0)

if __name__=='__main__':
    graph=new1
    source=str(0)
    destination=str(4)
    dijkstra(graph,source,destination)