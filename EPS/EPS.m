V_Volts = 15; %25, 30, 15
I_Amperes = 12; %10, 8, 12
t_seconds = 7200; %3600, 1800, 7200

function avail_power = P(V_Volts, I_Amperes)
    
    if V_Volts > 28
        V_Volts = 28;
    end

    if I_Amperes > 10
        I_Amperes = 10;
    end

    P = V_Volts * I_Amperes;
    avail_power = P;
end

function energy_avail = E(avail_power, t_seconds)
    E = avail_power * t_seconds;
    energy_avail = E;
end

disp(['Voltage: ' num2str(V_Volts) 'V, Amperage: ' num2str(I_Amperes) ...
    'A, Time Running: ' num2str(t_seconds) ' seconds'])

avail_power = P(V_Volts, I_Amperes);
disp(['The systems power is ' num2str(avail_power) 'W'])

energy_avail = E(avail_power, t_seconds);
disp(['The systems available energy is ' num2str(energy_avail) 'J'])