% Citations: Deepseek AI assisted in portions of ths code. The portions are
% labelled and assistance is called out.

clear;
clc;
close all;

% Loads the pressure data from Excel File
filename = 'Compressor_Data_2025.xlsx';
data = readtable('Compressor_Data_2025.xlsx', 'Sheet', 'Point Data', 'VariableNamingRule','preserve');
P_ref = 20*10^(-6);
r = 0.5;
N_total = 2048;
M_total = 12;
M_total2 = 5;

% 1/3 Octave Band Centers
standard_centers = [50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, ...
                    630, 800, 1000 1250, 1600, 2000, 2500];

% Retrieves Frequency Range
freq = data{4:end, 10};

% Reads Top 1 Pressure Data and Calculates Sound Power Level
P_top1 = data{4:end, 11};
spl_T1 = 10.*log10(P_top1.^2./P_ref.^2);
spw_T1 = spl_T1+10.*log10((2.*pi.*(r).^2)/M_total);

% Reads Top 2 Pressure Data and Calculates Sound Power Level
P_top2 = data{4:end, 14};
spl_T2 = 10.*log10(P_top2.^2./P_ref.^2);
spw_T2 = spl_T2+10.*log10((2.*pi.*(r).^2)/M_total);

% Reads Top 3 Pressure Data and Calculates Sound Power Level
P_top3 = data{4:end, 17};
spl_T3 = 10.*log10(P_top3.^2./P_ref.^2);
spw_T3 = spl_T3+10.*log10((2.*pi.*(r).^2)/M_total);

% Reads Top 4 Pressure Data and Calculates Sound Power Level
P_top4 = data{4:end, 20};
spl_T4 = 10.*log10(P_top4.^2./P_ref.^2);
spw_T4 = spl_T4+10.*log10((2.*pi.*(r).^2)/M_total);

% Reads Front 1 Pressure Data and Calculates Sound Power Level
P_front1 = data{4:end, 24};
spl_F1 = 10.*log10(P_front1.^2./P_ref.^2);
spw_F1 = spl_F1+10.*log10((2.*pi.*(r).^2)/M_total);

% Reads Front 2 Pressure Data and Calculates Sound Power Level
P_front2 = data{4:end, 27};
spl_F2 = 10.*log10(P_front2.^2./P_ref.^2);
spw_F2 = spl_F2+10.*log10((2.*pi.*(r).^2/M_total));

% Reads Right 1 Pressure Data and Calculates Sound Power Level
P_right1 = data{4:end, 31};
spl_R1 = 10.*log10(P_right1.^2./P_ref.^2);
spw_R1 = spl_R1+10.*log10((2.*pi.*(r).^2)/M_total);

% Reads Right 2 Pressure Data and Calculates Sound Power Level
P_right2 = data{4:end, 34};
spl_R2 = 10.*log10(P_right2.^2./P_ref.^2);
spw_R2 = spl_R2+10.*log10((2.*pi.*(r).^2)/M_total);

% Reads Back 1 Pressure Data and Calculates Sound Power Level
P_back1 = data{4:end, 38};
spl_B1 = 10.*log10(P_back1.^2./P_ref.^2);
spw_B1 = spl_B1+10.*log10((2.*pi.*(r).^2)/M_total);

% Reads Back 2 Pressure Data and Calculates Sound Power Level
P_back2 = data{4:end, 41};
spl_B2 = 10.*log10(P_back2.^2./P_ref.^2);
spw_B2 = spl_B2+10.*log10((2.*pi.*(r).^2)/M_total);

% Reads Left 1 Pressure Data and Calculates Sound Power Level
P_left1 = data{4:end, 45};
spl_L1 = 10.*log10(P_left1.^2./P_ref.^2);
spw_L1 = spl_L1+10.*log10((2.*pi.*(r).^2)/M_total);

% Reads Left 1 Pressure Data and Calculates Sound Power Level
P_left2 = data{4:end, 48};
spl_L2 = 10.*log10(P_left2.^2./P_ref.^2);
spw_L2 = spl_L2+10.*log10((2.*pi.*(r).^2)/M_total);

% Total Sound Power Level Calculation
spw_total_L = 10.^(spw_B1/10) + 10.^(spw_B2/10) + ...
                    10.^(spw_T1/10) + 10.^(spw_T2/10) + ...
                    10.^(spw_T3/10) + 10.^(spw_T4/10) + ...
                    10.^(spw_F1/10) + 10.^(spw_F2/10) + ...
                    10.^(spw_L1/10) + 10.^(spw_L2/10) + ...
                    10.^(spw_R1/10) + 10.^(spw_R2/10);

spw_total = 10*log10(spw_total_L);

% Retrieve Sound Intensity Data
data2 = readtable('Compressor_Data_2025.xlsx', 'Sheet', 'Scan Data', 'VariableNamingRule','preserve');
W_ref = 10^(-12);

% Area Calculations
A_Top = 1 * 1;     
A_Front = 1 * 0.5; 
A_Right = 1 * 0.5; 
A_Back = 1 * 0.5;  
A_Left = 1 * 0.5; 

