clear all
close all

%Intializes variables
m1 = 1;
m2 = 1.4;
k1 = 18;
k2 = 21;
c = 0.8;

% State Space Matrices
A1 = [0 1 0 0; ...
    -(k1+k2/m1) -c/m1 k2/m1 0; ...
     0 0 0 1; ...
     k2/m2 0 -k2/m2 0];

B1 = [0; 1/m1; 0; 0];

C1 = [1 0 0 0; ...
    0 0 1 0];

D1 = [0; 0;];

% Graphs State Spaces Model 
system4 = ss(A1,B1,C1,D1);

t = 0:.05:10;
step(system4,t)


