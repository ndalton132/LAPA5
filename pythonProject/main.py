import sys
import numpy as np
def parseFile(fileNum):
    with open("C:\\Users\\nickd\\OneDrive\\Pictures\\Screenshots\\School\\LinearAlgebraPA5\\Input_Files\\class_input_"+ str(fileNum) + "-2.txt") as file:
        input = file.readlines()
    array = [[float(num) for num in line.strip().split()] for line in input]
    return array

#print(parseFile('01'))


def bisector(v1,v2):
    M = np.divide(np.add(v1, v2), 2)
    norm = np.linalg.norm(np.subtract(v2, v1))
    normalize = np.divide(np.subtract(v2, v1), norm)
    #print(M)
    #print(normalize)

    c = (np.dot(normalize.ravel(), M.ravel()))*-1
    c = np.array([c])
    plane = np.array([[normalize[0]],[normalize[1]],[c]])

    #print(plane)


def distanceAndClosestPoint(v1,v2,p):
    #make a plane off of v1 and v2
    bisector(v1,v2)
    M = np.divide(np.add(v1, v2), 2)
    norm = np.linalg.norm(np.subtract(v2, v1))
    normalize = np.divide(np.subtract(v2, v1), norm)
    # print(M)
    # print(normalize)

    c = (np.dot(normalize.ravel(), M.ravel())) * -1
    c = np.array([c])
    plane = np.array([[normalize[0]], [normalize[1]],[normalize[2]], [c]])

    #d = c + n * p
    distance = c + np.dot(normalize.ravel(),p.ravel())
    #print(distance)

    #proj = d*n
    normal = v2 - v1
    x = p - distance *normal / np.linalg.norm(normal)
    print(x[0]," ",x[1]," ",x[2], " ", distance)
    #x = P- proj



def main(lines):
    p = np.array([[lines[0][0]], [lines[0][1]], [lines[0][2]]])
    q = np.array([[lines[0][3]], [lines[0][4]], [lines[0][5]]])
    r = np.array([[lines[0][6]], [lines[0][7]], [lines[0][8]]])
    #print(p,"  :  ",q)
    distanceAndClosestPoint(p, q, r)
    #bisector(p,q)
    for line in lines[1:]:
        v1 = np.array([[line[0]], [line[1]], [line[2]]])
        v2= np.array([[line[3]], [line[4]], [line[5]]])
        v3 = np.array([[line[6]], [line[7]], [line[8]]])
        #print(v1," : ",v2," : ",v3)
        distanceAndClosestPoint(v1, v2, v3)


lines = parseFile('2')
#print(lines)
main(lines)



# with open("C:\\Users\\nickd\\OneDrive\\Pictures\\Screenshots\\School\\LinearAlgebraPA5\\Part_B\\PartBOutput\\ndalton_output_B_1.txt", 'w') as f:
#     lines = parseFile(3)
#     lines.pop()
#
#     sys.stdout = f
#
#     main(lines)
#
#     sys.stdout = sys.__stdout__