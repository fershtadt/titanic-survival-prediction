import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from src.preprocessing import preprocess

def train():
    df = pd.read_csv("data/train.csv")
    df = preprocess(df)

    X = df.drop('Survived', axis=1)
    y = df['Survived']

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_val)
    acc = accuracy_score(y_val, y_pred)
    print(f"Validation Accuracy: {acc:.4f}")

    joblib.dump(model, "models/model.pkl")

if __name__ == "__main__":
    train()
