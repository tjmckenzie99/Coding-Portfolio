clear all
close all

% Initializes variables
m1 = 3000;
m2 = 12000;
m3 = 3000;

k1 = 13650;
k2 = 13650;
c = 100;
c2 = 100;

% State Space Matrices
A1 = [0 0 0 1 0 0; ...
      0 0 0 0 1 0; ...
      0 0 0 0 0 1; ...
      -k1/m1 k1/m1 0 -c/m1 c/m1 0; ...
      k1/m2 (-k1-k2)/m2 k2/m2 c/m2 (-2*c2)/m2 c/m2; ...
      0 k2/m3 -k2/m3 0 c/m3 -c/m3];

B1 = [0 0 0; ...
      0 0 0; ...
      0 0 0; ...
      1/m1 0 0; ...
      0 1/m2 0; ...
      0 0 1/m3];

C1 = [1 0 0 0 0 0; ...
      0 1 0 0 0 0; ...
      0 0 1 0 0 0];

D1 = [0 0 0; ...
      0 0 0; ...
      0 0 0];

% Create State Space Model
system4 = ss(A1, B1, C1, D1);

% Calculate the transfer function
sys_tf = tf(system4);

% Frequency range for analysis
w = logspace(-1, 2, 1000); % Adjust the frequency range as needed

% Input signal frequencies
omega_input_range = logspace(-1, 2, 100); % Adjust the range of frequencies as needed

% Initialize arrays to store steady-state responses
steady_state_responses = zeros(size(omega_input_range));

% Determine the steady-state response for each frequency component
for i = 1:length(omega_input_range)
    omega_input = omega_input_range(i);
    [Mag, Phase] = bode(sys_tf, omega_input);
    steady_state_responses(i) = Mag(1) * sin(Phase(1)); % Using the first element of Mag and Phase arrays
end

% Plot steady-state responses
figure;
semilogx(omega_input_range, steady_state_responses, 'LineWidth', 2);
xlabel('Frequency (rad/s)');
ylabel('Steady State Response');
title('Steady State Response vs. Input Frequency');
grid on;