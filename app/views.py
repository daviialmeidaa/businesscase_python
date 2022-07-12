from django.shortcuts import render, redirect
from app.forms import VagasForm
from app.forms import CandidatosForm
from app.forms import ParceiroForm
from app.forms import ColaboradoresForm
from app.forms import RegrasFeriasForm
from app.forms import DefinirFeriasForm
from app.models import Vagas
from app.models import Candidatos
from app.models import Colaboradores
from app.models import DefinirFerias





# ===============================   =================================  ======================   ================================ ===============================
# ===============================   =================================  VISUALIZAÇÃO DE LISTAS   ================================ ================================

# ===========================================================================
# Visualização da Pagina inicial

def home(request):
    data = {}
    data['db'] = Vagas.objects.all()
    return render(request, 'index.html', data)

# ===========================================================================
# Visualização de tabela de candidatos cadastrados dentro da vaga

def view(request, pk):
    data = {}
    data['db'] = Candidatos.objects.filter(vaga_id=pk)
    return render(request, 'listaCandidatos.html', data)

# ===========================================================================
# Visualização de tablea de colaboradores cadastrados   

def View_Colaboradores(request):
    data = {}
    data['db'] = Colaboradores.objects.all()
    return render(request, 'listaColaboradores.html', data)





# ===============================   =================================  ===========================   ================================ ===============================
# ===============================   =================================  VISUALIZAÇÃO DE FORMULÁRIOS   ================================ ================================

# ===========================================================================
# Visualização de Formulário de criação de Vagas

def form(request):
    data = {}
    data['form'] = VagasForm
    return render(request, 'vagasForm.html', data)

# ===========================================================================
# Visualização de Formulário de Cadastro de Candidato por vaga

def add(request, pk):
    data = {}
    data ['form'] = CandidatosForm
    print ('data', data)

    return render(request, 'candidatoForm.html', data)

# ===========================================================================
# Visualização de Formulário de Cadastro de Parceiros

def Cadastro_Parceiros(request):
    data = {}
    data['form'] = ParceiroForm
    return render(request, 'parceiroForm.html', data)

# ===========================================================================
# Visualização de Formulário de Cadastro de Colaboradores

def Cadastro_Colaboradores(request):
    data = {}
    data['form'] = ColaboradoresForm
    return render(request, 'ColaboradoresForm.html', data)

# ===========================================================================
# Visualização de Formulário de Cadastro de Regras de Ferias

def Cadastro_Regras(request):
    data = {}
    data['form'] = RegrasFeriasForm
    return render(request, 'regrasFeriasForm.html', data)

# ===========================================================================
# Visualização de Formulário de Cadastro de Ferias

def Cadastro_Ferias(request):
    data = {}
    data['form'] = DefinirFeriasForm
    return render(request, 'feriasForm.html', data)



# ===============================   =================================  ===============   ================================ ===============================
# ===============================   =================================  INSERT EM BANCO   ================================ ================================

# ===========================================================================
# Salvando formulario de criação de vagas

def create(request):
    form = VagasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

# ===========================================================================
# Salvando formulario de criação de candidatos por vagas

def createCandidate(request):
    form = CandidatosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

# ===========================================================================
# Salvando formulario de criação de parceiros

def createParceiro(request):
    form = ParceiroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

# ===========================================================================
# Salvando formulario de criação de colaboradores

def createColaborador(request):
    form = ColaboradoresForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('View_Colaboradores')

# ===========================================================================
# Salvando formulario de criação de regras de ferias

def createRegras(request):
    form = RegrasFeriasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('View_Colaboradores')

# ===========================================================================
# Salvando formulario de criação de ferias

def createFerias(request):
    form = DefinirFeriasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('View_Colaboradores')        




# ===============================   =================================  ===============   ================================ ================================
# ===============================   =================================  EDIÇÃO DE DADOS   ================================ ================================

# ===========================================================================
# Visualizando dados de vaga cadastrada dentro do formulário para alteração

def edit(request, pk):
    data = {}
    data['db'] = Vagas.objects.get(pk=pk)
    data['form'] = VagasForm(instance=data['db'])
    return render(request, 'vagasForm.html', data)

# ===========================================================================
# Visualizando dados de candidato cadastrado dentro do formulário para alteração

def editCandidate(request, pk):
    data = {}
    data['db'] = Candidatos.objects.get(pk=pk)
    data['form'] = CandidatosForm(instance=data['db'])
    return render(request, 'candidatoForm.html')




# ===============================   =================================  ===============   ================================ ================================
# ===============================   =================================  UPDATE EM BANCO   ================================ ================================    

# ===========================================================================
# Atualizando dados em banco do edit de vaga cadastrada

def update(request, pk):
    data = {}
    data['db'] = Vagas.objects.get(pk=pk)
    form = VagasForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

# ===========================================================================
# Atualizando dados em banco do edit de candidato cadastrado

def updateCandidate(request, pk):
    data = {}
    data['db'] = Candidatos.objects.get(pk=pk)
    form = CandidatosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('view')




# ===============================   =================================  ===============   ================================ ================================
# ===============================   =================================  DELETE EM BANCO   ================================ ================================

# ===========================================================================
# Deletando vaga cadastrada

def delete(request, pk):
    db = Vagas.objects.get(pk=pk)
    db.delete()
    return redirect('home')     


def all_eventes(request):
    event_list = Event.objects.all().order_by('event_date')
    return redirect('View_Colaboradores',
        {'event_list': event_list})