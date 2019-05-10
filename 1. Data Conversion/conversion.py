# Aleksandr Kim
# CS542: Machine Learning
# Code to unpack EDF data

import mne
import matplotlib
import matplotlib.pyplot
import pandas

mne.sys_info() 

# Read in EDF data
raw1 = mne.io.read_raw_edf('learn-nsrr01.edf').load_data()
raw2 = mne.io.read_raw_edf('learn-nsrr02.edf').load_data()
raw3 = mne.io.read_raw_edf('learn-nsrr03.edf').load_data()

# Convert to data frame
df1 = raw1.to_data_frame()
df2 = raw2.to_data_frame()
df3 = raw3.to_data_frame()

# Convert to arrays
nsrr01 = df1.values
nsrr02 = df2.values
nsrr03 = df3.values
