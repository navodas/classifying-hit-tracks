### predicting hit or flop tracks using Spotify's audio features

#### Introduction


In this project we analyze the audio features of tracks fetched using Spotify's Web API for each decade from 1970s to 2010s with the intention of training a ML classifer for predicting a given song could be a potential **hit** or a **flop**. This is a [Kaggle dataset](https://www.kaggle.com/code/albertangkasa/spotify-bop-or-flop/data) provided by @ALBERT ANGKASA. 

We developed a Random Forest classifier for this classification task which achived a **0.788 accuracy** and a **0.75 of precision**.

#### Data description

For each track below features are collected, 'track', 'artist', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature', 'chorus_hit', 'sections', 'target', 'decade'. More information about each of these features can be found at https://www.kaggle.com/code/albertangkasa/spotify-bop-or-flop/data.

A binary target variable is defined for each track as 'hit' or a 'flop'. A track is considered as a hit (1), if it has featured in the weekly list (issued by Billboards) of Hot-100 tracks in that decade at least once. Whereas, a track is identified as a flop (0) if it satisfies the below criteria.

            - The track must not appear in the 'hit' list of that decade.
			- The track's artist must not appear in the 'hit' list of that decade.
			- The track must belong to a genre that could be considered non-mainstream and / or avant-garde. 
			- The track's genre must not have a song in the 'hit' list.
			- The genre list for the particular decades are as follows:
			- The track must have 'US' as one of its markets.

Apart from the above features we also updated the dataset with the respective decade that each of the tracks belong to.


#### Steps

##### EDA and Model training 

Below tasks are carried out in the Jupyter notebook **File - ML_classifier_for_hits_prediction.ipynb**.
1. The dowwnloaded csv datasets are integrated to a single file and each track is updated with the feature **decade**.
2. Carried out the below EDA tasks to understand the data better. We vizualized how each of the above mentioned features have changed,
     - over the decades, and
     - across hits and flops.
3. Identified feature importance using mutual information which quantifies the association between the independednt variables and the target variables.
4. To identify and remove multicollinarity, correlation is computed between the numerical variables.
5. Then we standardized the data followed by training the below classifiers using cross validation 
    - Decision Tree 
    - Random Forest
    - Gradient Boosting
6. Selected Random Forest algorithm for hyper parameter tunning using grid search.
7. The final model is trained with best hyper-parameter values and saved for deployment (due to the large size of the model the gzip version is included to github rf_predictor.pkl.gz). 

##### Model deployment using fastapi
1. Developed a REST api using fastapi for deploying the ML model (refer **app.py**).
2. **ML_api.ipynb** showcases how the api can be used for obtaining the predictions.