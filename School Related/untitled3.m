t = 0:0.01:10;
u = 10 + 3 * sin(3 * t) + sin(10 * t);

% Define the transfer function
numerator = [1 10];
denominator = [1 2 10];
sys = tf(numerator, denominator);

% Calculate the steady-state response using the transfer function
yss = lsim(sys, u, t);

% Plot the input and steady-state response
plot(t, u, t, yss);
grid on;
legend('Input', 'y_{ss}');
xlabel('Time (s)');
ylabel('Amplitude');
title('Input and Steady-State Response');