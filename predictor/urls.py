# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('result/', views.predict, name='predict'),
#     path('history/', views.history, name='history'),
# ]


from django.urls import include, path

from predictor.utils import save_prediction
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result_view, name='result'),
    path('predict/diabetes/', views.predict_diabetes, name='predict_diabetes'),
    path('predict/heart/', views.predict_heart, name='predict_heart'),
    path('predict/kidney/', views.predict_kidney, name='predict_kidney'),
    path('predict/liver/', views.predict_liver, name='predict_liver'),
    path('history/', views.history, name='history'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('save-prediction/', save_prediction, name='save_prediction'),
]


