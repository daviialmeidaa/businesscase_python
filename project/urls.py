"""project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import home, form, create, edit, update, delete, add, view, createCandidate, editCandidate, Cadastro_Parceiros, createParceiro, Cadastro_Colaboradores, View_Colaboradores, createColaborador, Cadastro_Regras, createRegras, Cadastro_Ferias, createFerias

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),    
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('add/<int:pk>/', add, name='add'),
    path('createCandidate/', createCandidate, name='createCandidate'),
    path('view/<int:pk>/', view, name='view'),
    path('editCandidate/<int:pk>/', editCandidate, name='editCandidate'),
    path('Cadastro_Parceiros/', Cadastro_Parceiros, name='Cadastro_Parceiros'),
    path('createParceiro/', createParceiro, name='createParceiro'),
    path('Cadastro_Colaboradores/', Cadastro_Colaboradores, name='Cadastro_Colaboradores'),
    path('View_Colaboradores/', View_Colaboradores, name='View_Colaboradores'),
    path('createColaborador/', createColaborador, name='createColaborador'),
    path('Cadastro_Regras/', Cadastro_Regras, name='Cadastro_Regras'),
    path('createRegras/', createRegras, name='createRegras'),
    path('Cadastro_Ferias/', Cadastro_Ferias, name='Cadastro_Ferias'),
    path('createFerias/', createFerias, name='createFerias'),
    ]

