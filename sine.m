clc
clear all
t=0:0.01:10
F1=4
F2=2
x1=sin(2*pi*F1*t)
x2=sin(2*pi*F2*t)
c=x1+x2
plot(c)
