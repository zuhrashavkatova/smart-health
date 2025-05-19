import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

#Dataset yuklash
f = pd.read_csv('diabetes.csv')  # Bu CSV fayl sening papkangda bo‘lishi kerak

X = df.drop('Outcome', axis=1) 
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Modelni saqlash
model_dir = 'ml_models'
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

joblib.dump(model, os.path.join(model_dir, 'diabetes_model.pkl'))

# Modelni sinovdan o'tkazish
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model aniqligi: {accuracy:.2f}')



# import pandas as pd
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import joblib

# # Dataset yuklash
# df = pd.read_csv('diabetes.csv')  # Bu CSV fayl sening papkangda bo‘lishi kerak
# X = df.drop('Outcome', axis=1)
# y = df['Outcome']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = LogisticRegression(max_iter=1000)
# model.fit(X_train, y_train)

# # Modelni saqlash
# joblib.dump(model, 'ml_models/diabetes_model.pkl')

# # Modelni sinovdan o'tkazish
# y_pred = model.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print(f'Model aniqligi: {accuracy:.2f}')