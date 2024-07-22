

clc;

clear;

a = arduino();

s1 = servo(a, 'D11', 'MinPulseDuration', 700*10^-6, 'MaxPulseDuration', 2300*10^-6);

i = 1;

while i==1
    disp("Put Sensor on Material")
    input('and Press Enter to Start')

    disp("Turn Light On")
    pause(1)

    writeDigitalPin(a, 'D5', 1)
    pause(1)

%     disp("Read Voltage")
%     pause(1)
%     readVoltage(a,'A0')
%     pause(0.1)

    Voltage = readVoltage(a,'A0')

    writeDigitalPin(a,'D5', 0)
    disp("Turn Light Off")
    pause(1)

           
    if Voltage > 0.5 && Voltage <= 1.3
        disp("Computer Mouse")
        writePosition(s1, 1);

    elseif Voltage > 1.3 && Voltage <= 2
        disp("Phone Case")
        writePosition(s1, 0.5)

    else
        disp("Hand")
        writePosition(s1, 0)
    end
    pause(1)

    Ask = input("Do you want to test another material? Yes or No", 's');
    if strcmp(Ask, 'Yes')
        i = 1;
    else
        i = 2;
    end
end

disp("Thank you for using sensor")



    

 

     