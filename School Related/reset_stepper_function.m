while true

    % Prompt the user if they want to adjust the plate
    answer = input('Would you like to adjust the plate? (yes or no): ', 's');
    
    if strcmpi(answer, 'yes')
        % Prompt the user for the rotation direction
        direction = input('Rotate how many degrees clockwise (positive) or counterclockwise (negative)?: ');
        
        % Rotate the plate based on the user's input
        MoveClockWise(thisStepper, speed, direction * 2048 / 360);
    else
        disp('Ok, continuing rotation');
        break; % Exit the loop if the user doesn't want to adjust the plate
    end
end