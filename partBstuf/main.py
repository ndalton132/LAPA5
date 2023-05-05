import sys
import numpy as np
def parseFile(fileNum):
    with open("C:\\Users\\nickd\\OneDrive\\Pictures\\Screenshots\\School\\LinearAlgebraPA5\\Input_Files\\class_input_"+ str(fileNum) + "-2.txt") as file:
        input = file.readlines()
    array = [[float(num) for num in line.strip().split()] for line in input]
    return array

#print(parseFile(0))






def paralellProjection(x,n):
    I = np.eye(3)
    q = np.array([[0],[0],[0]])
    #print(v,"  \n ",n)
    v = -n
    #print(q,"  ",v)

    try:
        vdotn = np.dot(v.ravel(), n.ravel())
        if vdotn == 0 or np.isnan(vdotn):
            print("Invalid computation: vdotn is zero or NaN")
        else:
            left_side = (np.divide((np.dot(v, n.T)), vdotn))
            denominator = np.dot(v.ravel(), n.ravel())
            if denominator == 0 or np.isnan(denominator):
                print("Invalid computation: denominator is zero or NaN")
            else:
                right_side = ((np.dot(q.ravel(), n.ravel())) / denominator) * v
                xPrime = (np.dot((np.subtract(I, left_side)), x)) + right_side
                print(xPrime.ravel())

    except Exception:
        print("invalid computation")



def main(lines):
    p = np.array([[lines[0][0]], [lines[0][1]], [lines[0][2]]])
    q = np.array([[lines[0][3]], [lines[0][4]], [lines[0][5]]])
    r = np.array([[lines[0][6]], [lines[0][7]], [lines[0][8]]])
    i = 0

    paralellProjection(p,q)
    for line in lines[1:]:
        v1 = np.array([[line[0]], [line[1]], [line[2]]])
        v2= np.array([[line[3]], [line[4]], [line[5]]])
        v3 = np.array([[line[6]], [line[7]], [line[8]]])
        try:
            paralellProjection(v1, q)
            paralellProjection(v2, q)
            paralellProjection(v3, q)

        except Exception:
            print("Invalid computation")

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
