from django.forms import ModelForm
from app.models import Vagas
from app.models import Candidatos
from app.models import Areas
from app.models import IndicacaoModel
from app.models import Parceiros

# Create the form class.
class VagasForm(ModelForm):
    class Meta:
        model = Vagas
        fields = ['vaga', 'area', 'description', 'data']

class CandidatosForm(ModelForm):
    class Meta:
        model = Candidatos
        fields = ['nome', 'vaga', 'email', 'pretensao', 'previsao', 'indicacao', 'indicador']

class AreasForm(ModelForm):
    class Meta:
        model = Areas
        fields = ['area']        

class IndicacaoForm(ModelForm):
    class Meta:
        model = IndicacaoModel
        fields = ['indicacao_poll']        
    
class ParceiroForm(ModelForm):
    class Meta:
        model = Parceiros
        fields = ['parceiro']