clear;

clc;

a= arduino();

stepsPerRevolution = 2048/8;

thisStepper = StepperRevA(a,stepsPerRevolution,'D8', 'D9','D10','D11');

MoveClockWise(thisStepper,100, 2048/16);

MoveCounterClockWise(thisStepper, 100, 2048/8);

disp('program is done');