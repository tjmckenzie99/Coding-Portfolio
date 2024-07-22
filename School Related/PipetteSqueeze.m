%{
    EGR 103 Section 1
    Seth Folczyk
    ASSIGNMENT: Pipette Squeeze code

     Started      Finished
    11/06/2023 - 11/14/2023
%}

% setup to allow the rest of the code to work
s = servo(a, 'D4');

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
