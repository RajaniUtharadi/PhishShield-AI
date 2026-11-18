from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np

# Features:
# [length, dots, hyphen, @, https, ip, suspicious_keywords]

X = np.array([

    # SAFE URLs
    [20,1,0,0,1,0,0],
    [25,2,0,0,1,0,0],
    [30,2,1,0,1,0,0],
    [18,1,0,0,1,0,0],

    # SHORT PHISHING URLs
    [18,1,1,0,0,0,3],
    [20,1,1,0,0,0,4],
    [22,1,0,0,0,0,5],

    # LARGE PHISHING URLs
    [120,5,4,1,0,1,5],
    [150,6,5,1,0,1,6],
    [180,7,6,1,0,1,7]

])

# Labels
# 0 = Safe
# 1 = Phishing

y = np.array([
    0,0,0,0,
    1,1,1,
    1,1,1
])

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained successfully!")