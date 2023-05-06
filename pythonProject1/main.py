import sys
import numpy as np
def parseFile(fileNum):
    with open("C:\\Users\\nickd\\OneDrive\\Pictures\\Screenshots\\School\\LinearAlgebraPA5\\Input_Files\\class_input_"+ str(fileNum) + "-2.txt") as file:
        input = file.readlines()
    array = [[float(num) for num in line.strip().split()] for line in input]
    return array

#print(parseFile(0))


def normal(p,q,r):
    v = np.subtract(q,p)
    w = np.subtract(r, p)
    numerator = (np.cross(v,w))
    denominator = (np.linalg.norm(np.cross(v,w)))
    #print(numerator, "  :  ",denominator)
    if(denominator == 0):
        print("invalid computation")
    else:
        n = numerator/denominator
        return n

def line(p,q,t):
    # p(t) = p + t(v)
    v = np.sub(q,p)

def IntersectingTriangle(v1,v2,p1,p2,p3):
    r1 = np.subtract(p2,p1)
    r2 = np.subtract(p3,p1)
    v = np.subtract(v2,v1)
    #print(r1)
    A = np.vstack([r1.T,r2.T,-v.T])
    b = np.subtract(v1,v2)
    #print(A)

    if not (np.isclose(np.linalg.det(A),0)):
        x = np.linalg.solve(A, b)
        u1,u2,t = x

        if(u1 + u2 < 1):
            x = v1 - np.multiply(t,v)
            print("1",x[0],x[1],x[2])
        else:
            x = v1 - np.multiply(t, v)
            print("0", x[0], x[1], x[2])
    else:
        print("Invalid Det is 0")






    # num = np.dot(np.subtract(0,v1.ravel()),plane)
    # denom = np.dot(np.subtract(v2.ravel(),v1.ravel()),plane)
    # t = num/denom
    # #print(t)
    # #print(v1.ravel(),"  ",v2.ravel())
    # x = v1 - np.multiply(t,np.subtract(v2,v1))
    #print(x[0]," ",x[1], " ",x[2])
    #print(plane)










def main(lines):
    p = np.array([[lines[0][0]], [lines[0][1]], [lines[0][2]]])
    q = np.array([[lines[0][3]], [lines[0][4]], [lines[0][5]]])
    r = np.array([[lines[0][6]], [lines[0][7]], [lines[0][8]]])
    #print("hello")
    for line in lines[1:]:
        v1 = np.array([[line[0]], [line[1]], [line[2]]])
        v2= np.array([[line[3]], [line[4]], [line[5]]])
        v3 = np.array([[line[6]], [line[7]], [line[8]]])

        IntersectingTriangle(p,q,v1,v2,v3)



lines = parseFile(1)

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
