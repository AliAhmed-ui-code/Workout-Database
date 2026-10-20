from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CreateWorkoutForm
from .models import Workout

def create_workout(request):
    if request.method == "POST":
        form = CreateWorkoutForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("create_workout")
    else:
        form = CreateWorkoutForm()
        
    return render(request, 'workouts/create_workout.html', {'form': form})

def search_workouts(request):
    query = request.GET.get('q')
    workouts = Workout.objects.filter(name__icontains=query) if query else []
    return render(request, 'workouts/search_workouts.html', {'workouts': workouts, 'query': query})


