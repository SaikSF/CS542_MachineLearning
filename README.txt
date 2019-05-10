Team Neurals - Aleksandr Kim, Avantika Dasgupta, Siddharth Bakshi
Automatic Sleep Stage Classification
CS542: Machine Learning

Our process may be a bit convoluted, mixing both manual and computer methods.
The folders are numbered to help facilitate following our methodology. Unfortunately,
the data files are too large to upload to the github repository.

1. Data Conversion
This folder contains all the necessary files to be able to read in EEG data
in the form of EDF files and convert it to numeric arrays.
	1a. Run the python script in the folder with the unpacked EDF files
	1b. Manually save the numeric arrays labeled "nsrr01", "nsrr02" and "nsrr03"
		into a .mat file titled "RawData.mat"
	1c. Place this file into the 2nd folder

2. Data Processing
This folder contains all the necessary files to process the data. The file generated
in step 1 is placed in this folder and the ProcessSleepData.m file is run in matlab.
The file will normalize the data, split it into epochs, calculate a PSD and wrap
the created arrays to create a transformed data set.
	2a. Place the file generated in step 1 here. 
	2b. Manually import the data file into matlab
	2c. Manually import the 3 csv files into matlab
	2d. Run the matlab script to process data
	2e. Manually save the data labeled "dataset", "datalabels" and "f" into a file "SleepDataset.mat"

3. Split Data
This folder contains all the necessary files to split the data into a training and test set.
	3a. Run the Split.m matlab script
	3b. Save the data labeled "testingData", "testingLabel", "trainingData" and "trainingLabel" into a file
		labeled "SplitSleepDataset.mat"

4. Machine Learning
This folder contains all the necessary files to build and train the machine learning algorithms.
	4a. Copy the "SleepDataset.mat" and "SplitSleepDataset.mat" created in steps 2 and 3 here
	4b. Run the python files to build and train the neural networks.