from pydantic import BaseModel

class Song(BaseModel):
    danceability: float
    energy: float
    key: float
    loudness: float
    mode: float
    speechiness: float
    acousticness:float
    instrumentalness: float
    liveness: float
    valence: float
    tempo: float
    duration_ms: float
    time_signature: float
    chorus_hit: float

    