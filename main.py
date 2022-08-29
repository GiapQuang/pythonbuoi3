'''from collections import namedtuple
diem=namedtuple("Point","x y")
if __name__ =='__main__':
    A=diem(3,4)
    B=diem(5,6)
    print(A)
    print(B.x,B.y)'''
#Khoang cach tu diem A den B
'''import math
from collections import namedtuple
diem=namedtuple("Point", "x y")
def kc(A,B): return math.sqrt((A.x-B.x)**2+(A.y-B.y)**2)
def dt(A,B): return A.x*B.y-A.y*B.x
if __name__ == '__main__':
    x,y=map(float,input("A: ").split())
    A=diem(x,y)
    x, y = map(float, input("B: ").split())
    B = diem(x, y)
    x, y = map(float, input("C: ").split())
    C = diem(x, y)
    print("S1= ",abs(dt(A,B)+dt(B,C)+dt(A,C))/2)
    a,b,c=kc(B,C),kc(C,A),kc(A,B)
    p=(a+b+c)/2
    print("S2= ", math.sqrt(p*(p-a)*(p-b)*(p-c)))'''
# Dien tich tu giac
'''from collections import namedtuple
diem = namedtuple("Diem", "x, y")
def dt(A, B): return A.x * B.y - A.y * B.x
if __name__ == '__main__':
    D=[]
    for i in range(4):
        x, y = map(float, input("A" + str(i+1) + ": ").split())
        D.append(diem(x, y))
    D.append(D[0])
    s = 0
    for A, B in zip(D, D[1: ]): s += dt(A,B)
    print("Dien tich tu giac %.6f: "%(abs(s)/2))'''

# Tim diem trong tam giac
'''import math'''
'''from collections import namedtuple
diem = namedtuple('D', "x, y")
def dt(A, B):
    return A.x * B.y - A.y * B.x

def S(A, B, C): return abs(dt(A, B) + dt(B, C) + dt(C, A))/ 2
def bkpc(A, B): return (A.x - B.x) ** 2 + (A.y - B.y) ** 2
def tim(A,B,M): # Tim diem tren A B gan M nhat
    while abs(A.x - B.x) > 0.000001 or abs(A.y - B.y) > 0.000001:
        C = diem((A.x + B.x)/2, (A.y + B.y)/ 2)
        if bkpc(A,M) > bkpc(B, M): A = C
        else: B = C
    return A, bkpc(A, M)
if __name__ == '__main__':
    x, y = map(float, input().split())
    A = diem(x, y)
    x, y = map(float, input().split())
    B = diem(x, y)
    x, y = map(float, input().split())
    C = diem(x, y)
    x, y = map(float, input().split())
    M = diem(x, y)
    if S(A, B, C) == S(A, B, M) + S(A, C, M) + S(B, C, M): print("%.3f %.3f"%(M.x, M.y))
    else:
        A1,u = tim(B, C, M)
        B1,v = tim(C, A, M)
        C1,t = tim(A, B, M)
        z = min(u,v,t)
        E = A1 if z == u else (B1 if z == v else C1)
        print("%.3f %.3f" % (E.x, E.y))'''

'''#Cau truc sinh vien hom ho ten, tuoi, diem
#Nhap va xuat
#Sap xep danh sach theo diem giam dan
#Sap xep ds ten tang dan
#In ra sv co diem cao nhat'''

from collections import namedtuple
'''sv = namedtuple('SV', "ten tuoi diem")
def nhap():
    S = []
    for i in range(int(input())):
        a,b,c = input().rsplit(None, 2)
        S.append(sv(a, int(b), float(c)))
    return S
def xuat(S):
    for s in S: print("% -20s %5d %6.2f"%(s.ten, s.tuoi, s.diem))
if __name__ == '__main__':
    S = nhap()
    print("Danh sach sinh vien vua nhap")
    xuat(S)
    print("Danh sach diem giam dan")
    S.sort(key = lambda x : x.diem, reverse=True)
    xuat(S)'''

sv = namedtuple('SV', "ten tuoi diem")
def nhap(fname):
    f = open(fname, "r")
    S = []
    for i in range(int(f.readline())):
        a,b,c = f.readline().rsplit(None, 2)
        S.append(sv(a, int(b), float(c)))
        f.close()
    return S
def xuat(S):
    for s in S: print("% -20s %5d %6.2f"%(s.ten, s.tuoi, s.diem))
if __name__ == '__main__':
    S = nhap("sv.txt")
    print("Danh sach sinh vien vua nhap")
    xuat(S)
    print("Danh sach diem giam dan")
    S.sort(key = lambda x : x.diem, reverse=True)
    xuat(S)