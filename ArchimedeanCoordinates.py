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

def TruncatedTetrahedron():
    TruncatedTetrahedronSet1 = EvenNegSigns(1,1,3)
    TruncatedTetrahedronCoordinates = ([[0.0, 0.0, 0.0]])
    for i in range(np.shape(TruncatedTetrahedronSet1)[0]):
        TruncatedTetrahedronCoordinates = np.concatenate((TruncatedTetrahedronCoordinates, EvenPerm(TruncatedTetrahedronSet1[i][0], TruncatedTetrahedronSet1[i][1], TruncatedTetrahedronSet1[i][2])))
    TruncatedTetrahedronCoordinates = TruncatedTetrahedronCoordinates[1:,::]
    return TruncatedTetrahedronCoordinates

def Cuboctahedron():
    CuboctahedronSet1 = AllPerms(1,1,0)
    CuboctahedronCoordinates = ([[0.0, 0.0, 0.0]])
    for i in range(np.shape(CuboctahedronSet1)[0]):
        CuboctahedronCoordinates = np.concatenate((CuboctahedronCoordinates, SignChange(CuboctahedronSet1[i][0], CuboctahedronSet1[i][1], CuboctahedronSet1[i][2])))
    CuboctahedronCoordinates = CuboctahedronCoordinates[1:,::]
    return CuboctahedronCoordinates

def TruncatedCube():
    sqrt2 = 2 ** 0.5
    TruncatedCubeSet = AllPerms(1,1, sqrt2 - 1)
    TruncatedCubeCoordinates = ([[0.0, 0.0, 0.0]])
    for i in range(np.shape(TruncatedCubeSet)[0]):
        TruncatedCubeCoordinates = np.concatenate((TruncatedCubeCoordinates, SignChange(TruncatedCubeSet[i][0], TruncatedCubeSet[i][1], TruncatedCubeSet[i][2])))
    TruncatedCubeCoordinates = TruncatedCubeCoordinates[1:,::]
    return TruncatedCubeCoordinates

def TruncatedOctahedron():
    TruncatedOctahedronSet = SignChange(0,1,2)
    TruncatedOctahedronCoordinates = np.array([[0.0, 0.0, 0.0]])
    for i in range(np.shape(TruncatedOctahedronSet)[0]):
        TruncatedOctahedronCoordinates = np.concatenate((TruncatedOctahedronCoordinates, AllPerms(TruncatedOctahedronSet[i][0], TruncatedOctahedronSet[i][1], TruncatedOctahedronSet[i][2])))
    TruncatedOctahedronCoordinates = TruncatedOctahedronCoordinates[1:,::]
    return TruncatedOctahedronCoordinates

def Rhombicuboctahedron():
    sqrt2 = 2 ** 0.5
    RhombicuboctahedronSet = AllPerms(1,1,sqrt2 + 1)
    RhombicuboctahedronCoordinates = ([[0.0, 0.0, 0.0]])
    for i in range(np.shape(RhombicuboctahedronSet)[0]):
        RhombicuboctahedronCoordinates = np.concatenate((RhombicuboctahedronCoordinates, SignChange(RhombicuboctahedronSet[i][0], RhombicuboctahedronSet[i][1], RhombicuboctahedronSet[i][2])))
    RhombicuboctahedronCoordinates = RhombicuboctahedronCoordinates[1:,::]
    return RhombicuboctahedronCoordinates

def TruncatedCuboctahedron():
    sqrt2 = 2 ** 0.5
    TruncatedCuboctahedronSet = SignChange(1,1 + sqrt2,1 + 2 * sqrt2)
    TruncatedCuboctahedronCoordinates = np.array([[0.0, 0.0, 0.0]])
    for i in range(np.shape(TruncatedCuboctahedronSet)[0]):
        TruncatedCuboctahedronCoordinates = np.concatenate((TruncatedCuboctahedronCoordinates, AllPerms(TruncatedCuboctahedronSet[i][0], TruncatedCuboctahedronSet[i][1], TruncatedCuboctahedronSet[i][2])))
    TruncatedCuboctahedronCoordinates = TruncatedCuboctahedronCoordinates[1:,::]
    return TruncatedCuboctahedronCoordinates

