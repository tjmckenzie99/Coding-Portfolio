function [rTherm] = VoltageToResistance(vDivider)
rTherm = (5-vDivider)/(vDivider/10000)
end

