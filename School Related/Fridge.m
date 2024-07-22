%{
EGR102HEADERCOMMENT - Refrigerator Monitor
Authors:    Todd McKenzie
Assignment: Refrigerator Monitor
Changed:    29 September 2022
History:    29 September 2022- Wrote entire code
            
Purpose:
  To monitor a temperature of a refrigerator.

Notes:   
%}

clear;
clc;

a = arduino();
% Temperature to start while loop
TemperatureTherm = 35;

% Sets temperature that while loop ends.
while (TemperatureTherm<40)
    voltage = readVoltage(a, 'A0');
    ThermistorResistance = VoltageToResistance(voltage);
    TemperatureTherm = ResistanceToTempF (ThermistorResistance);
    pause(5);
end

writeDigitalPin(a,'D6',1);

disp('WARNING: TEMPERATURE IS TOO HIGH')
