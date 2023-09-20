import numpy as np
import pandas as pd
import statsmodels.api as sm
import yfinance as yf

data = yf.download("DOGE-RUB",start="2020-01-01",end="2023-09-20",interval="1d")

# Загрузка данных в формате CSV
#data = pd.read_csv('data.csv')

# Определение зависимой переменной y и независимой переменной x
y = data['Close']
x = data[['Open','Volume']]

# Добавление константы в независимые переменные
x = sm.add_constant(x)

# Создание и обучение модели линейной регрессии
model = sm.OLS(y, x)
results = model.fit()

# Вывод результатов
print(results.summary())

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

# Загрузка данных в формате массива NumPy
#x = np.array(data["Close"])  # Независимые переменные
#y = np.array(data["Close"])  # Зависимая переменная

# Создание и обучение модели множественной линейной регрессии
model = LinearRegression()
model.fit(x, y)

# Получение коэффициентов регрессии
coefficients = model.coef_

# Предсказание значений
predictions = model.predict(x)

# Оценка модели с использованием коэффициента детерминации (R^2)
r2 = r2_score(y, predictions)

# Вывод результатов
print("Коэффициенты регрессии:", coefficients)
print("Предсказанные значения:", predictions)
print("Коэффициент детерминации (R^2):", r2)
