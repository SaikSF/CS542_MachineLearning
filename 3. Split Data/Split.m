%% Aleksandr Kim
% CS 542 - Machine Learning
% Project: Sleep data processing

% Load in data
load('SleepDataset.mat')

test = 1;
train = 1;
threshold = 0.7;
rng(4242019);

% For loop to split data
for i=1:3923
    
    pick = rand;
    
    if pick < threshold
        
        trainingData(train,:) = dataset(i,:);
        trainingLabel(train,:) = datalabels(i,:);
        train = train + 1;
        
    else
        
        testingData(test,:) = dataset(i,:);
        testingLabel(test,:) = datalabels(i,:);
        test = test + 1;
        
    end
    
    
end
