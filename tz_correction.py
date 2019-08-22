# -*- coding: utf-8 -*-

# Python 3

'''
'''

__author__  = 'Dr.GAO, Siyu'
__version__ = '1.0.0'
__date__    = '2019.08.22'

import os, csv, itertools
import pandas as pd
import gsyMain3

# temp hardcode
str_path_data_in  = os.path.join(os.getcwd(), '_data', 'RollingSystemFrequency_20190819_1757.csv')
str_path_temp     = os.path.join(os.getcwd(), '_data', 'RollingSystemFrequency_20190809_temp.csv')
str_path_out      = os.path.join(os.getcwd(), '_data', 'RollingSystemFrequency_20190809_tz_converted.csv')

list_temp_data    = []

with open(str_path_data_in, 'r') as fin:

    list_temp_data = list(fin)

# delete the first line and the last line in the data
list_temp_data = list(itertools.islice(list_temp_data, 1, len(list_temp_data)-1))

with open(str_path_temp, 'w', newline='') as fout:

    for i in list_temp_data:

        fout.write(i)

# use pandas to convert timezone
# https://stackoverflow.com/questions/18911241/how-to-read-datetime-with-timezone-in-pandas
# do not read the header, since it is wrong
# only use the 2nd and 3rd cols since the 1st col is useless
# read the 2nd col as timestamp
# use the 2nd col as index for later timezone conversion
df = pd.read_csv(str_path_temp, header=None, usecols=[1, 2], parse_dates=[1], index_col=0)

# the index col is timestamp with no timezone, therefore firstly would need to localize it to GMT
# and then converted to London
df.index = df.index.tz_localize('GMT').tz_convert('Europe/London')

# output the converted data, note that need to round the floats
df.to_csv(str_path_out, index=True, float_format='%.3f', index_label='Time', header=['Frequency'])

# delete the temp data
gsyMain3.deleteFile(str_path_temp)

print('Done')