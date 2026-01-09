import sys
import json
import joblib
import os

# Set directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
model = joblib.load('crop_model.pkl')

while True:
    line = sys.stdin.readline()
    if not line:
        break
    try:
        data = json.loads(line)
        features = [[data['N'], data['P'], data['K'], data['M']]]
        
        # 1. Predict status
        prediction = model.predict(features)[0]
        
        # 2. Get Importance scores (The "Why")
        # We use the model's feature_importances_ 
        importance = [round(x * 100, 2) for x in model.feature_importances_]
        
        # 3. Output rich data
        print(json.dumps({
            "status": prediction,
            "npk_data": data,
            "bottlenecks": {
                "Nitrogen": importance[0],
                "Phosphorus": importance[1],
                "Potassium": importance[2],
                "Moisture": importance[3]
            }
        }))
        sys.stdout.flush()
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.stdout.flush()