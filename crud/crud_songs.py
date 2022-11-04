from joblib import load as joblib_load
import pathlib
import json
import pandas as pd
from schema.schema_songs import Song



def crud_predict(song_features: Song ) -> str:
    #Load the model
    rf_clf = joblib_load(open('Spotify/rf_predictor.pkl','rb'))

    #Load mean and sd of training data for standardization 
    with open(pathlib.Path.joinpath(pathlib.Path(__file__).parent.parent, 'mean_sd.json')) as json_f:
        mean_sd_dict = json.load(json_f)

    #numerical data standadization
    features = [[
        (song_features.danceability - mean_sd_dict['danceability'][0])/mean_sd_dict['danceability'][1],
        (song_features.energy - mean_sd_dict['energy'][0]) / mean_sd_dict['energy'][1],
        (song_features.key - mean_sd_dict['key'][0]) / mean_sd_dict['key'][1],
        (song_features.loudness - mean_sd_dict['loudness'][0]) / mean_sd_dict['loudness'][1],
        (song_features.mode - mean_sd_dict['mode'][0]) / mean_sd_dict['mode'][1],
        (song_features.speechiness - mean_sd_dict['speechiness'][0]) / mean_sd_dict['speechiness'][1],
        (song_features.acousticness - mean_sd_dict['acousticness'][0]) / mean_sd_dict['acousticness'][1],
        (song_features.instrumentalness - mean_sd_dict['instrumentalness'][0]) / mean_sd_dict['instrumentalness'][1],
        (song_features.liveness - mean_sd_dict['liveness'][0]) / mean_sd_dict['liveness'][1],
        (song_features.valence - mean_sd_dict['valence'][0]) / mean_sd_dict['valence'][1],
        (song_features.tempo - mean_sd_dict['tempo'][0]) / mean_sd_dict['tempo'][1],
        (song_features.duration_ms - mean_sd_dict['duration_ms'][0]) / mean_sd_dict['duration_ms'][1],
        (song_features.time_signature - mean_sd_dict['time_signature'][0]) / mean_sd_dict['time_signature'][1],
        (song_features.chorus_hit - mean_sd_dict['chorus_hit'][0]) / mean_sd_dict['chorus_hit'][1]
         ]]

    feat = pd.DataFrame(features, columns=list(mean_sd_dict.keys()))
    

    # Predicting the Class
    predicted_class = rf_clf.predict(feat)
        
    if(predicted_class[0] == 0):
        status = 0 #"Flop"

    elif(predicted_class[0] == 1):
        status = 1 #"Hit"

    return status