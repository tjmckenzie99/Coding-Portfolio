%% Transmission Loss of Pipe and Resonator %%

clc;
clear;
close all;

% Constants
c = 343;

% Quarter Pipe Constants
A1 = 5*10^(-4);
L = 20*10^(-2);
A_p = 10*10^(-4);

% Helmholtz Constants
A_neck = 5*10^(-4);
L_neck = 3*10^(-2);
V = 270*10^(-6);

% Tables
TL_Pipe_Table = [];
TL_Helmholtz_Table = [];

% Calculate TL Values

for f = 5:0.5:1000

    k = (2*pi*f)/c;
    w = (2*pi*f);
    
    % Transmission Loss Pipe

    term1 = (tan((2*pi*f/c)*L))^2;
    term2 = (4*(A_p/A1)^2);

    TL_Pipe = 10*log10((term1+term2)/(term2));

    TL_Pipe_Table = [TL_Pipe_Table, TL_Pipe];

    % Helmholtz Transmission Loss
   
    term3 = (c/(2*(A_p)));
    term4 = (((w)*(L_neck)/(A_neck))) - (((c^2) / (((w)* V))));
    TL_Helmholtz = 10*log10(1+(term3/term4)^2);
    
    TL_Helmholtz_Table = [TL_Helmholtz_Table, TL_Helmholtz];

end

% Plot the Data

figure
plot(5:0.5:1000, TL_Pipe_Table, 'r', 5:0.5:1000, TL_Helmholtz_Table, 'b', 'LineWidth', 1.5)

title('Transmission Loss Comparison: Quarter Pipe vs Helmholtz Resonator')
xlabel('Frequency (Hz)')
ylabel('Transmission Loss (dB)')

%% Transmission Loss of Expansion Chamber %%

% Constants
A_D1 = ((pi/4)*(5*10^(-2))^2);
A_D2 = ((pi/4)*(20*10^(-2))^2);

m = (A_D2/A_D1);

r = 30*(10^(-2));

% Arrays
TL_Expansion_Array = [];
TL_Expansion_Array_Simplified = [];

for f = 5:1000

    k = (2*pi*f)/c;

    TL_Expansion = 10*log10((1/4)*(((4*cos(k*r))^2)+((m+1/m)^2)*(sin(k*r))^2));

    TL_Expansion_Simplified = 10*log10((1/4)*(m^2)*(sin(k*r))^2);

    TL_Expansion_Array_Simplified = [TL_Expansion_Simplified, TL_Expansion_Array_Simplified];

    TL_Expansion_Array = [TL_Expansion, TL_Expansion_Array];

end

figure
plot(5:1000, TL_Expansion_Array, 'g', 5:1000, TL_Expansion_Array_Simplified, 'y','LineWidth', 1.5)
title('Transmission Loss of Expansion Chamber')
xlabel('Frequency (Hz)')
ylabel('Transmission Loss (dB)')
legend('Full Model', 'Simplified Model')
ylim([0, inf])
 


