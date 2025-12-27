from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd
import logging
import os
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Load model and scaler with error handling
def load_model_artifacts():
    """
    Load model and scaler from disk with error handling.
    
    Returns:
        tuple: (model, scaler) objects
        
    Raises:
        FileNotFoundError: If model files are missing
        Exception: If files are corrupted or cannot be loaded
    """
    model_path = "model.pkl"
    scaler_path = "scaler.pkl"
    
    try:
        # Check if model file exists
        if not os.path.exists(model_path):
            logger.error(f"Model file not found: {model_path}")
            raise FileNotFoundError(f"Model file not found: {model_path}")
        
        # Check if scaler file exists
        if not os.path.exists(scaler_path):
            logger.error(f"Scaler file not found: {scaler_path}")
            raise FileNotFoundError(f"Scaler file not found: {scaler_path}")
        
        # Load model
        logger.info(f"Loading model from {model_path}...")
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        logger.info(f"Model loaded successfully. Type: {type(model).__name__}")
        
        # Load scaler
        logger.info(f"Loading scaler from {scaler_path}...")
        with open(scaler_path, "rb") as f:
            scaler = pickle.load(f)
        logger.info(f"Scaler loaded successfully. Type: {type(scaler).__name__}")
        
        return model, scaler
        
    except FileNotFoundError as e:
        logger.error(f"File not found error: {str(e)}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Failed to load model artifacts: {str(e)}", exc_info=True)
        sys.exit(1)

# Load model and scaler at startup
model, scaler = load_model_artifacts()

# Define input schema
class Features(BaseModel):
    mean_radius: float
    mean_texture: float
    mean_perimeter: float
    mean_area: float
    mean_smoothness: float
    mean_compactness: float
    mean_concavity: float
    mean_concave_points: float
    mean_symmetry: float
    mean_fractal_dimension: float
    radius_error: float
    texture_error: float
    perimeter_error: float
    area_error: float
    smoothness_error: float
    compactness_error: float
    concavity_error: float
    concave_points_error: float
    symmetry_error: float
    fractal_dimension_error: float
    worst_radius: float
    worst_texture: float
    worst_perimeter: float
    worst_area: float
    worst_smoothness: float
    worst_compactness: float
    worst_concavity: float
    worst_concave_points: float
    worst_symmetry: float
    worst_fractal_dimension: float

# Initialize FastAPI app
app = FastAPI()

# Health check endpoint
@app.get("/health")
def health():
    return {"status": "API is running!"}

# Prediction endpoint
@app.post("/predict")
def predict(features: Features):
    try:
        # Log the prediction request
        logger.info(f"Received prediction request with {len(features.dict())} features")
        
        # Convert input to DataFrame
        input_df = pd.DataFrame([features.dict()])
        
        # Rename columns to match the model's expected feature names (with spaces)
        input_df.columns = [col.replace('_', ' ') for col in input_df.columns]
        
        # Scale input
        input_scaled = scaler.transform(input_df)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        
        # Log successful prediction
        logger.info(f"Prediction completed successfully. Result: {prediction}")
        
        return {"prediction": int(prediction)}
        
    except Exception as e:
        # Log the error with stack trace
        logger.error(f"Prediction failed: {str(e)}", exc_info=True)
        # Return 500 error with descriptive message
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
