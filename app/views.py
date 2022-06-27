from django.shortcuts import render, redirect
from app.forms import VagasForm
from app.forms import CandidatosForm
from app.models import Vagas
from app.models import Candidatos

# Pagina inicial

def home(request):
    data = {}
    data['db'] = Vagas.objects.all()
    return render(request, 'index.html', data)

# Primeiro formulario para adicionar uma vaga

def form(request):
    data = {}
    data['form'] = VagasForm
    return render(request, 'vagasForm.html', data)

# Botão save dentro do formulario anterior. Adicionando vaga ao banco

def create(request):
    form = VagasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

# Editando vagas cadastradas via botoes para manipular tabela de vagas cadastradas
# Abrindo formulario de edição de vaga

def edit(request, pk):
    data = {}
    data['db'] = Vagas.objects.get(pk=pk)
    data['form'] = VagasForm(instance=data['db'])
    return render(request, 'vagasForm.html', data)

# ===================================================================
# Editando a vaga clicando em salvar

def update(request, pk):
    data = {}
    data['db'] = Vagas.objects.get(pk=pk)
    form = VagasForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

# ===================================================================
# Deletando vaga cadastrada

def delete(request, pk):
    db = Vagas.objects.get(pk=pk)
    db.delete()
    return redirect('home')

# ===================================================================

# Adicionando candidatos a vaga previamente cadastrada
# Abrindo formulario de inclusao de candidatos

def add(request, pk):
    data = {}
    data ['form'] = CandidatosForm
    return render(request, 'candidatoForm.html', data)

# ===================================================================
# Botão save dentro do formulario anterior. Adicionando candidato ao banco

def createCandidate(request):
    form = CandidatosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

# ===================================================================
# Visualização de tabela de candidatos cadastrados dentro da vaga

def view(request, pk):
    data = {}
    data['db'] = Candidatos.objects.filter(vaga_id=pk)
    return render(request, 'listaCandidatos.html', data)

# ===================================================================
# Editando dados de candidatos

# def editCandidate(request, pk):
#     data = {}
#     data['db'] = Candidatos.objects.get(pk=pk)
#     data['form'] = CandidatosForm(instance=data['db'])
#     return render(request, 'candidatoForm.html')

# ===================================================================
# Atualizando dados lançados para cada candidato clicando em salvar no formulario
# def updateCandidate(request, pk):
#     data = {}
#     data['db'] = Candidatos.objects.get(pk=pk)
#     form = CandidatosForm(request.POST or None, instance=data['db'])
#     if form.is_valid():
#         form.save()
#         return redirect('view')     
