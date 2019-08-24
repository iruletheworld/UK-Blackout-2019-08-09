# -*- coding: utf-8 -*-

#- Python 3

'''
This project is to plot the events during the blackout in the UK on 2019-08-09.

Data : Rolling System Frequency, Elexon (15 sec resolution)

Upsampling : 15 sec to 0.1 sec

Method : Cubic

Upsampling is just to make the curve smooth and also makes easier to make annotations.

See the "requirements.txt" for the Python dependencies.

Ref : 
https://www.programcreek.com/python/example/61483/matplotlib.dates.DateFormatter
'''

__author__  = 'Dr.GAO, Siyu'
__version__ = '1.0.0'
__date__    = '2019.08.24'

import os, csv, itertools
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
import matplotlib.dates as dates
import matplotlib.dates as mdates
from dateutil import tz

# font property
fp = FontProperties(fname=r'C:\windows\fonts\msyhbd.ttf')

# temp hardcode
str_path_in = os.path.join(os.getcwd(), '_data', 'RollingSystemFrequency_20190809_upsampled.csv')

df = pd.read_csv(str_path_in, parse_dates=[0], index_col=0)

# fig size
int_dpi    = 100
fig_length = 1900 / int_dpi
fig_height = 900 / int_dpi

# start and end points
int_start  = 570000
int_end    = 576000

# points for events
int_lightning_detection  = 571530   # 16:52:33          ;0
int_lightning_fault      = 571535   # 16:52:33.490      ;1
int_hornsea_lost         = 571538   # 16:52:33.835      ;2
int_barford_steam_lost   = 571540   # 16:52:34          ;3
int_freq_response_start  = 571540   # 16:52:34          ;4
int_freq_response_650    = 571640   # 16:52:44          ;5
int_eaton_circuit_dar    = 571730   # 16:52:53          ;6
int_freq_stop1           = 571780   # 16:52:58          ;7
int_freq_response_900    = 571840   # 16:53:04          ;8
int_freq_stop2           = 571980   # 16:53:18          ;9
int_barford_gt1a_lost    = 572110   # 16:53:31          ;10
int_freq_response_all    = 572110   # 16:53:31          ;11
int_freq_lfdd            = 572294   # 16:53:49.398      ;12
int_barford_gt1b_lost    = 572380   # 16:53:58          ;13
int_freq_recover         = 574350   # 16:57:15          ;14
int_dno_reconnect        = 579660   # 17:06             ;15

# event coordinates
list_event_coord  = [
                        (mdates.date2num(df.index[int_lightning_detection]) , df['Frequency'][int_lightning_detection]),
                        (mdates.date2num(df.index[int_lightning_fault])     , df['Frequency'][int_lightning_fault]),
                        (mdates.date2num(df.index[int_hornsea_lost])        , df['Frequency'][int_hornsea_lost]),
                        (mdates.date2num(df.index[int_barford_steam_lost])  , df['Frequency'][int_barford_steam_lost]),
                        (mdates.date2num(df.index[int_freq_response_start]) , df['Frequency'][int_freq_response_start]),
                        (mdates.date2num(df.index[int_freq_response_650])   , df['Frequency'][int_freq_response_650]),
                        (mdates.date2num(df.index[int_eaton_circuit_dar])   , df['Frequency'][int_eaton_circuit_dar]),
                        (mdates.date2num(df.index[int_freq_stop1])          , df['Frequency'][int_freq_stop1]),
                        (mdates.date2num(df.index[int_freq_response_900])   , df['Frequency'][int_freq_response_900]),
                        (mdates.date2num(df.index[int_freq_stop2])          , df['Frequency'][int_freq_stop2]),
                        (mdates.date2num(df.index[int_barford_gt1a_lost])   , df['Frequency'][int_barford_gt1a_lost]),
                        (mdates.date2num(df.index[int_freq_response_all])   , df['Frequency'][int_freq_response_all]),
                        (mdates.date2num(df.index[int_freq_lfdd])           , df['Frequency'][int_freq_lfdd]),
                        (mdates.date2num(df.index[int_barford_gt1b_lost])   , df['Frequency'][int_barford_gt1b_lost]),
                        (mdates.date2num(df.index[int_freq_recover])        , df['Frequency'][int_freq_recover]),
                    ]

# make event info strings
list_event_time = [
                        '[16:52:33]',
                        '[16:52:33.490]',
                        '[16:52:33.835]',
                        '[16:52:34]',
                        '[16:52:34]',
                        '[16:52:44]',
                        '[16:52:53]',
                        '[16:52:58]',
                        '[16:53:04]',
                        '[16:53:18]',
                        '[16:53:31]',
                        '[16:53:31]',
                        '[16:53:49.398]',
                        '[16:53:58]',
                        '[16:57:15]',
                    ]

list_event_text   = [
                        'Lightning strikes at\nEaton Socon - Wymondley circuit',
                        'Lightning fault at\nEaton Socon -\nWymondley circuit',
                        'Hornsea windfarm\nlost 737 MW',
                        'Little Barford\nsteam turbine\nlost 244 MW',
                        'Frequency response\nstarted. Lost of\nMains 500 MW',
                        'Frequency response\ndelivered 650 MW',
                        'Eaton Socon- Wymondley\ncircuit closed on DAR',
                        'Frequency drop\narrested',
                        'Frequency response\ndelivered 900 MW',
                        'Frequency recovered',
                        'Little Barford\nGT1A lost 210 MW',
                        'All frequency\nresponse\nused',
                        'LFDD triggered.\n931 MW demand shedded',
                        'Little Barford GT1B\nlost 187 MW',
                        'Normal frequency restored',
                    ]

