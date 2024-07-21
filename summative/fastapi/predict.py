from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist
import numpy as np
import joblib
import uvicorn

# Initialize the FastAPI app
app = FastAPI()

# Define a request model with constraints
class DiabetesFeatures(BaseModel):
    features: conlist(float, min_items=10, max_items=10)  # Exactly 10 features

# Load the trained model
try:
    model = joblib.load("model.pkl")
except FileNotFoundError:
    raise RuntimeError("Model file not found. Ensure 'model.pkl' is in the correct directory.")

# Define the root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Diabetes Prediction API"}

# Define the prediction endpoint
@app.post("/predict")
def predict(diabetes_features: DiabetesFeatures):
    try:
        # Extract features from the request
        features = np.array(diabetes_features.features).reshape(1, -1)
        
        # Check if the features are within the valid range
        if not np.all((features >= 1) & (features <= 500)):
            raise HTTPException(
                status_code=400,
                detail="All features must be between 1 and 500."
            )
        
        # Make a prediction
        prediction = model.predict(features)
        # Return the prediction
        return {"prediction": prediction[0]}
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )

# Define the status endpoint
@app.get("/status")
def status():
    try:
        # Check the model status
        model_status = "ready" if model else "not loaded"
        return {"status": "ok", "model_status": model_status}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )

# Run the API
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