def SnubCube():
    snubcubeList1 = EvenPerm(1, 1 / tribonacci, tribonacci)
    snubcubeList2 = OddPerm(1, 1 / tribonacci, tribonacci)
    SnubCubeCoordinates = ([[0.0 ,0.0, 0.0]])
    for i in range(np.shape(snubcubeList1)[0]):
        SnubCubeCoordinates = np.concatenate((SnubCubeCoordinates, EvenNegSigns(snubcubeList1[i][0], snubcubeList1[i][1], snubcubeList1[i][2])))
        SnubCubeCoordinates = np.concatenate((SnubCubeCoordinates, OddNegSigns(snubcubeList2[i][0], snubcubeList2[i][1], snubcubeList2[i][2])))
    SnubCubeCoordinates = SnubCubeCoordinates[1:,::]
    return SnubCubeCoordinates

def Icosidodecahedron():
    IcosidodecahedronList1 = SignChange(0, 0, golden)
    IcosidodecahedronList2 = SignChange(1/2, golden / 2, golden ** 2 / 2)
    IcosidodecahedronCoordinates = ([[0.0, 0.0, 0.0]])
    for i in range(np.shape(IcosidodecahedronList1)[0]):
        IcosidodecahedronCoordinates = np.concatenate((IcosidodecahedronCoordinates, AllPerms(IcosidodecahedronList1[i][0], IcosidodecahedronList1[i][1], IcosidodecahedronList1[i][2])))
    for j in range(np.shape(IcosidodecahedronList2)[0]):
        IcosidodecahedronCoordinates = np.concatenate((IcosidodecahedronCoordinates, EvenPerm(IcosidodecahedronList2[j][0], IcosidodecahedronList2[j][1], IcosidodecahedronList2[j][2])))
    IcosidodecahedronCoordinates = IcosidodecahedronCoordinates[1:,::]
    return IcosidodecahedronCoordinates

def TruncatedDodecahedron():
    tdlist1 = SignChange(0, 1 / golden, 2 + golden)
    tdlist2 = SignChange(1 / golden, golden, 2 * golden)
    tdlist3 = SignChange(golden, 2, golden + 1)
    TruncatedDodecahedronCoordinates = ([[0.0, 0.0, 0.0]])
    for i in range(np.shape(tdlist1)[0]):
        TruncatedDodecahedronCoordinates = np.concatenate((TruncatedDodecahedronCoordinates, EvenPerm(tdlist1[i][0], tdlist1[i][1], tdlist1[i][2])))
    for i in range(np.shape(tdlist2)[0]):
        TruncatedDodecahedronCoordinates = np.concatenate((TruncatedDodecahedronCoordinates, EvenPerm(tdlist2[i][0], tdlist2[i][1], tdlist2[i][2])))
    for i in range(np.shape(tdlist3)[0]):
        TruncatedDodecahedronCoordinates = np.concatenate((TruncatedDodecahedronCoordinates, EvenPerm(tdlist3[i][0], tdlist3[i][1], tdlist3[i][2])))
    TruncatedDodecahedronCoordinates = TruncatedDodecahedronCoordinates[1:,::]
    return TruncatedDodecahedronCoordinates

def TruncatedIcosahedron():
    tilist1 = SignChange(0, 1, 3 * golden)
    tilist2 = SignChange(1, 2 + golden, 2 * golden)
    tilist3 = SignChange(golden, 2, 2 * golden + 1)
    TruncatedIcosahedronCoordinates = ([[0.0, 0.0, 0.0]])
    for i in range(np.shape(tilist1)[0]):
        TruncatedIcosahedronCoordinates = np.concatenate((TruncatedIcosahedronCoordinates, EvenPerm(tilist1[i][0], tilist1[i][1], tilist1[i][2])))
    for i in range(np.shape(tilist2)[0]):
        TruncatedIcosahedronCoordinates = np.concatenate((TruncatedIcosahedronCoordinates, EvenPerm(tilist2[i][0], tilist2[i][1], tilist2[i][2])))
    for i in range(np.shape(tilist3)[0]):
        TruncatedIcosahedronCoordinates = np.concatenate((TruncatedIcosahedronCoordinates, EvenPerm(tilist3[i][0], tilist3[i][1], tilist3[i][2])))
    TruncatedIcosahedronCoordinates = TruncatedIcosahedronCoordinates[1:,::]
    return TruncatedIcosahedronCoordinates

def Rhombicosidodecahedron():
    rlist1 = SignChange(1, 1, golden ** 3)
    rlist2 = SignChange(golden ** 2, golden, 2 * golden)
    rlist3 = SignChange(2 + golden, 0, golden ** 2)
    RhombicosidodechedronCoordinates = ([[0.0, 0.0, 0.0]])
    for i in range(np.shape(rlist1)[0]):
        RhombicosidodechedronCoordinates = np.concatenate((RhombicosidodechedronCoordinates, EvenPerm(rlist1[i][0], rlist1[i][1], rlist1[i][2])))
    for i in range(np.shape(rlist2)[0]):
        RhombicosidodechedronCoordinates = np.concatenate((RhombicosidodechedronCoordinates, EvenPerm(rlist2[i][0], rlist2[i][1], rlist2[i][2])))
    for i in range(np.shape(rlist3)[0]):
        RhombicosidodechedronCoordinates = np.concatenate((RhombicosidodechedronCoordinates, EvenPerm(rlist3[i][0], rlist3[i][1], rlist3[i][2])))
    RhombicosidodechedronCoordinates = RhombicosidodechedronCoordinates[1:,::]
    return RhombicosidodechedronCoordinates

