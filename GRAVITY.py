# -*- coding: utf-8 -*-
from math import *
r=894.7
N=1.0
G=r*(2*pi*N/60)**2*(1/9.80665)
G=1.118*r*N**2*10**-3
type=1
# r: radiud of wheel
# N: rpm of wheel
# G: GA m/s^2
# v: Liner Speed v=r * w(rad/s)
# rad = rad=deg∗(π/180)

def print_params():
    rS="Radius:r={0:.2f}m".format(r)
    Cy=60/N
    NS="Rotation Speed:\n  N={0:.2f}rpm({1:.2f}sec/cycle)".format(N,Cy)
    v= r * ((N * 360 / 60) * pi /180)
    vkm = v * 60 * 60 / 1000
    LiS="Linear Speed:\n  {0:.2f} m/s({1:.2f} km/h)".format(v,vkm)
    GS="Pseudo Gravity:G={0:.2f}(xg)".format(G)
    print(rS)
    print(NS)
    print(LiS)
    print(GS)
    print("")

print_params()

while type != "0":
    print("Select Parameter by \n [0]uit [1]:r [2]:N \n [3]:G keep r [4]:G keep N")
    type=input("Enter Number [0]-[4] > ")
    if type == "1":
        rI=input("enter Radius of wheels by meter(m) >> ")
        r=float(rI)
        G=r*(2*pi*N/60)**2*(1/9.80665)
        print_params()
    elif type == "2":
        nI=input("enter rotation speeed of wheels by rpm >> ")
        N=float(nI)
        G=r*(2*pi*N/60)**2*(1/9.80665)
        print_params()
    elif type == "3":
        GI=input("enter GA m/s^2 with keep r >> ")
        G=float(GI)
        N=sqrt(G/1.118/r/(10**-3))
        print_params()
    elif type == "4":
        GI=input("enter GA m/s^2 with keep N >> ")
        G=float(GI)
        r=G/((2*pi*N/60)**2*(1/9.80665))
        print_params()

print("Quit")