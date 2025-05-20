import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Fill missing values
    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['Embarked'].fillna('S', inplace=True)
    df['Fare'].fillna(df['Fare'].median(), inplace=True)

    # Drop unused columns
    df.drop(['Cabin', 'Ticket', 'Name', 'PassengerId'], axis=1, inplace=True)

    # Encode categorical variables
    label = LabelEncoder()
    df['Sex'] = label.fit_transform(df['Sex'])
    df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

    return df
    