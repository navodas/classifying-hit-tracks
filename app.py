from fastapi import FastAPI
import uvicorn
from routes.route_songs import song_route

 
# Initialize an instance of FastAPI
app = FastAPI()

#Add routes
app.include_router(song_route, prefix="/songs",tags=["Song"])

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)