clear;

clc;

ClassData = readmatrix("MiniProjectData.xlsx");
Materials(1:5) = "Phone Case";
Materials(6:10) = "Eraser";
Materials(11:15) = "Computer Mouse";
RGB_Levels = ClassData(:,2:4);
x = fitctree(RGB_Levels, Materials);
view(x,"Mode","Graph");