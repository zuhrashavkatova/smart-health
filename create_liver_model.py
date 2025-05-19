# import pandas as pd
# from sklearn.ensemble import GradientBoostingClassifier
# from sklearn.model_selection import train_test_split
# import joblib

# df = pd.read_csv('liver.csv')

# X = df.drop('Dataset', axis=1)
# y = df['Dataset']  # 1 = jigar kasalligi bor, 2 = yo'q

# y = y.map({1:1, 2:0})  # Binary classification uchun

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = GradientBoostingClassifier()
# model.fit(X_train, y_train)

# joblib.dump(model, 'ml_models/liver_model.pkl')



import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

# 1. CSV faylni o‘qish
df = pd.read_csv('liver.csv')

# 2. NaN (bo‘sh) qiymatlarni tashlab yuborish
df = df.dropna()

# 3. Kategorik ustunni (Gender) raqamlarga aylantirish
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])  # Male = 1, Female = 0

# 4. X (kiruvchi ma’lumotlar) va y (target/maqsad)
X = df.drop('Dataset', axis=1)  # Dataset - bu target
y = df['Dataset']

# 5. Train/test uchun bo‘lish
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Modelni tanlash va o‘rgatish
model = GradientBoostingClassifier()
model.fit(X_train, y_train)

# Modelni saqlash
with open('liver_model.pkl', 'wb') as file:
    pickle.dump(model, file)
print("Model saqlandi: liver_model.pkl")

# 7. Test qilish va aniqlikni chiqarish
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model aniqligi: {accuracy:.2f}")












# import pandas as pd
# from sklearn.ensemble import GradientBoostingClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# import joblib

# # Faylni yuklash (xatoli qatorlarni tashlab ketish)
# df = pd.read_csv('liver.csv', on_bad_lines='skip')

# # Ustun nomlarini ko'rish (Debug uchun)
# print("USTUNLAR:", df.columns)

# # NaN qiymatlarni olib tashlash
# df = df.dropna()

# # Agar asl ustun nomi 'Dataset ' (bo‘shliq bilan) bo‘lsa, uni aniqlash
# df.columns = df.columns.str.strip()  # Ustun nomlaridagi bo‘shliqlarni olib tashlash

# # Target ustunni ajratish
# y = df['Dataset'].map({1: 1, 2: 0})  # 1 = kasal, 0 = sog'

# # X ni ajratish (ya'ni barcha ustunlar - 'Dataset')
# X = df.drop('Dataset', axis=1)

# # Matnli ustunlarni raqamlash
# for column in X.columns:
#     if X[column].dtype == 'object':
#         le = LabelEncoder()
#         X[column] = le.fit_transform(X[column])

# # Train/Test bo'lib ajratish
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)













# import pandas as pd
# from sklearn.ensemble import GradientBoostingClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# import joblib
# import os

# # CSV faylni to'g'ri o'qish (keraksiz ustunlar, bo'sh qatorlar bo'lmasin)
# df = pd.read_csv("liver.csv", skip_blank_lines=True, on_bad_lines='skip')

# # Keraksiz ustunlarni olib tashlash (masalan: 'Unnamed: ...')
# df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# # Ustun nomlaridagi bo'sh joylarni olib tashlash
# df.columns = df.columns.str.strip()

# # NaN (bo‘sh) qiymatlarni olib tashlash
# df = df.dropna()

# # Target ustun: Dataset (1 = kasal, 2 = sog') -> (1 = True, 0 = False)
# y = df['Dataset'].map({1: 1, 2: 0})

# # X: 'Dataset' ustunidan tashqari barcha ustunlar
# X = df.drop('Dataset', axis=1)




# # Matnli (katta) ustunlarni raqamli (numerik)ga o‘tkazish (masalan, 'Gender')
# for column in X.columns:
#     if X[column].dtype == 'object':
#         le = LabelEncoder()
#         X[column] = le.fit_transform(X[column])

# # Ma'lumotlarni o'qitish va test uchun ajratish
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Model yaratish va o‘qitish
# model = GradientBoostingClassifier()
# model.fit(X_train, y_train)

# # Modelni saqlash
# os.makedirs('ml_models', exist_ok=True)
# joblib.dump(model, 'ml_models/liver_model.pkl')

# print("✅ Model muvaffaqiyatli o‘qitildi va 'ml_models/liver_model.pkl' ga saqlandi.")


