import json
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import joblib
import numpy as np
from collections import defaultdict
from .forms import DiabetesForm, HeartForm, KidneyForm, LiverForm
from .models import Prediction
from .utils import save_prediction
from predictor.models import Prediction

# 🏠 Home Page
def index(request):
    return render(request, 'index.html')

# 📊 Prediction History Page
@login_required
def prediction(request):
    user = request.user
    predictions = Prediction.objects.filter(user=user).order_by('-created_at')
    
    grouped_predictions = defaultdict(list)
    for record in predictions:
        grouped_predictions[record.prediction_type].append(record)
    return render(request, 'history.html', {
        'grouped_history': grouped_predictions,
        'predictions': predictions  
    })

@login_required
def history(request):
    predictions = Prediction.objects.filter(user=request.user).order_by('-created_at')
    
    history = {}
    for p in predictions:
        # print("Input Data:", p.input_data)    #for checking
        try:
            # input_data = json.loads(p.input_data)
            input_data = p.input_data
        except Exception:
            input_data = {}
        ptype = p.prediction_type
        if ptype not in history:
            history[ptype] = []
        history[ptype].append({
            'date': p.created_at,
            'result': p.result,
            'input_data': input_data,
            'age': input_data.get('Age', 'N/A'),
        })

    return render(request, 'history.html', {'history': history})


# 📂 Result View (Agar to'g'ridan-to'g'ri result.html sahifasini ko‘rish kerak bo‘lsa)
def result_view(request):
    return render(request, 'result.html')

# 🔄 Machine Learning modellari bir marta yuklanadi
models = {
    'diabetes': joblib.load('ml_models/diabetes_model.pkl'),
    'heart': joblib.load('ml_models/heart_model.pkl'),
    'kidney': joblib.load('ml_models/kidney_model.pkl'),
    'liver': joblib.load('ml_models/liver_model.pkl'),
}

# 🩸 Diabet bashorati
@login_required
def predict_diabetes(request):
    result = None
    if request.method == 'POST':
        form = DiabetesForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            input_data = np.array([
                cd['Pregnancies'],
                cd['Glucose'],
                cd['BloodPressure'],
                cd['SkinThickness'],
                cd['Insulin'],
                cd['BMI'],
                cd['DiabetesPedigreeFunction'],
                cd['Age']
            ]).reshape(1, -1)
            prediction = models['diabetes'].predict(input_data)[0]
            result = "🛑 Diabet bor" if prediction == 1 else "✅ Diabet yo'q"
            save_prediction(request, 'diabetes', result, form.cleaned_data)
    else:
        form = DiabetesForm()
    return render(request, 'result.html', {'form': form, 'result': result, 'title': '🩸 Diabet bashorati'})

# ❤️ Yurak bashorati
# @login_required
# def predict_heart(request):
#     result = None
#     if request.method == 'POST':
#         form = HeartForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             input_data = np.array([
#                 cd['age'],
#                 cd['sex'],
#                 cd['cp'],
#                 cd['trestbps'],
#                 cd['chol'],
#                 cd['fbs'],
#                 cd['restecg'],
#                 cd['thalach'],
#                 cd['exang'],
#                 cd['oldpeak'],
#                 cd['slope'],
#                 cd['ca'],
#                 cd['thal']
#             ]).reshape(1, -1)

#             prediction = models['heart'].predict(input_data)[0]
#             result = "🫀 Yurak kasalligi bor" if prediction == 1 else "✅ Yurak sog‘lom"
#             save_prediction(request, "heart", result, form.cleaned_data)

#     else:
#         form = HeartForm()

#     return render(request, 'result.html', {'form': form, 'result': result, 'title': '❤️ Yurak bashorati'})


@login_required
def predict_heart(request):
    result = None
    if request.method == 'POST':
        form = HeartForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            input_data = np.array([
                cd['age'],
                cd['sex'],
                cd['cp'],
                cd['trestbps'],
                cd['chol'],
                cd['fbs'],
                cd['restecg'],
                cd['thalach'],
                cd['exang'],
                cd['oldpeak'],
                cd['slope'],
                cd['ca'],
                cd['thal']
            ]).reshape(1, -1)

            prediction = models['heart'].predict(input_data)[0]
            result = "🫀 Yurak kasalligi bor" if prediction == 1 else "✅ Yurak sog‘lom"

            # Bu yerda 'result' ni save_prediction ga uzatamiz
            save_prediction(request, "heart", result, form.cleaned_data)
    else:
        form = HeartForm()

    # Bashoratlar ro'yxatini olish (jadval uchun)
    predictions = Prediction.objects.filter(user=request.user, prediction_type='heart').order_by('-created_at')

    return render(request, 'result.html', {
        'form': form,
        'result': result,
        'predictions': predictions  # jadval uchun ma'lumotlarni yuborish
    })





# 🧪 Buyrak bashorati
@login_required
def predict_kidney(request):
    result = None
    if request.method == 'POST':
        form = KidneyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            input_data = np.array([
                cd['age'],
                cd['bp'],
                cd['sg'],
                cd['al'],
                cd['su'],
                cd['bgr'],
                cd['bu'],
                cd['sc'],
                cd['sod'],
                cd['pot'],
                cd['hemo'],
                cd['pcv'],
                cd['wc'],
                cd['rc']
            ]).reshape(1, -1)
            prediction = models['kidney'].predict(input_data)[0]
            result = "🛑 Buyrak yetishmovchiligi bor" if prediction == 1 else "✅ Buyrak sog‘lom"
            save_prediction(request, 'kidney', result, form.cleaned_data)
    else:
        form = KidneyForm()
    return render(request, 'result.html', {'form': form, 'result': result, 'title': '🧪 Buyrak bashorati'})


# 🧬 Jigar bashorati
@login_required
def predict_liver(request):
    result = None
    if request.method == 'POST':
        form = LiverForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            input_data = np.array([
                int(cd['Gender']),
                cd['Age'],
                cd['Total_Bilirubin'],
                cd['Direct_Bilirubin'],
                cd['Alkaline_Phosphotase'],
                cd['Alamine_Aminotransferase'],
                cd['Aspartate_Aminotransferase'],
                cd['Total_Proteins'],
                cd['Albumin'],
                cd['Albumin_and_Globulin_Ratio']
            ]).reshape(1, -1)

            prediction = models['liver'].predict(input_data)[0]
            result = "🛑 Jigar kasalligi bor" if prediction == 1 else "✅ Jigar sog‘lom"
            save_prediction(request, 'liver', result, form.cleaned_data)
    else:
        form = LiverForm()

    return render(request, 'result.html', {'form': form, 'result': result, 'title': '🧬 Jigar bashorati'})


