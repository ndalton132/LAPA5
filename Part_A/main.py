import sys
import numpy as np
import sys
import numpy as np
def parseFile(fileNum):
    with open("C:\\Users\\nickd\\OneDrive\\Pictures\\Screenshots\\School\\LinearAlgebraPA5\\Input_Files\\class_input_"+ str(fileNum) + "-2.txt") as file:
        input = file.readlines()
    array = [[float(num) for num in line.strip().split()] for line in input]
    return array

#print(parseFile(0))

def paralellProjection(q,n,v,x):

    # x = np.array([3,2,4])
    # v = np.array([0,0,1])
    # n = np.array([1,1,1])
    # q = np.array([1,0,0])

    vdotn = np.dot(v, n)
    if vdotn == 0 or np.isnan(vdotn):
        print("Invalid computation: vdotn is zero or NaN")
    else:
        xPrime = x + np.dot(np.divide(np.dot(np.subtract(q,x),n),vdotn),v)
        return xPrime






def main(lines):
    p = np.array([lines[0][0], lines[0][1], lines[0][2]])
    q = np.array([lines[0][3], lines[0][4], lines[0][5]])
    r = np.array([lines[0][6], lines[0][7], lines[0][8]])

    for line in lines[1:]:
        v1 = np.array([line[0], line[1], line[2]])
        v2= np.array([line[3], line[4], line[5]])
        v3 = np.array([line[6], line[7],line[8]])

        print(paralellProjection(p,q,r,v1)," ",paralellProjection(p,q,r,v2)," ",paralellProjection(p,q,r,v3))



lines = parseFile(2)

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



