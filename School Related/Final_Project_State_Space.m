clear all
close all

% Intializes variables
 
m1=3000;
m2=12000;
m3=3000;

% m1=3000*0.7;
% m2=12000
% m3=3000*0.8;

k1=13650;
k2=13650;

% c=100;
% c2=100;

c=10;
c2=10;

% State Space Matrices

A1 = [0 0 0 1 0 0; ...
     0 0 0 0 1 0; ...
     0 0 0 0 0 1; ...
     -k1/m1 k1/m1 0 -c/m1 c/m1 0; ...
     k1/m2 (-k1-k2)/m2 k2/m2 c/(m2) (-2*c2)/m2 c/m2; ... 
     0 k2/m3 -k2/m3 0 c/m3 -c/m3];

B1 = [0 0 0; ...
    0 0 0; ...
    0 0 0; ...
    1/m1 0 0; ...
    0 1/m2 0; ...
    0 0 1/m3];

C1 = [1 0 0 0 0 0; ...
    0 1 0 0 0 0; ...
    0 0 1 0 0 0];

D1 = [0 0 0; ...
    0 0 0; ...
    0 0 0];

% Graphs State Spaces Model 
system4 = ss(A1,B1,C1,D1);
t = 0:.01:10;
step(system4,t)

% Impulse Response
figure
impulse(system4 (2,2),t)

% Frequency Response
figure
bode(system4 (2,2))











