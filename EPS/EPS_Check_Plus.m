EPS_matrix  = [0, 7,  300;...
               30, 12,  60; 
               28, 10, 200; 
               10, 10,  10 ]; 
             %(voltage, amperage, duration)

%             [0, 7,  300;...
%              30, 10,  60; 
%              28, 10, 200; 
%              10, 10,  10 ]; 

%             [22, 7,  300;...
%              40, 7,  60; 
%              25, 10, 200; 
%              10, 8,  600 ]
disp("-------START-------")
function x = P(EPS_matrix)
    sum = 0;
    time_sum = 0;
    [rows, cols] = size(EPS_matrix);
    for i = 1:rows
        disp(['#### INPUT ' num2str(i) ' ####'])
        for j = 1:cols
            if j == 1
                disp(['Voltage: ' num2str(EPS_matrix(i,j)) 'V'])
            end

            if j == 2
                disp(['Amperage: ' num2str(EPS_matrix(i,j)) 'A'])
            end

            if j == 3
                disp(['Time: ' num2str(EPS_matrix(i,j)) ' seconds'])
            end
        end
        
        if EPS_matrix(i, 1) == 0 %CHECKS IF NO VOLTAGE DETECTED
            disp('*ERROR: NO VOLTAGE DETECTED!')
        end
       
        if EPS_matrix(i, 1) > 28 %CHECKS VOLTAGE
            diff = EPS_matrix(i, 1) - 28;
            disp(['*ERROR: Input matrix ' num2str(i) ' Voltage error!'])
            disp(['      Voltage input is ' num2str(EPS_matrix(i, 1)) '.'])
            disp(['      Voltage is ' num2str(diff) 'V above threshold.'])
            disp('      Changing Voltage to 28V.')
            fprintf('\n')
            EPS_matrix(i, 1) = 28;
        end

        if EPS_matrix(i, 2) > 10 %CHECKS AMPERAGE
            diff = EPS_matrix(i, 2) - 10;
            disp(['*ERROR: Input matrix ' num2str(i) ' Amperage error!'])
            disp(['      Amperage input is ' num2str(EPS_matrix(i, 1)) '.'])
            disp(['      Amperage is ' num2str(diff) 'A above threshold.'])
            disp('      Changing Voltage to 10A.')
            fprintf('\n')
            EPS_matrix(i, 2) = 10;
        end

        Power = EPS_matrix(i, 1) * EPS_matrix(i, 2); %POWER CALCULATION
        E = Power * EPS_matrix(i, 3); %ENERGY STORAGE CALCULATION
        disp(['The energy output is of matrix ' num2str(i) ' is ' num2str(E) 'J.'])
        fprintf('\n')
        sum = sum + E;
        time_sum = time_sum + EPS_matrix(i, 3);
        disp('--------------------------')
    end
    fprintf('\n')
    disp(['The overall time elapsed is ' num2str(time_sum) ' seconds.'])
    x = sum; 
end

x = P(EPS_matrix);

disp(['The overall energy output of the ' num2str(size(EPS_matrix, 1)) ...
    ' inputs is ' num2str(x) 'J.'])
fprintf('\n')
disp("-------END-------")