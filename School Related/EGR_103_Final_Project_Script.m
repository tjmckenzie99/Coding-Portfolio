clear;
clc;

a = arduino();

stepsPerRevolution = 2048;

speed = 1600;

thisStepper = StepperRevA(a, stepsPerRevolution, 'D8', 'D9', 'D10', 'D11');

% Rotate the plate 90 degrees
MoveClockWise(thisStepper, speed, stepsPerRevolution/4);

% Pause for a moment to simulate a delay
pause(1);  % You can adjust the pause duration as needed

% Rotate the plate back to the original position
MoveCounterClockWise(thisStepper, speed, stepsPerRevolution/2);

disp('Program is done');