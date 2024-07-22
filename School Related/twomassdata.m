clear all
close all

m1 = 1;
m2 = 1.4;
k1 = 18;
k2 = 21;
c = .8;

A1 = [0 1 0 0; ...
    -(k1+k2)/m1 -c/m1 k2/m1 0; ...
     0 0 0 1; ...
     k2/m2 0 -k2/m2 0];
B1 = [0; 0; 0; 1/m2];
C1 = [1 0 0 0; ...
      0 0 1 0];
D1 = [0; 0];

system4 = ss(A1,B1,C1,D1);

t = 0:.05:10;
step(system4,t)

figure
Num = [0 0 k2];
Den = [m1*m2 m1*c+m2*c m1*k2+m2*(k1+k2) k1*c k1*k2];
system5 = tf(Num,Den);
step(system5,t)
figure
impulse(system5,t)
[EVec,Eigv] = eig(A1);
[r,p,K] = residue(Num,Den);
roots(Den)
figure
bode(Num,Den)
