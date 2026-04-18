import pickle
import numpy as np
import os

# ------------------ Load the Ideal Yield Model ------------------
with open(os.path.join("models", "Ideal_Yield_Model.pkl"), "rb") as f:
    obj = pickle.load(f)

# Check if pickle is a dict containing the model
if isinstance(obj, dict):
    model = obj.get("model")       # extract the actual model
    scaler = obj.get("scaler")     # optional, if you saved a scaler
else:
    model = obj
    scaler = None

# ------------------ Sample Test Input ------------------
# Crop_enc: 0-9, other features in same order as trained
test_input = np.array([[ 
    0,      # Crop_enc (e.g., 0 = rice)
    22.5,   # Temperature
    60.0,   # Humidity
    45.0,   # Moisture
    1200.0, # Light Intensity
    400.0   # Rainfall
]])

# If you have a scaler, transform input
if scaler:
    test_input = scaler.transform(test_input)

# ------------------ Make Prediction ------------------
prediction = model.predict(test_input)

# ------------------ Print prediction ------------------
print("🌱 Ideal Yield Prediction (kg/ha):", np.array(prediction))
