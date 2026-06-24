import fastapi
from fastapi import FastAPI
from pydantic import BaseModel
from ML.predictor import predict_cena

app = FastAPI()

# class for user
class userhaip(BaseModel):
    housing_median_age: float
    total_rooms: int
    total_bedrooms: int
    district: str
    building_type: str
    total_floors: int
    ceiling_height: float
    total_area: float
    metro_distance_km:float
    proximity: str

@app.get("/")
def read_root():
    return {"message":"vse rabotaet"}

@app.post("/predict")
def predict(features: userhaip):
    prediction = predict_cena(features.model_dump())
    return {"prediction": prediction}