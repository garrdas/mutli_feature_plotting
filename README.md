# Mutliple Feature Plotting Tool
This code generates simple plots with a line for each feature passed to it.

The code looks in a directory for .txt files (unless other extension specified) and converts the headers in each file to lower case. After converting headers to lower case it will spit out a new .csv file with those new headers. It also lower cases the feature list passed. It then checks that the all of the features match up with headers in the data file. If they do, it will generate plots of the features over the lenght of the data file. 

The user should not pass more than 20 features because it will break the code and will generate difficult to read plots anyway. 

This is set up for time series data, it expects a 'date' column and a 'time' column in the first two columns of the data file. It will concat these two columns and use them as the x-axis or independent variable on the plot.

## Inputs
1. path to directory containing data files
2. list of features (or column headers) you want to plot
3. data file extension (default .txt)

#### I will update this periodically... maybe