clc;

clear;

disp('//----------------------\\')
disp('||  METRIC FLASH CARDS  ||')
disp('\\----------------------//')

    %Pull data from metricPrefixes.xlsx 
    
    metricTable = readtable('metricPrefixes.xlsx');

    %Create a string array of names from the prefix column
    
    prefixNames = string(metricTable.prefix);

    %Create a string array of abbreviations from the abbreviation column
    
    prefixAbbreviations = string(metricTable.abbreviation);

    %Create a string array of exponents from the exponent column
    
    prefixExponents = double(metricTable.exponent);

    %Store prefix name, abbreviation, and exponent from the rowNumber-th row as variables
    
    arrayLength = length(prefixExponents);
    reviewLength = input('How many flashcards would you like to review?');
    rowNumber = zeros;
    numCorrectAbbrev = 0;
    numCorrectExponent = 0;
    
    for index = 1:reviewLength
    rowNumber(index) = randi(arrayLength);
    Name = prefixNames(rowNumber(index));
    correctAbbrev = prefixAbbreviations(rowNumber(index));
    Exponent = prefixExponents(rowNumber(index));

    % Report the prefix name and assign it to the output variable prefixName
    
    fprintf('The prefix is: %s.\n ', Name)
   
    %Compare abbrevGuess and report back if correct or incorrect     
    % If the guess is incorrect, display the correct answer.
    abbrevGuess = input('What is the abbreviation?', 's');

    if abbrevGuess == correctAbbrev
        disp ("Congratulations")
        numCorrectAbbrev = numCorrectAbbrev + 1;
    else
        disp("Your answer is incorrect, the correct guess was:" + correctAbbrev);
        
    end

    %Compare exponentGuess and report back if correct or incorrect     
    % If the guess is incorrect, display the correct answer.
    
    exponentGuess = input('What is the exponent?');

    if exponentGuess == Exponent
        disp("Congratulations")
        numCorrectExponent = numCorrectExponent + 1;
    else
        disp("Your answer is incorrect, the correct guess was:" + Exponent)
    end
    end

    abbrevpercentageVal = 100*(numCorrectAbbrev/reviewLength);
    exponentpercentageVal = 100*( numCorrectExponent/reviewLength);

    if reviewLength > 0
        
    disp ('//-------------------------------------------\\')
    disp ('||             SESSION REVIEW                ||')
    disp ('||-------------------------------------------||')
    fprintf('|| Number of Prefixes Reviewed:  %d           ||\n', reviewLength)
    fprintf('|| Correct Abbreviations:        %d  (%5.1f%%) ||\n', numCorrectAbbrev, abbrevpercentageVal)
    fprintf('|| Correct Exponents:            %d  (%5.1f%%) ||\n', numCorrectExponent,  exponentpercentageVal)
    disp ('||-------------------------------------------||')
    disp ('|| REVIEWED PREFIXES                         ||')
    disp ('||-------------------------------------------||')
    
    for index = 1:reviewLength
        fprintf('||   %-5s %s 10^%3d                          ||\n', prefixNames(rowNumber(index)), prefixAbbreviations(rowNumber(index)), prefixExponents(rowNumber(index)))

    end

     disp('\\-------------------------------------------//')
     disp('Thank you for using Metric Flash Cards!')
    

    else 
        disp('No prefixes reviewed')
        disp('Thank you for using Metric Flash Cards!')
    
    end



