from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime
import joblib
import pandas as pd
app = FastAPI(
    title="FlightOnTime DS Model Service",
    description="Microservicio de predicción de retrasos de vuelos",
    version="1.0.0"
)

class PredictionRequest(BaseModel):
    aerolinea: str = Field(..., example="AZ")
    destino: str = Field(..., example="GRU")
    origen: str = Field(..., example="GIG")
    fechaPartida: datetime = Field(..., example="2025-11-10T14:30:00")
    distancia: int = Field(..., gt=0, example=350)
    temp_mean: float = Field(..., example=25.0)
    precipitation: float = Field(..., example=0.0)
    wind_speed: float = Field(..., example=10.0)

class PredictionResponse(BaseModel):
    prevision: str
    probabilidad: float
    
    
    
with open ("MVP_entrenamiento.pkl", "rb") as f:
    model = joblib.load(f)
    
    
"""
@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    #preparar los datos de entrada para el modelo
    df_input = pd.DataFrame([{
        "hour": request.fechaPartida.hour,
        "distance": request.distanciaKm,
        "marketing_airline_network": request.aerolinea,
        "temp_mean":25.0, # Valor ficticio
        "precipitation":0.0, # Valor ficticio
        "wind_speed":10 # Valor ficticio
    }])
    # Realizar la predicción utilizando el modelo cargado
    pred = model.predict_proba(df_input)[0]
    proba = model.predict_proba(df_input)[0,1]    
    return PredictionResponse(
        prevision = "Restrasado" if pred == 1 else "Puntual",
        probabilidad = round(float(proba), 2)
    )
"""
@app.post("/predict")
def predict_pr(request: PredictionRequest):
    #preparar los datos de entrada para el modelo
    df_input = pd.DataFrame([{
        "marketing_airline_network": request.aerolinea,
        "airport_code": request.origen,
        "destcityname": request.destino,
        "distance": request.distancia,
        "year": request.fechaPartida.year,
        "month": request.fechaPartida.month,
        "dayofmonth": request.fechaPartida.day,
        "day_of_week": request.fechaPartida.weekday(),
        "hour": request.fechaPartida.hour,
        "temp_mean": request.temp_mean,
        "precipitation": request.precipitation,
        "wind_speed": request.wind_speed
    }])
    # Realizar la predicción utilizando el modelo cargado
    pred = model.predict(df_input)[0]
    proba = model.predict_proba(df_input)[0,1]    
    return PredictionResponse(
        prevision = "Retrasado" if pred == 1 else "Puntual",
        probabilidad = round(float(proba), 2)
    )