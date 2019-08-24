# -*- coding: utf-8 -*-

#- Python 3

'''
'''

__author__  = 'Dr.GAO, Siyu'
__version__ = '1.0.0'
__date__    = '2019.08.22'

import os, csv, itertools
import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# temp hardcode
str_path_in = os.path.join(os.getcwd(), '_data', 'RollingSystemFrequency_20190809_tz_converted.csv')
str_path_out = os.path.join(os.getcwd(), '_data', 'RollingSystemFrequency_20190809_upsampled.csv')

df = pd.read_csv(str_path_in, parse_dates=[0], index_col=0)

df = df.resample('0.1S')
df = df.interpolate(method='cubic')

df.to_csv(str_path_out, index=True, float_format='%.3f') #, index_label='Time', header=['Frequency'])

print('Done')

