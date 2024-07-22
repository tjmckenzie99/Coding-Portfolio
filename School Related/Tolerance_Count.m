%{
EGR102HEADERCOMMENT - Tolerance Count
Authors:    Todd McKenzie
Assignment: Tolerance Count
Changed:    5 October 2022
History:    5 October 2022
            
Purpose:
  Describe the contents of a MATLAB script in a form that students
  can use as basis for the header comments of their script files.

Notes:

%}

%Basic Variables
nomWeight = 4.13;
tolerance = 0.25;
minWeight = nomWeight - tolerance;
maxWeight = nomWeight + tolerance;

%Reads Week7Weights
weightArray = readmatrix('Week7Weights.xlsx');
numWeights = length(weightArray);

%Displays the first and last values
fprintf('The first weight is %.2f.\n', weightArray(1))

fprintf('The last weight is %.2f.\n', weightArray(240))

%Sets up overweightArray and underweightArray
underweightArray = weightArray < minWeight;
overweightArray = weightArray > maxWeight;

%Sets up numUnderweight and the percentage that is underweight.
numUnderweight = sum(underweightArray);
percentUnderweight = numUnderweight*100/numWeights;

%Sets up numUnderweight and the percentage that is overweight.
numOverweight = sum(overweightArray);
percentOverweight = numOverweight*100/numWeights;

%Displays all values necessary (underweight, overweight, percentage underweight,
% and percentage overweight).
fprintf('Underweight (< %.2f oz) items: %d (%.2f %%)\n',minWeight,numUnderweight,percentUnderweight)
fprintf('Overweight (> %.2f oz) items: %d (%.2f %%)\n',maxWeight,numOverweight,percentOverweight)