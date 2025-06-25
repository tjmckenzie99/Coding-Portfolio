clear;
clc;
close all;

% Load the narrowband SPL data from an Excel file
filename = 'Mavic_Pro_SPL.xlsx';
data = readtable(filename, 'Sheet', 'narrow band', 'VariableNamingRule', 'preserve');

% Extract frequency (Hz) and SPL (dB) values
freq = data{2:end, 1}; 
spl  = data{2:end, 2};  % Raw (unweighted) SPL values

% Define A-weighting function
A_weight = @(f) 2.00 + 20*log10( (12194^2 .* f.^4) ./ ...
    ( (f.^2+20.6^2) .* (f.^2+12194^2) .* sqrt((f.^2+107.7^2).*(f.^2+737.9^2)) ) );

% Apply A-weighting to the narrowband SPL values
A_corr = A_weight(freq);
spl_A = spl + A_corr; 

% 1/3-octave band center frequencies
third_octave_centers = [63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000];
third_octave_spl = zeros(size(third_octave_centers));

% Calculate 1/3-octave band A-weighted SPL
for i = 1:length(third_octave_centers)
    f_low = third_octave_centers(i) * 2^(-1/6);
    f_high = third_octave_centers(i) * 2^(1/6);
    
    band_indices = (freq >= f_low) & (freq < f_high);
    
    if any(band_indices)
        energy = sum(10.^(spl_A(band_indices)/10));
        third_octave_spl(i) = 10 * log10(energy);
    else
        third_octave_spl(i) = NaN;
    end
end

% Define octave band center frequencies
octave_centers = [63, 125, 250, 500, 1000, 2000];
octave_spl = zeros(size(octave_centers));

% Calculate octave band A-weighted SPL
for i = 1:length(octave_centers)
    f_low = octave_centers(i) / sqrt(2);
    f_high = octave_centers(i) * sqrt(2);
    
    band_indices = (freq >= f_low) & (freq < f_high);
    
    if any(band_indices)
        energy = sum(10.^(spl_A(band_indices)/10));
        octave_spl(i) = 10 * log10(energy);
    else
        octave_spl(i) = NaN;
    end
end

% Compute overall A-weighted SPL
overall_energy = sum(10.^(spl_A / 10));
overall_spl = 10 * log10(overall_energy);

% Plot the Result
figure;

% Define x-axis ticks
xTicks = [63, 125, 250, 500, 1000, 2000];

% Subplot 1: Narrowband (Raw) and Bands
subplot(2,1,1);
semilogx(freq, spl, 'b.-', 'LineWidth', 1);
hold on;
semilogx(third_octave_centers, third_octave_spl, 'ro-', 'LineWidth', 2, 'MarkerSize', 8);
semilogx(octave_centers, octave_spl, 'gs-', 'LineWidth', 2, 'MarkerSize', 8);
xlabel('Frequency (Hz)');
ylabel('SPL (dB)');
title('Narrowband (Unweighted) & Bands (A-weighted)');
legend('Narrowband (raw)', '1/3-Octave (A-weighted)', 'Octave (A-weighted)', 'Location', 'best');
xlim([50 2000]);
set(gca, 'XTick', xTicks, 'XTickLabel', arrayfun(@num2str, xTicks, 'UniformOutput', false));
grid on;
hold off;

% Subplot 2: A-Weighted SPL
subplot(2,1,2);
semilogx(freq, spl_A, 'm.-', 'LineWidth', 1);
hold on;
semilogx(third_octave_centers, third_octave_spl, 'ro-', 'LineWidth', 2, 'MarkerSize', 8);
semilogx(octave_centers, octave_spl, 'gs-', 'LineWidth', 2, 'MarkerSize', 8);
xlabel('Frequency (Hz)');
ylabel('A-weighted SPL (dB)');
title('A-weighted SPL: Narrowband & Bands');
legend('Narrowband (A-weighted)', '1/3-Octave (A-weighted)', 'Octave (A-weighted)', 'Location', 'best');
xlim([50 2000]);
set(gca, 'XTick', xTicks, 'XTickLabel', arrayfun(@num2str, xTicks, 'UniformOutput', false));
grid on;
hold off;

% Display overall SPL
fprintf('Overall A-weighted SPL: %.2f dB\n', overall_spl);