from django import forms

class DiabetesForm(forms.Form):
    Pregnancies = forms.IntegerField(label="Homiladorlik soni")
    Glucose = forms.FloatField(label="Glyukoza darajasi (qon shakar)")
    BloodPressure = forms.FloatField(label="Qon bosimi")
    SkinThickness = forms.FloatField(label="Terining qalinligi")
    Insulin = forms.FloatField(label="Insulin darajasi")
    BMI = forms.FloatField(label="Tana massasi indeksi (BMI)")
    DiabetesPedigreeFunction = forms.FloatField(label="Merosi koeffitsiyenti (Diabetga moyillik)")
    Age = forms.IntegerField(label="Yosh")

class HeartForm(forms.Form):
    age = forms.IntegerField(label="Yosh")
    sex = forms.IntegerField(label="Jinsi (1 = Erkak, 0 = Ayol)")
    cp = forms.IntegerField(label="Ko'krak og‘rig‘i turi (0–3)")
    trestbps = forms.FloatField(label="Tinch holatdagi qon bosimi (mm Hg)")
    chol = forms.FloatField(label="Xolesterin miqdori (mg/dl)")
    fbs = forms.IntegerField(label="Qon shakar > 120 mg/dl (1 = ha, 0 = yo‘q)")
    restecg = forms.IntegerField(label="Elektrokardiografiya natijasi (0–2)")
    thalach = forms.FloatField(label="Erishilgan maksimal yurak urish tezligi")
    exang = forms.IntegerField(label="Jismoniy mashq natijasida og‘riq (1 = ha, 0 = yo‘q)")
    oldpeak = forms.FloatField(label="ST segmenti pasayishi darajasi")
    slope = forms.IntegerField(label="ST segmenti qiyaligi (0–2)")
    ca = forms.IntegerField(label="Asosiy qon tomirlari soni (0–4)")
    thal = forms.IntegerField(label="Talassemiya turi (1 = fiksatsiyalangan, 2 = qaytuvchan, 3 = normal)")

class KidneyForm(forms.Form):
    age = forms.IntegerField(label="Yosh")
    bp = forms.FloatField(label="Qon bosimi")
    sg = forms.FloatField(label="Siydik og‘irligi (specific gravity)")
    al = forms.IntegerField(label="Al’bumin miqdori")
    su = forms.FloatField(label="Qondagi shakar darajasi")
    bgr = forms.FloatField(label="Tasodifiy qon glyukoza darajasi")
    bu = forms.FloatField(label="Qon mochevinasi miqdori")
    sc = forms.FloatField(label="Serum kreatinini miqdori")
    sod = forms.FloatField(label="Qondagi natriy miqdori")
    pot = forms.FloatField(label="Qondagi kaliy miqdori")
    hemo = forms.FloatField(label="Gemoglobin darajasi")
    pcv = forms.IntegerField(label="Qadoqlangan hujayralar hajmi (PCV)")
    wc = forms.FloatField(label="Oq qon hujayralari soni")
    rc = forms.FloatField(label="Qizil qon hujayralari soni")


class LiverForm(forms.Form):
    Age = forms.IntegerField(label="Yosh")
    Gender = forms.ChoiceField(
        choices=[('1', 'Erkak'), ('0', 'Ayol')],
        label="Jinsi"
    )
    Total_Bilirubin = forms.FloatField(label="Umumiy bilirubin")
    Direct_Bilirubin = forms.FloatField(label="To‘g‘ridan-to‘g‘ri bilirubin")
    Alkaline_Phosphotase = forms.FloatField(label="Qon fosfataza miqdori")
    Alamine_Aminotransferase = forms.FloatField(label="Alanin aminotransferaza (ALT) darajasi")
    Aspartate_Aminotransferase = forms.FloatField(label="Aspartat aminotransferaza (AST) darajasi")
    Total_Proteins = forms.FloatField(label="Umumiy oqsillar")
    Albumin = forms.FloatField(label="Al’bumin miqdori")
    Albumin_and_Globulin_Ratio = forms.FloatField(label="Al’bumin va globulin nisbati")
