# -*- coding: utf-8 -*-
"""
@author: steve
"""

#==============================================================================
#
# IMPORT LIBRARIES
#
#==============================================================================
import dill
import pandas as pd

#==============================================================================
#
# LOAD DATAFRAME
#
#==============================================================================
playlist_song_mat_train = dill.load(open("playlist_song_mat_train.pkl", "rb"))

#==============================================================================
#
# RUN INQUIRIES
#
#==============================================================================
# Ask for song or band
print('\n')
song_band_inquiry = input('Name a song or band: ').lower()

# Show options
options = pd.DataFrame([col for col in playlist_song_mat_train.columns if song_band_inquiry in col])[0]
print('\n')
print('Suggestions:')
print(options)

# Obtain user input
while True:
    print('\n')
    options
    try:
        song_band_number = int(input('What number? '))
    except:
        print('\n')
        print('*** Must input an integer. ***')
        continue
    else: 
        if (song_band_number in range(0,len(options))):
            song_band_choice = options[song_band_number]
            break
        else:
            print('\n')
            print('*** Choose a number from the table. ***')
            continue
			
#==============================================================================
#
# RECOMMEND
#
#==============================================================================
print('\n')
print('Top 3 suggested songs: ')
for x_song_band, x_count in \
    playlist_song_mat_train[playlist_song_mat_train[song_band_choice]==1]\
        .sum().sort_values(ascending=False)[1:4,].iteritems():
    print(' * ', x_song_band)
    
print('\n')
print('Top 3 suggested songs (again): ')
results = playlist_song_mat_train[playlist_song_mat_train[song_band_choice]==1].sum().sort_values(ascending=False)[1:4,]
print(results)
