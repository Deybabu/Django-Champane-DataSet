from django.shortcuts import render, redirect
from .forms import DateRangeForm

def Home(request):
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('/')  # Redirect to a success page
    else:
        form = DateRangeForm()
    
    return render(request, 'Home/index.html', {'form': form})
