% Sets initial values
m1 = 48.279;
m2 = 0.02198;
e = 1;
vo = 0;
a = 9.81;
d1 = input('Please enter the distance the arm is placed from the pivot in feet');
d2 = input('Please enter the distance the weights are placed from the pivot in feet');

% Does math to determine the velocity of the system 
unit1 = d1/(3.281);
v1 = sqrt(2*a*(unit1));
v2 = 2.99466;
v3 = 4.0547544;

v_tot = v1 + v2 + v3;
va = (v_tot)/3;

% Dynamic Calculations (L1 + sum(F)dt = L2)
p1 = (m2/m1);
vb_2 = (2*va)/(1+(p1));

disp(vb_2)

% Impact force calculation
% F = (m2*vb_2)/(2*t);



