%{
EGR102HEADERCOMMENT 
Authors:    Todd McKenzie
Assignment: Machine Vision
Changed:   30 November 2022
History: 

Purpose:
To interpret coins in an image.

Notes:
 
%}

clc;

clear;

image=imread('CoinsOnGreen.jpg');

imshow(image)

imtool(image)

 g_channel=image(:,:,2);

 r_channel=image(:,:,1);

 b_channel=image(:,:,3);

 rg_ratio=double(r_channel)./double(g_channel);% red green ratio

 bg_ratio=double(b_channel)./double(g_channel);% blue green ratio

 rg_ratio(isnan(rg_ratio))=0;% if it is nan it sets it to zero

 bg_ratio(isnan(bg_ratio))=0;% this should only happen if it is black

 g_bin=rg_ratio<0.7 ;

 bw = bwareaopen(g_bin,50);

 bw = ~bw;

 stats = regionprops('table',bw,'Centroid', 'ConvexArea', 'MajorAxisLength','MinorAxisLength');

 UsefulTable=stats{:,:};

radii=UsefulTable(:,3)/2;

centers=UsefulTable(:,1:2);

figure

    imshow(image)
    hold on
    viscircles(centers, radii);
    hold off

realCoins=UsefulTable(:,5)>1000 & UsefulTable(:,5)<100000;

CoinTable=UsefulTable(realCoins,:);

histogram(CoinTable(:,3),20);



len = length(CoinTable);

Change = 0;

for i = 1:len

    if CoinTable(i,3) < 71.5
        Change = Change + 0.10;

    elseif CoinTable(i,3) >= 71.5 && CoinTable(i,3) < 80
        Change = Change + 0.01;

    elseif CoinTable(i,3) >= 80 && CoinTable(i,3) < 85
        Change = Change + 0.05;

    else 
        Change = Change + 0.25;

    end
end

fprintf("The value of the coins in the image is %0.2f\n", Change)
       