% Calculate sound power
W_Top = data2{4:end, 11} .* A_Top;      
W_Front = data2{4:end, 14} .* A_Front;
W_Right = data2{4:end, 17} .* A_Right;
W_Back = data2{4:end, 20} .* A_Back;
W_Left = data2{4:end, 23} .* A_Left;

% Total sound power 
W_Total = W_Top + W_Front + W_Right + W_Back + W_Left;

% Calculate sound power level
spw_total_I = 10.*log10(W_Total./W_ref);

% Graph the results
figure;
plot(freq, spw_total)
title("Sound Power Level vs. Frequency")
xlabel('Frequency (Hz)');
ylabel('Sound Power Level (dB)');
ylim([40 80]);

figure;
plot(freq, spw_total_I)
title("Sound Power Level vs. Frequency")
xlabel('Frequency (Hz)');
ylabel('Sound Power Level (dB)');
xlim([50 4000])
ylim([40 80]);

figure;
plot(freq, spw_total, 'b');
hold on;
plot(freq, spw_total_I, 'r');
hold off;
title("Sound Power Level vs. Frequency");
xlabel('Frequency (Hz)');
ylabel('Sound Power Level (dB)');
xlim([50 4000]);
ylim([40 80]);


% ---- Deepseek AI (https://www.deepseek.com/) Assisted in the modification and fine turning of this portion if the code. ----
valid_centers = standard_centers(standard_centers >= min(freq) & standard_centers <= max(freq));

% Initialize storage arrays
octave_bands_point = zeros(size(valid_centers));
octave_bands_scan = zeros(size(valid_centers));

% Process each band
for i = 1:length(valid_centers)
    fc = valid_centers(i);
    fl = fc/(2^(1/6));  
    fu = fc*(2^(1/6));  
    
    % Find indices in current band
    band_mask = (freq >= fl) & (freq <= fu);
    
    % Process point data
    if any(band_mask)
        octave_bands_point(i) = 10*log10(sum(10.^(spw_total(band_mask)/10)));
    else
        octave_bands_point(i) = NaN;
    end
    
    % Process scan data 
    if any(band_mask)
        octave_bands_scan(i) = 10*log10(sum(10.^(spw_total_I(band_mask)/10)));
    else
        octave_bands_scan(i) = NaN;
    end
end

% Plot 1/3 octave results with logarithmic x-axis
figure;
semilogx(valid_centers, octave_bands_point, 'r-o', 'LineWidth', 1.5); % Log x-axis
hold on;
semilogx(valid_centers, octave_bands_scan, 'b-s', 'LineWidth', 1.5);
title('1/3 Octave Band Sound Power Levels');
xlabel('Center Frequency (Hz)');
ylabel('Sound Power Level (dB)');
set(gca, 'XTick', valid_centers, 'XScale', 'log'); % Explicitly set log scale and ticks
xticklabels(arrayfun(@num2str, valid_centers, 'UniformOutput', false)); 
xtickangle(45); % Improve label readability
legend('Point Data', 'Scan Data', 'Location', 'best');
grid on;
xlim([50 2500]);
ylim([65 95]);

% --- End of Citation ---


% Sound Pressure Level at 5m 
r2 = 5;
spl_5m = spw_total_I - 10.*log10(2.*pi.*(r2).^2);


% --- Copied from the portion above Deepseek AI assisted with. ---

% Plot SPL at 5 meters
octave_bands_spl_5m = zeros(size(valid_centers));

for i = 1:length(valid_centers)
    fc = valid_centers(i);
    fl = fc/(2^(1/6)); 
    fu = fc*(2^(1/6));  
    
    % Find indices in the current 1/3-octave band
    band_mask = (freq >= fl) & (freq <= fu);
    
    % Compute the total SPL in this band (in linear units, then convert to dB)
    if any(band_mask)
        octave_bands_spl_5m(i) = 10*log10(sum(10.^(spl_5m(band_mask)/10)));
    else
        octave_bands_spl_5m(i) = NaN;
    end
end

% Plot the 1/3 Octave Band SPL at 5 meters
figure;
semilogx(valid_centers, octave_bands_spl_5m, 'b-o', 'LineWidth', 1.5);
title('1/3 Octave Band SPL at 5m');
xlabel('Center Frequency (Hz)');
ylabel('SPL (dB)');
set(gca, 'XTick', valid_centers, 'XScale', 'log');  
xticklabels(arrayfun(@num2str, valid_centers, 'UniformOutput', false));
xtickangle(45);
grid on;
xlim([50 2500]);   
ylim([40 70]);     

% --- End of Citation ---


% Other Calculations
interval = 0.002;
f_size = 2;
block_size = f_size/interval;
fprintf('The block size is %.2f\n', block_size)
min_f = 1/f_size;
fprintf('The minimum frequency is %.2f Hz\n', min_f)
f_res = 1/f_size;
fprintf('The frequency resolution is %.2f Hz\n', f_res)
n_lines = (block_size/2);
fprintf('The number of lines is %.2f lines\n', n_lines)
s_freq = 1/interval;
n_freq = s_freq/2;
fprintf('The nyquist frequency is %.2f Hz\n', n_freq)
