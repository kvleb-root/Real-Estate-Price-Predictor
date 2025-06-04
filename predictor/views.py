 # views.py
from django.shortcuts import render
import joblib
import numpy as np
import os

model = joblib.load(os.path.join(os.path.dirname(__file__), 'house_price_model.pkl'))

def predict_price(request):
    prediction = None

    if request.method == 'POST':
        area = int(request.POST.get('area'))
        bedrooms = int(request.POST.get('bedrooms'))
        bathrooms = int(request.POST.get('bathrooms'))
        stories = int(request.POST.get('stories'))
        mainroad = int(request.POST.get('mainroad'))
        guestroom = int(request.POST.get('guestroom'))
        basement = int(request.POST.get('basement'))
        hotwaterheating = int(request.POST.get('hotwaterheating'))
        airconditioning = int(request.POST.get('airconditioning'))
        parking = int(request.POST.get('parking'))
        prefarea = int(request.POST.get('prefarea'))
        furnishingstatus = int(request.POST.get('furnishingstatus'))

        data = np.array([[area, bedrooms, bathrooms, stories, mainroad, guestroom,
                          basement, hotwaterheating, airconditioning, parking, prefarea, furnishingstatus]])

        prediction = model.predict(data)[0]
        prediction = round(prediction, 2)

    return render(request, 'form.html', {'prediction': prediction})