def TruncatedIcosidodechedron():
    tidlist1 = SignChange(1 / golden, 1 / golden, 3 + golden)
    tidlist2 = SignChange(2 / golden, golden, 1 + 2 * golden)
    tidlist3 = SignChange(1 / golden, golden ** 2, 3 * golden - 1)
    tidlist4 = SignChange(2 * golden - 1, 2, 2 + golden)
    tidlist5 = SignChange(golden, 3, 2 * golden)
    TruncatedIcosidodechedronCoordinates = ([[0.0, 0.0, 0.0]])
    for i in range(np.shape(tidlist1)[0]):
        TruncatedIcosidodechedronCoordinates = np.concatenate((TruncatedIcosidodechedronCoordinates, EvenPerm(tidlist1[i][0], tidlist1[i][1], tidlist1[i][2])))
        TruncatedIcosidodechedronCoordinates = np.concatenate((TruncatedIcosidodechedronCoordinates, EvenPerm(tidlist2[i][0], tidlist2[i][1], tidlist2[i][2])))
        TruncatedIcosidodechedronCoordinates = np.concatenate((TruncatedIcosidodechedronCoordinates, EvenPerm(tidlist3[i][0], tidlist3[i][1], tidlist3[i][2])))
        TruncatedIcosidodechedronCoordinates = np.concatenate((TruncatedIcosidodechedronCoordinates, EvenPerm(tidlist4[i][0], tidlist4[i][1], tidlist4[i][2])))
        TruncatedIcosidodechedronCoordinates = np.concatenate((TruncatedIcosidodechedronCoordinates, EvenPerm(tidlist5[i][0], tidlist5[i][1], tidlist5[i][2])))
    TruncatedIcosidodechedronCoordinates = TruncatedIcosidodechedronCoordinates[1:,::]
    return TruncatedIcosidodechedronCoordinates

def SnubDodecahedron():
    alpha = epsilon - 1 / epsilon
    beta = epsilon * golden + golden ** 2 + golden / epsilon
    sdlist1 = EvenPerm(2 * alpha, 2, 2 * beta)
    sdlist2 = EvenPerm(alpha + beta / golden + golden, -1 * alpha * golden + beta + 1 / golden, alpha / golden + beta * golden - 1)
    sdlist3 = EvenPerm(alpha + beta / golden - golden, alpha * golden - beta + 1 / golden, alpha / golden + beta * golden + 1)
    sdlist4 = EvenPerm(-1 * alpha / golden + beta * golden + 1, -1 * alpha + beta / golden - golden, alpha * golden + beta  - 1 / golden)
    sdlist5 = EvenPerm(-1 * alpha / golden + beta * golden - 1, alpha - beta / golden - golden, alpha * golden + beta  + 1 / golden)
    SnubDodecahedronCoordinates = ([[0.0, 0.0, 0.0]])
    for i in range(np.shape(sdlist1)[0]):
        SnubDodecahedronCoordinates = np.concatenate((SnubDodecahedronCoordinates, OddNegSigns(sdlist1[i][0], sdlist1[i][1], sdlist1[i][2])))
        SnubDodecahedronCoordinates = np.concatenate((SnubDodecahedronCoordinates, OddNegSigns(sdlist2[i][0], sdlist2[i][1], sdlist2[i][2])))
        SnubDodecahedronCoordinates = np.concatenate((SnubDodecahedronCoordinates, OddNegSigns(sdlist3[i][0], sdlist3[i][1], sdlist3[i][2])))
        SnubDodecahedronCoordinates = np.concatenate((SnubDodecahedronCoordinates, OddNegSigns(sdlist4[i][0], sdlist4[i][1], sdlist4[i][2])))
        SnubDodecahedronCoordinates = np.concatenate((SnubDodecahedronCoordinates, OddNegSigns(sdlist5[i][0], sdlist5[i][1], sdlist5[i][2])))
    SnubDodecahedronCoordinates = SnubDodecahedronCoordinates[1:,::]
    return SnubDodecahedronCoordinates
