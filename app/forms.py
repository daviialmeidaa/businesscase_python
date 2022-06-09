from django.forms import ModelForm
from app.models import Vagas
from app.models import Candidatos

# Create the form class.
class VagasForm(ModelForm):
    class Meta:
        model = Vagas
        fields = ['vaga', 'description', 'data']

class CandidatosForm(ModelForm):
    class Meta:
        model = Candidatos
        fields = ['nome', 'vaga', 'pretensao', 'area', 'previsao', 'indicacao', 'indicador']