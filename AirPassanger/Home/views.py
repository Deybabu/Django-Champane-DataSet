from django.shortcuts import render, redirect
from .forms import DateRangeForm
import os
import pickle
import matplotlib.pyplot as plt
from io import BytesIO
import base64

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
            
            # Create a Matplotlib plot
            plt.figure(figsize=(12, 6))
            plt.plot(predictions, label='SARIMA Predictions', linestyle='--', color='red', marker='o')
            plt.xlabel('Date')
            plt.ylabel('Sales')
            plt.title('SARIMA Predictions')
            plt.grid(True)

            # Save the plot as a BytesIO object
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            plt.close()

            # Convert the BytesIO object to base64 for embedding in HTML
            plot_data = base64.b64encode(buffer.read()).decode('utf-8')
             
            return render(request, 'Home/index.html', {'form': form, 'plot_data': plot_data})  # Redirect to a success page
    else:
        form = DateRangeForm()
    
    return render(request, 'Home/index.html', {'form': form})
