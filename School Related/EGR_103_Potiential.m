clear all;
clc;

a = arduino();

speed = 1600;

thisStepper = StepperRevA(a, 2048, 'D8', 'D12', 'D10', 'D11');

s = servo(a, 'D9');

% starts at the correct angle to prevent any errors
angle = 0.6;
writePosition(s, angle);

% configurable pause to allow for raising/ lowering of pipette / start of
% squeeze
pause(1);
angle = 0.25;
writePosition(s, angle);

% another configurable pause to release the squeeze arm allowing for the
% sample to be drawn
pause(2)
angle = 0.6;
writePosition(s, angle);


% Rotate the plate 90 degrees
MoveClockWise(thisStepper, speed, 2048/4);

% Pause (To insert whatever code in necessary for subsections)
pause(5);  

s = servo(a, 'D9');

% starts at the correct angle to prevent any errors
angle = 0.6;
writePosition(s, angle);

% configurable pause to allow for raising/ lowering of pipette / start of
% squeeze
pause(1);
angle = 0.25;
writePosition(s, angle);

% another configurable pause to release the squeeze arm allowing for the
% sample to be drawn
pause(2)
angle = 0.6;
writePosition(s, angle);


% Rotate the plate back to the original position
MoveCounterClockWise(thisStepper, speed, 2048/4);

s = servo(a, 'D9');

% starts at the correct angle to prevent any errors
angle = 0.6;
writePosition(s, angle);

% configurable pause to allow for raising/ lowering of pipette / start of
% squeeze
pause(1);
angle = 0.25;
writePosition(s, angle);

% another configurable pause to release the squeeze arm allowing for the
% sample to be drawn
pause(2)
angle = 0.6;
writePosition(s, angle);


% Rotate the plate 180 degrees
MoveClockWise(thisStepper, speed, 2048/2);

% Pause (To insert whatever code in necessary for subsections)
pause(5);  

s = servo(a, 'D9');

% starts at the correct angle to prevent any errors
angle = 0.6;
writePosition(s, angle);

% configurable pause to allow for raising/ lowering of pipette / start of
% squeeze
pause(1);
angle = 0.25;
writePosition(s, angle);

% another configurable pause to release the squeeze arm allowing for the
% sample to be drawn
pause(2)
angle = 0.6;
writePosition(s, angle);


% Rotate the plate back to the original position
MoveCounterClockWise(thisStepper, speed, 2048/2);

s = servo(a, 'D9');

% starts at the correct angle to prevent any errors
angle = 0.6;
writePosition(s, angle);

% configurable pause to allow for raising/ lowering of pipette / start of
% squeeze
pause(1);
angle = 0.25;
writePosition(s, angle);

% another configurable pause to release the squeeze arm allowing for the
% sample to be drawn
pause(2)
angle = 0.6;
writePosition(s, angle);


% Rotate the plate 270 degrees
MoveClockWise(thisStepper, speed, 3 * (2048/4));

% Pause (To insert whatever code in necessary for subsections)
pause(5);  

s = servo(a, 'D9');

% starts at the correct angle to prevent any errors
angle = 0.6;
writePosition(s, angle);

% configurable pause to allow for raising/ lowering of pipette / start of
% squeeze
pause(1);
angle = 0;
writePosition(s, angle);

% another configurable pause to release the squeeze arm allowing for the
% sample to be drawn
pause(2)
angle = 0.6;
writePosition(s, angle);


% Rotate the plate back to the original position
MoveCounterClockWise(thisStepper, speed, 3 * (2048/4));

s = servo(a, 'D9');

% starts at the correct angle to prevent any errors
angle = 0.6;
writePosition(s, angle);

% configurable pause to allow for raising/ lowering of pipette / start of
% squeeze
pause(1);
angle = 0.25;
writePosition(s, angle);

% another configurable pause to release the squeeze arm allowing for the
% sample to be drawn
pause(2)
angle = 0.6;
writePosition(s, angle);


disp('Program is done');
