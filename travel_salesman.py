### The script and Travel Salesman always require a start point.

import math
import itertools
import csv
import time

start = time.time()

# Panel's global positions [x, y, z, yaw]
start_point = [0, 0, 0.2, 0]
panel_1st = [5.53, -6.72, 0.2, 0.1]
panel_2nd = [8.44, -6.45, 0.2, 0.1]
panel_3rd = [-4.3, 9.44, 0.2, 0.35]
panel_4th = [-1.53, 10.44, 0.2, 0.35]
panel_5th = [11.3, 4.72, 0.2, 0.35]
panel_6th = [10.77, 6.19, 0.7, 0.35]
panel_7th = [6, 17.17, 0.2, 0.8]
panel_8th = [-8.81, -0,61, 0.2, 0]
panel_9th = [-5.75, -10.61, 0.2, 0.6]
panel_10th = [-5.84, -8.77, 0.7, 0.6]
points = [start_point,panel_1st,panel_2nd,panel_3rd,panel_4th,panel_5th,
          panel_6th,panel_7th,panel_8th,panel_9th]


### Distance Matrix
distance_matrix = []
cs_size = 0 
points_number = []
print("Total global points: ", len(points))
def split_list(lst, chunk_size):
    chunks = []
    for i in range(0, len(lst), chunk_size):
        chunk = lst[i:i + chunk_size]
        chunks.append(chunk)
    return chunks

for i in points:
    xa,ya = i[0], i[1]
    for j in points:
        xb,yb = j[0], j[1]
        distance = math.sqrt(((xa - xb)**2) + ((ya - yb)**2))

        distance_matrix.append(distance)
        #distance_matrix[i][j] = distance
        #print(xa,ya, " to ",xb,yb , "distance", distance)
    cs_size +=1
    points_number.append(cs_size)
    cluster_size = cs_size

cluster = split_list(distance_matrix,cluster_size)
#print(cluster)
#print(cluster[0][0])
#print(points_number)
points_number.pop(0)
#print(points_number)
#print(cs_size)

combinations = list(itertools.permutations(points_number,cs_size-1))
#print(combinations)
posible_ways = len(combinations)
print("Possible ways: ",posible_ways)
#print(combinations[0])

### Distance measurement
total_distances = []
for i in combinations:
    #print(i)
    k = 1
    l = 0
    total_distance = 0

    for j in i:
        l +=1
        distance_l = cluster[k-1][j-1]
        #print(k,j, "distance: ",distance_l )
        k = j
        total_distance = total_distance +  distance_l

        if l == (cs_size-1):
            distance_l = cluster[0][j-1]   
            total_distance = total_distance +  distance_l
            total_distances.append(total_distance)
    
    #print("total distance: ", total_distance)
#print(total_distances)
path = total_distances.index(min(total_distances))
print(combinations[path])

compinations_path = combinations[path]

updated_path = [start_point]

points.insert(0,0) # to shift the points left

#updating path
for i in compinations_path:        
    #print(i)
    new_point = points[i]
    #print(new_point)
    updated_path.append(new_point)
updated_path.append(start_point)


end = time.time()
spended_time = int(end- start)
print ("Computation time: ", spended_time , " seconds !")

## Saving the updated points in "CSV" folder

print(updated_path)

with open("updated_path.csv", "w") as f:
    write = csv.writer(f)
    write.writerows(updated_path)