list_event_info = [k + '\n' + v for k, v in zip(list_event_time, list_event_text)]

list_event_info = [str(k+1).zfill(2) + '. ' + v for k, v in enumerate(list_event_info)]

# annotation xytext value
list_event_xytext = [
                        (60  , 90),       # Lightning strikes at Eaton Socon - Wymondley circuit
                        (-180, -10),      # Lightning fault at Eaton Socon - Wymondley circuit
                        (60  , 5),        # Hornsea windfarm lost 737 MW
                        (-130, -90),      # Little Barford steam turbine lost 244 MW
                        (70  , -90),      # Frequency response started, Lost of Mains 500 MW
                        (-180, 20),       # Frequency response delivered 650 MW
                        (-200, -10),      # Eaton Socon - Wymondley circuit closed on DAR
                        (-20 , 90),       # Frequency drop arrested at 49.1 Hz
                        (-30 , -100),     # Frequency response delivered 900 MW
                        (30  , 50),       # Frequency recovered to 49.2 Hz
                        (20  , 30),       # Little Barford GT1A lost 210 MW
                        (45  , -25),      # All frequency response used
                        (120 , -13),       # LFDD triggered. 931 MW demand shedded
                        (100 , 40),       # Little Barford GT1B lost 187 MW
                        (20  , -70),      # Normal frequency restored
                    ]

# make fig
fig = plt.figure(figsize=[fig_length, fig_height], dpi=int_dpi)

# get fig axes
ax = plt.gca()

# plot the freq
df.plot(ax=ax, color='red', lw=3, zorder=10)

# normal freq
ax.axhline(50.0, lw=3, color='k', zorder=4)

# normal freq upper limit
ax.axhline(50.5, lw=3, color='b', clip_on=False, zorder=5)

# normal freq lower limit
ax.axhline(49.5, lw=3, color='b', zorder=6)

# annotation background bbox
bkcolor = dict(facecolor='w', edgecolor='none', pad=0.01)

# annotation font size
int_size_an_font = 10

# annotation
for i in range(0, len(list_event_info)):

    # text and arrow
    an = ax.annotate(
                        list_event_info[i],
                        xy=list_event_coord[i],
                        xytext=list_event_xytext[i],
                        textcoords='offset points',
                        arrowprops=dict(width=5, headwidth=12, facecolor='orange', edgecolor='k', lw=1.5, shrink=0.05),
                        fontsize=int_size_an_font,
                        bbox=bkcolor,
                        zorder=100
                    )

    # dot on curve
    ax.scatter(list_event_coord[i][0], list_event_coord[i][1], s=60, facecolor='r', edgecolor='orange', lw=2, zorder=100)

# set axes and legend
dict_font_title = {
                        'fontsize' : 20,
                        'fontweight' : 'bold',
                        'fontname' : 'arial'
                    }

dict_font_label = {
                        'fontsize' : 16,
                        'fontweight' : 'bold',
                        'fontname' : 'arial'
                    }

ax.set_title('System Frequency during the Blackout at 2018-08-09 in the UK', fontdict=dict_font_title, pad=10)

ax.set_ylabel('Frequency (Hz)', labelpad=12, fontdict=dict_font_label)
ax.set_ylim(48.8, 50.5)
ax.set_yticks(np.linspace(48.8, 50.5, (50.5-48.8)/0.1+1))

ax.set_xlabel('Time of 2018-08-09 (BST)', labelpad=12, fontdict=dict_font_label)
ax.set_xlim(df.index[int_start], df.index[int_end])
ax.set_xticks(df.index[int_start:int_end+1:200])
plt.xticks(rotation=45)

ax.tick_params(labelsize=12)
ax.legend(prop={'size':16})

# show time only, mind the timezone
ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M:%S', tz=tz.gettz('Europe/London')))

# grid line
plt.grid(True, ls='--')

# point for signature
int_sign = 574220

coord_sign = (mdates.date2num(df.index[int_sign]) , 48.9)

# signature
str_sign = (
                u'DAR : Delayed Auto Reclose'
                + '\n' + u'LFDD : Low Frequency Demand Disconnection'
                + '\n' + u'Data : Rolling System Frequency, Elexon'
                + '\n' + u'Upsampling : 15 sec to 0.1 sec'
                + '\n' + u'Method : Cubic'
                + '\n' + u'Licence : MIT'
                + '\n' + u'© 高斯羽 博士 (Dr. Gāo, Sīyǔ)'
            )

# sign bbox setting
bksign = dict(facecolor='w', edgecolor='r', boxstyle='round,pad=1')

# sign
ax.annotate(
                str_sign,
                fontproperties=fp,
                xy=coord_sign,
                bbox=bksign, 
                va='bottom',
                fontsize=14,
                fontweight='bold'
            )

plt.tight_layout()

# max fig 
fig_manager = plt.get_current_fig_manager()
fig_manager.window.showMaximized()

# save the fig
plt.savefig('uk_blackout_2019_08_09.png', dpi=300)

# show fig
plt.show()

