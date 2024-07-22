clear all
close all

% States s is a time transfer function.
s = tf('s') 

%Intializes variables
m1 = 1;
m2 = 1.4;
k1 = 18;
k2 = 21;
c = 0.8;

t = 0:.05:10;

% Transfer Functions
A1 = (m2*s^2+k2)/(m1*m2*s^4+c*s^3+(k1+k2)*m2*s^2+m1*k2*s^2++c*k2*s+k1*k2)

B1 = (k2)/(m1*m2*s^4+c*s^3+(k1+k2)*m2*s^2+m1*k2*s^2+c*k2*s+k1*k2)

% Creates Graphs
figure
step(A1,10)
figure
step(B1,10)
