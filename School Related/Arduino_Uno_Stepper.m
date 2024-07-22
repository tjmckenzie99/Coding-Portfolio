clc;
clear;
clear s

s = serialport('COM6', 9600);
pause(2)

x = 1
y = 1

% While Loop 

while (x <= 4)

    if (x == 1)
    
        steps_for_1 = 2048/4;
        steps_for_2 = -2048;

        pause(10)

            if (y == 1)

            steps_for_1 = -2048/4;
            steps_for_2 = 2048;

            x = (x + 1);
            y = (y + 1);

            end
    
    elseif (x == 2)
    
        steps_for_1 = 2048/2;
        steps_for_2 = -2048/2; 

        pause(10);

            if (y == 2)

            steps_for_1 = -2048/2;
            steps_for_2 = 2048;

            x = (x + 1);
            y = (y + 1);

            end

    elseif (x == 3)
    
        steps_for_1 = (3 * (2048/4));
        steps_for_2 = (-2048);

        pause(10)

        if (y == 3)

            steps_for_1 = -(3 * (2048/4));
            steps_for_2 = (2048);

            x = (x + 1);
            y = (y + 1);

        end
    
    end
end

   

Multiple_Stepper_String = append("1,", int2str(steps_for_1),",","2,",int2str(steps_for_2));

write(s, Multiple_Stepper_String, 'string');


