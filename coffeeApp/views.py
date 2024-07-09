from django.shortcuts import redirect, render
from coffeeApp.forms import FormCoffee
# Create your views here.

def index(request):
    form = FormCoffee()
    if request.method == 'POST' :
        form = FormCoffee(request.POST)
        if form.is_valid():
            form.save()
        #return index(request)
    data = {'form': form}
    return render(request, 'coffeeApp/index.html', data)
