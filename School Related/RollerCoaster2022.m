%{
This code is to form the basis for the Week 9 Roller Coaster Assignment. 
%}

clear
clc

a=arduino();


s1 = servo(a, 'D9', 'MinPulseDuration', 700*10^-6, 'MaxPulseDuration', 2300*10^-6);



totalNumRiders = 0; 
GatePositionKnob.Value = 'Gate Up';
writePosition(s1, 0.5);

while totalNumRiders < 5

    sensor = readVoltage(a, 'A0'); 

if sensor < 3.0
    GatePositionKnob.Value = 'Gate Down';
    writePosition(s1, 1)
    totalNumRiders = totalNumRiders + 1;
    TotalRidersLabel.Text = num2str(totalNumRiders);
    pause(2);

else 
    GatePositionKnob.Value = 'Gate Up';
    writePosition(s1, 0.5)
    pause(2);
  
end %end of the while loop
end

GatePositionKnob.Value = 'Gate Locked';
writePosition(s1,0);
pause(1);


