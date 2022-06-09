from django.shortcuts import render
from django.shortcuts import render, redirect
from app.forms import VagasForm
from app.forms import CandidatosForm
from app.models import Vagas
from app.models import Candidatos

# Create your views here.
def home(request):
    data = {}
    data['db'] = Vagas.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = VagasForm
    return render(request, 'vagasForm.html', data)

def create(request):
    form = VagasForm(request.POST or None)
    print('AQUII', request.POST.get('data'))
    if form.is_valid():
        form.save()
        return redirect('home')   

def edit(request, pk):
    data = {}
    data['db'] = Vagas.objects.get(pk=pk)
    data['form'] = VagasForm(instance=data['db'])
    return render(request, 'vagasForm.html', data)

def add(request, pk):
    data = {}
    data ['form'] = CandidatosForm
    return render(request, 'candidatoForm.html', data)
    
def update(request, pk):
    data = {}
    data['db'] = Vagas.objects.get(pk=pk)
    form = VagasForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')       

def delete(request, pk):
    db = Vagas.objects.get(pk=pk)
    db.delete()
    return redirect('home')
             