%{
EGR102HEADERCOMMENT - Blink LED Assignment
Authors:    Todd McKenzie
Assignment: EGR 102
Changed:    8 September 2022
History:    8 September 2022 - Code Written
            
Purpose:
  To make a light blink 10 times.

Notes:
  
%}
% Step 1: Connect Arduino
clear;
a=ardino();

% Step 2: Blink the LED 10 times
for i= 1:10                       % Code executed 10 times
    writeDigitalPin(a, 'D9', 1)   % Turn on LED
    pause(0.5);                   % Wait 1/2 second
    writeDigitalPin(a, 'D9', 0)   % Turn off LED
    pause(0.5);                   % Wait for 1/2 second
end                               % Repeat until i > 10

% Step 3: Create 20 steps for incrementing from 0 (OFF) to 1 (ON)
brightness_step = (1-0)/20;

% Step 4: Brighten LED 
for i= 1:20
    writePWMDutyCycle (a, 'D9', i*brightness_step);
    pause(0.1);
end

% Step 5: Dim the LED
for i=1:20
    writePWMDutyCycle(a, 'D9', 1-i*brightness_step);
    pause(0.1);
end

% Last Step: Report to the user that the purpose has ended
disp('Done');





