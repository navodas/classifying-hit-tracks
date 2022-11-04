from fastapi import APIRouter

from crud.crud_songs import crud_predict
from schema.schema_songs import Song

song_route = APIRouter()

# Defining path operation for root endpoint
@song_route.get('/')
def get_test():
    return {'message': 'Connected to ML api...'}
 
# Creating an Endpoint to receive the data to make prediction on.
@song_route.post('/predict',)
def predict(song: Song):
    prediction = crud_predict(song)
    return prediction

@song_route.put("/{id}")
def update(id):
    pass
