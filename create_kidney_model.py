# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# import joblib

# df = pd.read_csv('kidney_disease.csv')

# df = df.dropna()  # Soddalashtirish uchun

# X = df.drop('classification', axis=1)
# y = df['classification'].map({'ckd':1, 'notckd':0})

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = DecisionTreeClassifier()
# model.fit(X_train, y_train)

# joblib.dump(model, 'ml_models/kidney_model.pkl')

# import os
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# import joblib

# df = pd.read_csv('kidney_disease.csv')
# df = df.dropna()  # NaN qiymatlarni olib tashlash

# X = df.drop('classification', axis=1)
# y = df['classification'].map({'ckd': 1, 'notckd': 0})

# # Matnli ustunlarni raqamga o‘girish
# for column in X.columns:
#     if X[column].dtype == 'object':
#         le = LabelEncoder()
#         X[column] = le.fit_transform(X[column])

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = DecisionTreeClassifier()
# model.fit(X_train, y_train)

# joblib.dump(model, 'ml_models/kidney_model.pkl')

# print("✅ Model muvaffaqiyatli saqlandi.")

# # print(X.columns)
# # print(len(X.columns))



import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# 1. Faylni o'qish
df = pd.read_csv("kidney_disease.csv").dropna()

# 2. Bizga kerak bo'lgan 14 ustun ro'yxati
feature_cols = [
    "age", "bp", "sg", "al", "su",
    "bgr", "bu", "sc", "sod", "pot",
    "hemo", "pcv", "wc", "rc"
]

# 3. Faqat shu ustunlarni va targetni ajratib olamiz
X = df[feature_cols].copy()
y = df["classification"].map({"ckd": 1, "notckd": 0})

# 4. Kategoriyali ustun bo'lsa, kodlash (bu 14 ta ichida yo'q, lekin shablon sifatida qoldirdik)
for col in X.select_dtypes("object").columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])

# 5. Train-test bo'linishi va model
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 6. Model va ustun nomlarini saqlash
joblib.dump(model, "ml_models/kidney_model.pkl")
joblib.dump(feature_cols, "ml_models/kidney_features.pkl")

print("✅ 14 ustunli model muvaffaqiyatli saqlandi.")
