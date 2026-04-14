import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# ✅ Import result function
from src.result import save_results

# ==============================
# 📁 Create folders if not exist
# ==============================
os.makedirs("images", exist_ok=True)
os.makedirs("models", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# ==============================
# 📊 Load dataset
# ==============================
df = pd.read_csv("data/iot_dataset.csv")

# Features and target
X = df[["temperature", "vibration", "pressure"]]
y = df["failure"]

# ==============================
# 🔀 Split data
# ==============================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# ==============================
# 🤖 Train model
# ==============================
model = RandomForestClassifier()
model.fit(X_train, y_train)

# ==============================
# 🔮 Prediction
# ==============================
y_pred = model.predict(X_test)

print("Predictions:", y_pred)

# ==============================
# 📊 Save Results (from result.py)
# ==============================
save_results(y_test, y_pred)

# ==============================
# 📊 1. Scatter Plot
# ==============================
plt.scatter(df["temperature"], df["vibration"], c=df["failure"])
plt.xlabel("Temperature")
plt.ylabel("Vibration")
plt.title("Temperature vs Vibration")
plt.savefig("images/scatter_plot.png")
plt.show()

# ==============================
# 📊 2. Feature Distribution
# ==============================
df.hist(figsize=(8,6))
plt.suptitle("Feature Distribution")
plt.savefig("images/feature_distribution.png")
plt.show()

# ==============================
# 📊 3. Correlation Heatmap
# ==============================
sns.heatmap(df.corr(), annot=True)
plt.title("Feature Correlation")
plt.savefig("images/correlation.png")
plt.show()

# ==============================
# 📊 4. Failure Count Plot
# ==============================
sns.countplot(x="failure", data=df)
plt.title("Failure Count")
plt.savefig("images/failure_count.png")
plt.show()

# ==============================
# 💾 Save Model
# ==============================
joblib.dump(model, "models/model.pkl")

print("\n✅ Model saved successfully!")