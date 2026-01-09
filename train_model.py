import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Synthetic Dataset: [Nitrogen, Phosphorus, Potassium, Moisture]
data = {
    'N': [90, 20, 85, 40, 95, 10, 50, 80],
    'P': [50, 45, 50, 15, 55, 40, 20, 50],
    'K': [40, 35, 40, 40, 45, 15, 20, 40],
    'M': [50, 45, 95, 50, 98, 40, 50, 10],
    'Health': ['Optimal', 'Needs_N', 'Waterlogged', 'Needs_P', 'Waterlogged', 'Needs_K', 'Low_Nutrient', 'Dry']
}

df = pd.DataFrame(data)
X = df[['N', 'P', 'K', 'M']]
y = df['Health']

# Train the model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Save the brain
joblib.dump(model, 'crop_model.pkl')
print("Model trained successfully!")