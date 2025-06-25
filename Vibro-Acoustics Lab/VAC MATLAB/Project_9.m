clear;
clc;
close all;

% Density 
rho_concrete = 2600;
rho_glass = 2300;
rho_door = 720;
t_gap = 1;

% Thickness
t_concrete = 200*10^(-3);
t_glass = 3*10^(-3);
t_door = 0.05;

% Modified Density Value
modified_rho_concrete = rho_concrete*t_concrete;
modified_rho_glass = rho_glass*t_glass;
modified_rho_door = rho_door*t_door;

% Transmission Loss Arrays
TL_gap_range = [];
TL_concrete_range = [];
TL_glass_range = [];
TL_door_range = [];
TL_avg_range =[];
TL_avg_no_gap_range =[];

% Transmission Coefficient Array
TC_gap_range = [];
TC_concrete_range = [];
TC_glass_range = [];
TC_door_range = [];
TC_avg_range =[];
TC_avg_no_gap_range =[];

% Surface Area Calculation
SA_concrete = 5.75;
SA_glass = 1*1;
SA_door = 2.5*0.9;
SA_gap = 0.9*(10*10^(-3));
SA_door_no_gap = (SA_door + SA_gap);

SA_total = (SA_concrete+SA_glass+SA_door+SA_gap);
SA_total_no_gap = (SA_concrete+SA_glass+SA_door_no_gap);

for f = 100:10000
    
    % Calculate Transmission Loss
    TL_gap = 0;
    TL_concrete = 20*log10(modified_rho_concrete*f) - 42;
    TL_glass = 20*log10(modified_rho_glass*f) - 42;
    TL_door = 20*log10(modified_rho_door*f) - 42;
    
    % Stores in a table
    TL_gap_range = [TL_gap_range, TL_gap];
    TL_concrete_range = [TL_concrete_range, TL_concrete];
    TL_glass_range = [TL_glass_range, TL_glass];
    TL_door_range = [TL_door_range, TL_door];

    % Calculate Transmission Coefficient
    TC_gap = 1;
    TC_concrete = 10^(-TL_concrete/10);
    TC_glass = 10^(-TL_glass/10);
    TC_door = 10^(-TL_door/10);
    
    % Stores in a table
    TC_gap_range = [TC_gap_range, TC_gap];
    TC_concrete_range = [TC_concrete_range, TC_concrete];
    TC_glass_range = [TC_glass_range, TC_glass];
    TC_door_range = [TC_door_range, TC_door];

    % Weighted Transmission Coefficient 
    A = (1/(SA_total));
    TC_avg = A*((SA_gap*TC_gap)+(SA_concrete*TC_concrete) ...
        +(SA_glass*TC_glass)+(SA_door*TC_door));

    TC_avg_range = [TC_avg_range, TC_avg];

    % Weighted Transmission Loss
    TL_avg = 10*log10(1/TC_avg);
    
    TL_avg_range = [TL_avg_range, TL_avg];

    % Weighted Transmission Coefficient With No Gap
    B = (1/SA_total_no_gap);
    TC_avg_no_gap = B*((SA_concrete*TC_concrete) ...
        +(SA_glass*TC_glass)+(SA_door_no_gap*TC_door));
    
    TC_avg_no_gap_range = [TC_avg_no_gap_range, TC_avg_no_gap];

    % Weighted Transmission Loss With No Gap
    TL_avg_no_gap = 10*log10(1/TC_avg_no_gap);

    TL_avg_no_gap_range = [TL_avg_no_gap_range, TL_avg_no_gap];

end

figure;
semilogx(100:10000, TL_avg_range, 'r')
title('Transmission Loss of a Wall With Gap')
xlabel('Frequency')
ylabel('Transmission Loss (dB)')

figure;
semilogx(100:10000, TL_avg_no_gap_range, 'g');
ylim([24,65]);
title('Transmission Loss of a Wall Without Gap');
xlabel('Frequency (Hz)');
ylabel('Transmission Loss (dB)')