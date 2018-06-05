# urls.py
from django.urls import path
from admision.views import AdmisionView, Prueba1View, Prueba2View

urlpatterns = [
    path('', AdmisionView.as_view()),
    path('prueba1', Prueba1View.as_view()),
    path('prueba2', Prueba2View.as_view()),
]