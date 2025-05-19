# from django.db import models
# from django.contrib.auth.models import User

# class Prediction(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     prediction_type = models.CharField(max_length=50)  # diabetes, heart, kidney, liver
#     result = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.prediction_type}: {self.result} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"



from django.db import models
from django.contrib.auth.models import User

# class Prediction(models.Model):
#     # Umumiy maydonlar
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     prediction_type = models.CharField(max_length=50)  # diabetes, heart, kidney, liver
#     result = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     # input_data = models.JSONField()
#     input_data = models.TextField(default='')  # yoki kerakli bo‘lsa: null=True, blank=True

class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prediction_type = models.CharField(max_length=100)
    result = models.CharField(max_length=255)
    # input_data = models.TextField()
    input_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    # === Diabetes maydonlari ===
    Pregnancies = models.IntegerField(null=True, blank=True)
    Glucose = models.FloatField(null=True, blank=True)
    BloodPressure = models.FloatField(null=True, blank=True)
    SkinThickness = models.FloatField(null=True, blank=True)
    Insulin = models.FloatField(null=True, blank=True)
    BMI = models.FloatField(null=True, blank=True)
    DiabetesPedigreeFunction = models.FloatField(null=True, blank=True)
    DiabetesAge = models.IntegerField(null=True, blank=True)  # "Age" maydon nomi to‘qnashmasligi uchun

    # === Heart Disease maydonlari ===
    heart_age = models.IntegerField(null=True, blank=True)
    sex = models.IntegerField(null=True, blank=True)
    cp = models.IntegerField(null=True, blank=True)
    trestbps = models.FloatField(null=True, blank=True)
    chol = models.FloatField(null=True, blank=True)
    fbs = models.IntegerField(null=True, blank=True)
    restecg = models.IntegerField(null=True, blank=True)
    thalach = models.FloatField(null=True, blank=True)
    exang = models.IntegerField(null=True, blank=True)
    oldpeak = models.FloatField(null=True, blank=True)
    slope = models.IntegerField(null=True, blank=True)
    ca = models.IntegerField(null=True, blank=True)
    thal = models.IntegerField(null=True, blank=True)

    # === Kidney Disease maydonlari ===
    kidney_age = models.IntegerField(null=True, blank=True)
    bp = models.FloatField(null=True, blank=True)
    sg = models.FloatField(null=True, blank=True)
    al = models.IntegerField(null=True, blank=True)
    su = models.FloatField(null=True, blank=True)
    bgr = models.FloatField(null=True, blank=True)
    bu = models.FloatField(null=True, blank=True)
    sc = models.FloatField(null=True, blank=True)
    sod = models.FloatField(null=True, blank=True)
    pot = models.FloatField(null=True, blank=True)
    hemo = models.FloatField(null=True, blank=True)
    pcv = models.IntegerField(null=True, blank=True)
    wc = models.FloatField(null=True, blank=True)
    rc = models.FloatField(null=True, blank=True)

    # === Liver Disease maydonlari ===
    liver_Age = models.IntegerField(null=True, blank=True)
    Gender = models.CharField(max_length=1, null=True, blank=True)  # '1' yoki '0'
    Total_Bilirubin = models.FloatField(null=True, blank=True)
    Direct_Bilirubin = models.FloatField(null=True, blank=True)
    Alkaline_Phosphotase = models.FloatField(null=True, blank=True)
    Alamine_Aminotransferase = models.FloatField(null=True, blank=True)
    Aspartate_Aminotransferase = models.FloatField(null=True, blank=True)
    Total_Proteins = models.FloatField(null=True, blank=True)
    Albumin = models.FloatField(null=True, blank=True)
    Albumin_and_Globulin_Ratio = models.FloatField(null=True, blank=True)

    # def __str__(self):
    #     return f"{self.prediction_type}: {self.result} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"
    def __str__(self):
        if self.user:
                return f"{self.user.username} - {self.prediction_type}: {self.result} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"
        return f"{self.prediction_type}: {self.result} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"


    # def __str__(self):
    #     return f"Prediction for age {self.age} - {self.prediction_result}"