import sys
from heapq import heapify, heappush, heappop
def dijkstra(graph,src,dest):
    inf=sys.maxsize #to initialize the infinite function.
    node_data={
        '1':{'cost':inf, 'pred':[]},
        '2': {'cost': inf, 'pred': []},
        '3': {'cost': inf, 'pred': []},
        '4': {'cost': inf, 'pred': []},
        '5': {'cost': inf, 'pred': []},
        '6': {'cost': inf, 'pred': []},
        '7': {'cost': inf, 'pred': []},
        '0': {'cost': 0, 'pred': []},
    }
    #node_data[src]['cost']=0
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





if __name__=='__main__':
    graph={
        '0': {'5': 243.2385660210979, '6': 165.0969412193939, '7': 234.138847695123},
         '6': {'1': 117.6860229593982, '2': 183.17205026968497, '4': 94.81033698917012, '5': 82.86132994346639,'7': 91.0823802938856},
         '5': {'1': 36.0, '2': 104.7377677822093, '3': 238.9518780005715, '4': 33.24154027718932,'7': 40.52159917870962},
         '4': {'1': 51.85556864985669, '2': 89.47066558375433, '3': 237.8423847845459, '7': 73.54590403278758},
         '1': {'2': 81.98780397107853, '3': 204.00490190189058, '7': 46.32493928760188},
         '7': {'2': 128.2809416865966, '3': 240.30813552603666}, '2': {'3': 157.0350279396288},
        '2': {'3': 157.0350279396288}
    }
    source=str(0)
    destination=str(2)
    dijkstra(graph,source,destination)