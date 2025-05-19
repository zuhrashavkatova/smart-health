from .models import Prediction

def save_prediction(request, prediction_type, result, form_data=None):
    history = Prediction(
        user=request.user,
        prediction_type=prediction_type,
        result=result,
        input_data=form_data if form_data else {},  # input_data ni kiritish juda muhim
    )
    history.save()


