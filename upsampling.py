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

df = df.resample('0.01S')
df = df.interpolate(method='cubic')

df.to_csv(str_path_out, index=True, float_format='%.3f') #, index_label='Time', header=['Frequency'])

print('Done')

# int_dpi    = 100
# fig_length = 1200 / int_dpi
# fig_height = 1000 / int_dpi

# int_start  = 5700000
# int_end    = 5760000



# # only show the time part, no date
# df.index = df.index.time

# fig = plt.figure(figsize=[fig_length, fig_height], dpi=int_dpi)

# ax = plt.gca()


# ax.axhline(50.0, lw=3, color='k')
# ax.axhline(50.5, lw=3, color='b', clip_on=False)
# ax.axhline(49.5, lw=3, color='b')

# df.plot(ax=ax, color='red', lw=3)

# dict_font_title = {
#                         'fontsize' : 18,
#                         'fontweight' : 'bold',
#                         'fontname' : 'arial'
#                     }

# dict_font_label = {
#                         'fontsize' : 16,
#                         'fontweight' : 'bold',
#                         'fontname' : 'arial'
#                     }

# ax.set_title('System Frequency during the Blackout at 2018-08-09 in the UK', fontdict=dict_font_title, pad=10)

# ax.set_ylabel('Frequency (Hz)', labelpad=10, fontdict=dict_font_label)
# ax.set_ylim(48.8, 50.5)
# ax.set_yticks(np.linspace(48.8, 50.5, (50.5-48.8)/0.1+1))

# ax.set_xlabel('Time of 2018-08-09', labelpad=10, fontdict=dict_font_label)
# ax.set_xlim(df.index[int_start], df.index[int_end])
# ax.set_xticks(df.index[int_start:int_end+1:2000])
# plt.xticks(rotation=45)

# ax.tick_params(labelsize=12)
# ax.legend(prop={'size':16})

# # grid line
# plt.grid(True, ls='--')

# plt.tight_layout()

# fig_manager = plt.get_current_fig_manager()
# fig_manager.window.showMaximized()

# # show fig
# plt.show()

