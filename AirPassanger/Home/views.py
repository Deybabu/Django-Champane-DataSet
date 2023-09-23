from django.shortcuts import render, redirect
from .forms import DateRangeForm
import os
import pickle
def Home(request):
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            form.save() 
            print("Start Date", form.cleaned_data['start_date'])
            print("End Date", form.cleaned_data['end_date'])
            current_directory = os.path.dirname(os.path.abspath(__file__))
            pickle_file_path = os.path.join(current_directory, 'model_sarimax_fit1.pkl')
            model_path = pickle_file_path
            with open(model_path, 'rb') as file:
                loaded_model = pickle.load(file)
            start=form.cleaned_data['start_date']
            end=form.cleaned_data['end_date']
            predictions=loaded_model.predict(start,end)
            print(predictions)   
            return redirect('/')  # Redirect to a success page
    else:
        form = DateRangeForm()
    
    return render(request, 'Home/index.html', {'form': form})
