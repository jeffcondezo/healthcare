# urls.py
from django.urls import path
from admision.views import AdmisionView

urlpatterns = [
    path('', AdmisionView.as_view()),
]