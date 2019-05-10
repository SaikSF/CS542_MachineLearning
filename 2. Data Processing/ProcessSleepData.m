%% Aleksandr Kim
% CS 542 - Machine Learning
% Project: Sleep data processing

% Load in data
load('RawData.mat')

% Initialize variables
sampleHz = 250; % Hz
epoch = 30; %sec

% Set PSD parameters
window = hamming(250);
overlap = 125;

% Compile data into single matrix, removing unnecessary columns
compiled = [nsrr01; nsrr02; nsrr03];
compiled = compiled(:,[3:8 14]);

% Z-score normalization of the data
normalized = zscore(compiled,[ ], 1);

% Create empty array for the final data set
dataset = NaN([3923 903]);

% Loop through data to calculate the PSD's for each segment
for i=1:size(compiled,1)/sampleHz/epoch
    data = normalized(sampleHz * epoch * (i - 1) + 1:sampleHz * epoch * i ,:);

    % Calculate single sided PSD
    [pxx, f] = pwelch(data, window, overlap, [], sampleHz, 'onesided');
    
    % Sort data into single row
    row = pxx(:)';

    % Append to data set
    dataset(i,:) = row;
end

datalabels = table2array([learnnsrr01profusionannotations; learnnsrr02profusionannotations; learnnsrr03profusionannotations]);