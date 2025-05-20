# 🚢 Titanic Survival Prediction 

[![GitHub last commit](https://img.shields.io/github/last-commit/fershtadt/titanic-survival-prediction)](https://github.com/fershtadt/titanic-survival-prediction)
[![GitHub repo size](https://img.shields.io/github/repo-size/fershtadt/titanic-survival-prediction)](https://github.com/fershtadt/titanic-survival-prediction)
[![Issues](https://img.shields.io/github/issues/fershtadt/titanic-survival-prediction)](https://github.com/fershtadt/titanic-survival-prediction/issues)
[![License: MIT](https://img.shields.io/github/license/fershtadt/titanic-survival-prediction)](https://github.com/fershtadt/titanic-survival-prediction/blob/main/LICENSE)

🔗 **Запустить в Google Colab:**  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fershtadt/titanic-survival-prediction/blob/main/notebooks/eda_and_model.ipynb)

---

## 📋 Описание

Проект предсказывает выживание пассажиров Титаника на основе данных: пол, возраст, класс билета, количество родственников на борту и другие признаки. Используется модель Random Forest.

---

## 📂 Структура проекта

titanic-survival-prediction/
├── data/ # Датасет (train.csv)
├── models/ # Обученная модель (model.pkl)
├── notebooks/ # Jupyter ноутбук (EDA + вывод)
│ └── eda_and_model.ipynb
├── src/ # Исходный код
│ ├── preprocessing.py
│ └── train_model.py
├── .gitignore
├── README.md
├── requirements.txt
└── .env


---

## 🛠 Используемые технологии

- Python
- Pandas, NumPy
- Scikit-learn
- Joblib
- Jupyter Notebook
- Git, GitHub

---

## 📈 Результаты

Модель `RandomForestClassifier` достигла:
- Accuracy: ~80% на валидации
- Сохранена в файл `models/model.pkl` через `joblib`

---

## 🚀 Как запустить проект

```bash
# Установить зависимости
pip install -r requirements.txt

# Запустить обучение модели
PYTHONPATH=. python src/train_model.py
