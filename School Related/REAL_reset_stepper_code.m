  % Prompt the user if they want to adjust the plate

    clear;

    clc;

    a = arduino();

    speed = 100;


    thisStepper = StepperRevA(a, 2048, 'D8', 'D9', 'D10', 'D11');
    answer = input('Would you like to adjust the plate? (yes or no): ', 's');
    
    if strcmpi(answer, 'yes')
        % Prompt the user for the rotation direction
        direction = input('Rotate how many degrees clockwise (positive) or counterclockwise (negative)?: ');
        
        % Calculate the exact number of steps for the specified rotation
        steps = round(direction * 2048 / 360);
        
        % Rotate the plate based on the user's input
        if steps > 0
            MoveClockWise(thisStepper, speed, steps);
        elseif steps < 0
            MoveCounterClockWise(thisStepper, speed, -steps);
        end
    else
        disp('Ok, continuing rotation')
    end
