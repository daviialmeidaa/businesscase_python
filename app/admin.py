from django.contrib import admin
from app.models import Vagas
from app.models import Candidatos
from app.models import Areas
from app.models import IndicacaoModel
from app.models import Parceiros
from app.models import Colaboradores
from app.models import regras_ferias
from app.models import Modalidades


# from app.models import Candidatos
# Register your models here.

admin.site.register(Areas)
admin.site.register(IndicacaoModel)
admin.site.register(Parceiros)
admin.site.register(Vagas)
admin.site.register(Candidatos)
admin.site.register(Modalidades)
admin.site.register(Colaboradores)
admin.site.register(regras_ferias)