% This is for coding for water sampler.

clear all

clc

image = imread('WaterAndOilAndText7.jpg');
% Brings in image and name it "original".

imshow(image);
% Lets you see image.

BlueWater = imread('BlueWaterA.jpg');
figure
imshow(BlueWater)
% Lets you see BlueWater image.

Test1 = imcrop(BlueWater);
figure
imshow(Test1);
% Crops the image

imshow(BlueWater);
% RegionofInterest = round(getPosition(imrect));

rect = [317 311 374 216];
Test2 = imcrop(BlueWater, rect);
figure
imshow(Test2);
% Sets up rectangle

imtool(image);

g_channel = (image(:,:,2));
r_channel = (image(:,:,1));
b_channel = (image(:,:,3));
% Seperates color planes

rb_ratio = double(r_channel)./double(b_channel); %red blue ratio
bg_ratio =  double(b_channel)./double(g_channel); %blue green ratio
rb_ratio(isnan(rb_ratio))= 0;
bg_ratio(isnan(bg_ratio))= 0; % In case of division by zero. 
% Ratio set up

water_bin = (rb_ratio<=0.7 & bg_ratio >= 1.2 & r_channel<=35);
blackAndWhite=bwareaopen(water_bin, 200);
imshow(blackAndWhite);

waterMask = blackAndWhite >= 100;
waterMask = imfill(blackAndWhite,'holes');
green_overlay= imoverlay(image, waterMask, [0,1,0]);
imshow(green_overlay)



















