## Titanic Survival Prediction 

**Запустить в Google Colab:**  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fershtadt/titanic-survival-prediction/blob/main/notebooks/eda_and_model.ipynb)

---

## Описание

Проект предсказывает выживание пассажиров Титаника на основе данных: пол, возраст, класс билета, количество родственников на борту и другие признаки. Используется модель Random Forest.

---

## Структура проекта

```
titanic-survival-prediction/
├── data/                  # Датасет (train.csv)
├── models/                # Обученная модель (model.pkl)
├── notebooks/             # Jupyter ноутбук (EDA + вывод)
│   └── eda_and_model.ipynb
├── src/                   # Исходный код
│   ├── preprocessing.py
│   └── train_model.py
├── .gitignore
├── README.md
├── requirements.txt
└── .env
```

---

## Используемые модули

- Python 3.x
- Pandas, NumPy
- Scikit-learn
- Joblib
- Jupyter Notebook
- Git, GitHub

---

## Результаты

Модель `RandomForestClassifier` достигла:
- Точность предсказания: ~80% на валидации
- Сохранена в файл `models/model.pkl` через `joblib`

---

## Как запустить проект

```bash
# Установить зависимости
pip install -r requirements.txt

# Запустить обучение модели
PYTHONPATH=. python src/train_model.py
```