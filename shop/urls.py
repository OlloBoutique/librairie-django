from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('livre/<int:id>/', views.detail, name="detail"),
    path('ajouter/<int:id>/', views.ajouter_panier, name="ajouter_panier"),
    path('panier/', views.panier, name="panier"),
    path('supprimer/<int:id>/', views.supprimer_panier, name='supprimer_panier'),
    path('commander/', views.commander, name='commander'),
]

