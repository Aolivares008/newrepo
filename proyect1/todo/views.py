from django.shortcuts import render

# Create your views here.

from .models import Tarea
from .forms import TareaForm

def home(request):
    tareas = Tarea.objects.all()
    context = {'tareas':tareas}
    return render (request, 'todo/home.html', context)

def agregar(request, tarea_id):
    if request.method == "POST":
        form = TareaForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo/home.html')
    else:
        form = TareaForm()

    context = {'form':form}
    return render (request, 'todo/agregar.html', context)

def eliminar(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect("todo/home.html")

def editar(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    if request.method == "POST":
        form = TareaForm(request.POST, instance = tarea)
        if form.is_valid():
            form.save()
            return redirect ("home")
    return render (request, 'todo/home.html', context)
