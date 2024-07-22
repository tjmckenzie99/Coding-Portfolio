% This code was revised September 24, 2020 by Julie Whitney
% It contains both servo connect commands I know of to test with different
% servos.  This code looks for a servo on pin D9.
 
clear
clc
 
a=arduino();
 
s1 = servo(a, 'D3', 'MinPulseDuration', 700*10^-6, 'MaxPulseDuration', 2300*10^-6);
% If you get an IOServerBlock error when the servo moves, try this instead:
%s1=servo(a,'D10','MinPulseDuration', 1*10^-3, 'MaxPulseDuration', 2e-3);
while 1 ==1
test = input("Enter a number");
% start with Gate down

if test == 1
writePosition(s1, 0);
elseif test == 2
writePosition(s1,0.5);
else
writePosition(s1, 1);
end
if test ==4 
    i =2
else 
    i =1
end
end
%  
%disp('done');
