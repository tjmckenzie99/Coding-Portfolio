%{
EGR102HEADERCOMMENT - Antenna Calculator
Authors:    Todd McKenzie
Assignment: EGR 102
Changed:    10 September 2022
History:    10 September 2022 
            
Purpose:
  To calculate the wavelength of an electromagnetic signal and to calculate
  the optimum length for an antenna.

Notes:


%}

% Display the HASL logo
disp ('| ((|)) Handmade')
disp ('|___|   Aerial')
disp ('|   |   Solutions')
disp ('|   |   LLC')
% Prompt the user for a frequency with the message "Enter the desired reception frequency in MHz: "
frequency_MHz = input('Enter the desired reception frequency in MHz:');
if frequency_MHz == 0
    error('Invalid number. Please do not use zero or negative numbers.')
end

if frequency_MHz < 0
    error('Invalid number. Please do not use zero or negative numbers.')
end
% Convert frequency from MHz into Hz
frequency_Hz = frequency_MHz * 1e6;
% Calculate the wavelength of the signal
lightSpeed = 300000000;
wavelength = lightSpeed/frequency_Hz;
% Calculate the optimum antenna length
optimumLength_meters = 0.95*(wavelength)/2;
% Convert antenna length from meters into inches
optimumLength_inches = optimumLength_meters*39.3701;
% Display the signal wavelength in meters
fprintf('The signal wavelength in meters is %.2f meters.\n', wavelength)
% Display the antenna length in inches
fprintf('The antenna length in inches is %.2f inches.\n', optimumLength_inches)
% Display the antenna length in meters
fprintf('The antenna length in meters is %.2f meters.\n', optimumLength_meters)


%This code does not work with 0 MHz or negative MHz. If you use a negative
%value the value will be negative. If you use zero you will get an infinite
%value.
