# IR_project_wpi
This is the code and related data of the final project for the wpi information retrieval class
for the dataset, I create my owns.

# Rest of your script
There are four files in the folder. 
The recommend py is the main file which I use to search the related items based on the input of geolocation and device.

First input the item's category. That is the first factor.

Second, for geolocation, I use the geopy to get the latitude and longitute of a location and then compute the similarity between 
the geolocation and the sample data.

Third, for device, since it is difficult to get the price data, so simply just showing if the device is iphone 15 or iphone 15 pro,
then the price is high. We can just choose the highest value in the selling price (use max( )to get the maximum). Otherwise, we 
return the least value of the column.

To decide we should let the geolocation data or the device price be the second factor, simply choosing the value of 0.4. If value>0.4, choose Selling Price. Otherwise, choose geolocation.

The rest of files are related to build the webpage.

The dataset: https://drive.google.com/file/d/1moBpPmp836gzYVTUWsC32cHCre5itG70/view?usp=sharing
