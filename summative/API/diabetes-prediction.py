from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, ValidationError
import numpy as np
import joblib
import uvicorn

# Initialize the FastAPI app
app = FastAPI()

# Define a request model
class DiabetesFeatures(BaseModel):
    features: list[float]

# Load the trained model
try:
    model = joblib.load("model.pkl")
except FileNotFoundError:
    raise RuntimeError("Model file not found. Ensure 'model.pkl' is in the correct directory.")

# Define the root endpoint
@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    return {"message": "Welcome to the Diabetes Prediction API"}

# Define the prediction endpoint
@app.post("/predict", status_code=status.HTTP_200_OK)
def predict(diabetes_features: DiabetesFeatures):
    try:
        # Extract features from the request
        features = np.array(diabetes_features.features).reshape(1, -1)
        # Check if the number of features is correct
        if features.shape[1] != 8:  # Assuming the model expects 8 features (adjust if necessary)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Expected 8 features, but got {features.shape[1]}"
            )
        # Make a prediction
        prediction = model.predict(features)
        # Return the prediction
        return {"prediction": prediction[0]}
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )

# Define the status endpoint
@app.get("/status", status_code=status.HTTP_200_OK)
def status():
    try:
        # Check the model status
        model_status = "ready" if model else "not loaded"
        return {"status": "ok", "model_status": model_status}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )

# Run the API
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
