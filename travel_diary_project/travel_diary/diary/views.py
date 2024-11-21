
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Travel
from .forms import TravelForm

def travel_list(request):
    travels = Travel.objects.all()
    return render(request, 'diary/travel_list.html', {'travels': travels})

@login_required
def create_travel(request):
    if request.method == 'POST':
        form = TravelForm(request.POST, request.FILES)
        if form.is_valid():
            travel = form.save(commit=False)
            travel.user = request.user
            travel.save()
            return redirect('travel_list')
    else:
        form = TravelForm()
    return render(request, 'diary/create_travel.html', {'form': form})
