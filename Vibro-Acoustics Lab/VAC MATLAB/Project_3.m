clear;
clc;
close all;
n = 1:6;

% Calculate the coefficients A_n, B_n, and C_n
A_n = (sin(2*pi*n) ./ (n*pi)) - (sin((3*pi*n)/2) ./ (n*pi));
B_n = (cos(2*pi*n) / (n*pi)) - (cos((3*pi*n)/2) ./ (n*pi));
C_n = sqrt(A_n.^2 + B_n.^2);

% Create a new figure
figure;

% Plot A_n, B_n, and C_n using stem plots
stem(n, A_n, 'b', 'DisplayName', 'A_n');
hold on;
stem(n, B_n, 'r', 'DisplayName', 'B_n');
stem(n, C_n, 'g', 'DisplayName', 'C_n');
hold off;

% Add labels, title, and legend
xlabel('n');
ylabel('Coefficient Value');
title('Fourier Coefficients A_n, B_n, and C_n');
legend('Location', 'best');
grid on;