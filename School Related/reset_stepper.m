clear;
clc;

% Create an Arduino object
a = arduino();

% Define motor parameters
speed = 1600;
steps_per_revolution = 2048;
pin1 = 'D8';
pin2 = 'D9';
pin3 = 'D10';
pin4 = 'D11';

% Create a Stepper motor object
thisStepper = StepperRevA(a, steps_per_revolution, pin1, pin2, pin3, pin4);

% Reset the stepper motor to 0 degrees (straight up and down)
reset_stepper_function(thisStepper, speed, 0);

disp('Program is done');

