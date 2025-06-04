from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {'prediction': None})

def predict(request):
    if request.method == 'POST':
        # Récupération des données du formulaire
        try:
            area = request.POST.get('area')
            bedrooms = request.POST.get('bedrooms')
            bathrooms = request.POST.get('bathrooms')
            stories = request.POST.get('stories')
            mainroad = request.POST.get('mainroad')
            guestroom = request.POST.get('guestroom')
            basement = request.POST.get('basement')
            hotwaterheating = request.POST.get('hotwaterheating')
            airconditioning = request.POST.get('airconditioning')
            parking = request.POST.get('parking')
            prefarea = request.POST.get('prefarea')
            furnishingstatus = request.POST.get('furnishingstatus')

            # Simulation d'une prédiction pour test
            prediction = f"{250000 + (int(area) * 1000):,.2f} €"
            return render(request, 'index.html', {'prediction': prediction})
        except Exception as e:
            return render(request, 'index.html', {'prediction': None})
    
    return render(request, 'index.html', {'prediction': None})
