omega = 0:.01:10;
Z = (j.*omega + 2)./(-omega.^2 + .05*j.*omega + 6);
plot(omega,abs(Z))
xlabel('Omega')
ylabel('Magnitude (Z)')
figure
plot(omega,angle(Z))
xlabel('Omega')
ylabel('Phase (Z)')
