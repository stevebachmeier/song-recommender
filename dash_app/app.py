# -*- coding: utf-8 -*-
"""
Song recommender app

@author: Steve Bachmeier
"""

#==============================================================================
#
# IMPORT LIBRARIES
#
#==============================================================================

import dash
import dash_core_components as dcc 
import dash_html_components as html
import dill

#==============================================================================
#
# LOAD DATA
#
#==============================================================================

playlist_song_mat_train = dill.load(open("playlist_song_mat_train_sample25.pkl", "rb")) 

#==============================================================================
#
# APP DESIGN
#
#==============================================================================

# ---- INITIALIZE DASH ----
app = dash.Dash(__name__)
server = app.server

# ---- LAYOUT ----
app.layout = html.Div(
    children=[
        # ---- HEADING ----
        html.H1(
            'Song Recommender',
            style={'color':'white', 'textAlign':'center'}
        ),
        
        # ---- SONG/BAND DROPDOWN ----
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='options_dropdown',
                    options=[{'label':i, 'value':i} for i in 
                        playlist_song_mat_train.columns],
                    placeholder="Choose a song (search by song or band)"
                )],
                style={'width': '70%', 'display': 'inline-block'}
            ),
            html.Div(
                id='selection_reminder',
                style={'color':'white', 'margin':'1em 0 0 0'}
            )
        ],
    
        style={
            'width':'100%', 
            'display':'float', 
            'textAlign':'center'}
        ), # close song/band dropdown
        
        # ---- LIST SUGGESTIONS ----
        html.Div([
            dcc.Markdown(
                id='suggestions_output'
            )
        ], 
        style={'color':'white', 'margin':'1em 0 0 1em'}) # close list suggestions

    ], # close parent children
    # ---- LAYOUT STYLE ----
    style={
        'backgroundColor':'gray', 
        'width':'100%', 
        'height':'100vh', 
        'position':'absolute'}
) # close parent div

#==============================================================================
#
# INTERACTIONS
#
#==============================================================================

# ---- DROPDOWN SELECTION ----
@app.callback(
    dash.dependencies.Output('selection_reminder', 'children'),
    [dash.dependencies.Input('options_dropdown', 'value')])
def update_output(selection):
    return 'You have selected "{}"'.format(selection)

# ---- LIST RECOMMENDATIONS ----
@app.callback(
    dash.dependencies.Output('suggestions_output', 'children'),
    [dash.dependencies.Input('options_dropdown', 'value')])
def suggestions(selection):
    dff = playlist_song_mat_train[playlist_song_mat_train[selection]==1].sum().sort_values(ascending=False)[1:4,].index.tolist()
    return '## The top three song recommendations are: \n * {} \n * {} \n * {}'.format(dff[0], dff[1], dff[2])
             
#==============================================================================
#
# RUN SERVER
#
#==============================================================================                 
if __name__ == '__main__':
    app.run_server(debug=True)