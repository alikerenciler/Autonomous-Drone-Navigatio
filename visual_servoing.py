import math
import numpy as np

#Panel Locations
#panel_0 = [14, 8, 0.2, 1]
panel_1st = [10, 10, 0.2, 0]
panel_2nd = [5, 5, 0.2, 0.52]
panel_3rd = [-5, -10, 0.2, 0.87]
panel_4th = [-4.31, -9.25, 0.2, 0.87]  
panel_5th = [5, 10, 0.2, 4.04]

panel_locations = [panel_1st,panel_2nd,panel_3rd,panel_4th,panel_5th]

goals = [[0, 0, 3, 0]]


for i in panel_locations:
    a = 1 #panel widht
    h = math.sqrt(27/4) * a
    x,y,z,yaw = i[0],i[1],i[2],i[3]
    
    x1 = x + 2 * a * math.cos(yaw)
    y1 = y + 2 * a * math.sin(yaw)
    
    x2 = x - a * math.cos(yaw)
    y2 = y - a * math.sin(yaw)

    x3 = (x2+x1)/2
    y3 = (y2+y1)/2

    x4 = x3 + h * math.sin(yaw)
    y4 = y3 - h * math.cos(yaw)
    z = z + 3
    yaw = (yaw + 1.57) * 57.295
    #yaw = yaw * 57.295

    drone_positions = [x4, -y4, z, yaw]
    goals.append(drone_positions)
    
    """
    print(x,y,z,yaw)
    print(x1,y1,z,yaw)
    print(x2,y2,z,yaw)
    print(x3,y3,z,yaw)
    print(x4,y4,z,yaw)
    print("**************")
    """

    #print(x1,y1,h)
goals.append([0, 0, 3, 0])

print(goals)