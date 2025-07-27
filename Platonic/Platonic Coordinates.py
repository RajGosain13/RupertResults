import numpy as np

golden = (1 + 5 ** 0.5) / 2
sqrt33 = 33 ** 0.5
a = 19 - 3 * sqrt33
b = 19 + 3 * sqrt33
c = 1 + a ** (1/3) + b ** (1/3)
tribonacci = c / 3

d = golden - 5 / 27
e = 0.5 * (d ** 0.5)
f = golden / 2 + e
g = golden / 2 - e
epsilon = f ** (1 / 3) + g ** (1 / 3)


def SignChange(num1, num2, num3):
    if num1 == 0 and num2 == 0:
        return np.array([[num1, num2, num3], [num1, num2, -num3]])
    elif num1 == 0:
        return np.array([[num1, num2, num3], [num1, -num2, num3], [num1, num2, -num3], [num1, -num2, -num3]])
    elif num2 == 0:
        return np.array([[num1, num2, num3], [-num1, num2, num3], [num1, num2, -num3], [-num1, num2, -num3]])
    elif num3 == 0:
        return np.array([[num1, num2, num3], [-num1, num2, num3], [num1, -num2, num3], [-num1, -num2, num3]])
    else:
        return np.array([[num1, num2, num3], [-num1, num2, num3], [num1, -num2, num3], [num1, num2, -num3], [num1, -num2, -num3], [-num1, num2, -num3], [-num1, -num2, num3], [-num1, -num2, -num3]])
    
def EvenNegSigns(num1, num2, num3):
    return np.array([[num1, num2, num3], [-num1, -num2, num3], [-num1, num2, -num3], [num1, -num2, -num3]])

def OddNegSigns(num1, num2, num3):
    return np.array([[-num1, num2, num3], [num1, -num2, num3], [num1, num2, -num3], [-num1, -num2, -num3]])

def AllPerms(num1, num2, num3):
    if num1 == num2:
        return np.array([[num1, num2, num3], [num1, num3, num2], [num3, num1, num2]])
    else:
        return np.array([[num1, num2, num3], [num1, num3, num2], [num2, num1, num3], [num2, num3, num1], [num3, num1, num2], [num3, num2, num1]])

def EvenPerm(num1, num2, num3):
    return np.array([[num1, num2, num3], [num2, num3, num1], [num3, num1, num2]])

def OddPerm(num1, num2, num3):
    return np.array([[num1, num3, num2], [num2, num1, num3], [num3, num2, num1]])

def Tetrahedron():
    TetrahedronCoordinates = EvenNegSigns(1,1,1)
    return TetrahedronCoordinates

def Cube():
    CubeCoordinates = SignChange(1,1,1)
    return CubeCoordinates

def Octahedron():
    listOctahedron1 = SignChange(0,0,1)
    listOctahedron2 = ([[0.0, 0.0, 0.0]])
    for i in range(np.shape(listOctahedron1)[0]):
        listOctahedron2 = np.concatenate((listOctahedron2, AllPerms(listOctahedron1[i][0], listOctahedron1[i][1], listOctahedron1[i][2])))
    OctahedronCoordinates = listOctahedron2[1:,::]
    return OctahedronCoordinates

def Dodecahedron():
    DodecahedronSet1 = SignChange(1,1,1)
    DodecahedronSet2 = SignChange(0, 1 / golden, golden)
    DodecahedronCoordinates = ([[0.0, 0.0, 0.0]])
    for i in range(np.shape(DodecahedronSet2)[0]):
        DodecahedronCoordinates = np.concatenate((DodecahedronCoordinates, EvenPerm(DodecahedronSet2[i][0], DodecahedronSet2[i][1], DodecahedronSet2[i][2])))
    DodecahedronCoordinates = np.concatenate((DodecahedronCoordinates[1:,::], DodecahedronSet1))
    return DodecahedronCoordinates

def Icosahedron():
    IcosahedronSignSet = SignChange(0,golden,1)
    IcosahedronCoordinates = ([[0.0, 0.0, 0.0]])
    for i in range(np.shape(IcosahedronSignSet)[0]):
        IcosahedronCoordinates = np.concatenate((IcosahedronCoordinates, EvenPerm(IcosahedronSignSet[i][0], IcosahedronSignSet[i][1], IcosahedronSignSet[i][2])))
    IcosahedronCoordinates = IcosahedronCoordinates[1:,::]
    return IcosahedronCoordinates