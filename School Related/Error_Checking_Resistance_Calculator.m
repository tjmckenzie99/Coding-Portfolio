%{
EGR102HEADERCOMMENT - Error Checking Resistance Calculator
Authors:    Todd McKenzie
Assignment: EGR 102-000 Week 2 
Changed:    31 August 2022
History:    31 August 2022 - Wrote entire code
            17 September 2022 - Editted code to take into account errors
        
Purpose:
  To make  

Notes:
N/A 

%}

%Create variables for the Arduino source voltage (5V), LED forward voltage
% (1.85V), and the LED maximum current (30 milliamps).
Vsource = 5;
Vled = 1.85;
Imax= 30; 

%Input the value of the first resistor.
Resistor1 = input("Please enter resistance 1:"); 

%If the value is negative:
while (Resistor1 <= 0)
disp('Resistance must be positive');
Resistor1 = input("Please enter resistance 1:"); 
end

%Input the value of the second resistor.

%Calculate the effective resistance using the
% same formula as you used in the Parallel resistor calculator.
R_Eff = Resistor1;

%Calculate the current in amperes, based on the two voltages and the 
% effective (total) resistance.  The formula is: Current = (Vsource - Vled)
% / Reff, where Vsource and Vled are the two voltages from step 1, and Reff 
% is the resistance calculated in step 6.

Current = (Vsource-Vled)/R_Eff;

%Convert the current to milliamps by multiplying by 1000.
miliamps = Current*1000;

if miliamps < Imax
Resistance = ['Parallel resistance is:', num2str(R_Eff)];
disp(Resistance);
end

fprintf('The current is %.2f.\n', miliamps)

