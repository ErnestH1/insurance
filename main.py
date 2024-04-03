from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from models import InputData  # Import the InputData model
from predictions import predict_charges  # Import the predict_charges function

app = FastAPI()

@app.get("/")
async def read_root():
    message = "Welcome to the Insurance Charges Prediction API!\n" \
              "Make a POST request to /predict with the following data in the request body: 'age', 'sex', 'bmi', 'children', 'smoker', 'region'.\n" \
              "For API documentation, visit: http://localhost:8000/docs"

    return PlainTextResponse(content=message, status_code=200)

@app.post("/predict/")
async def predict(input_data: InputData):
    return predict_charges(input_data)
