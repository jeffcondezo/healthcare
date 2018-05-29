from django.shortcuts import render
from django.views.generic.edit import FormView
from django.utils import timezone

# Model import-->
from .models import Paciente
# Model import<--

# Forms import-->
from .forms import PacienteForm
# Forms import<--

# Extra python features-->
# Extra python features<--


# Create your views here.

class AdmisionView(FormView):
    template_name = 'admision/admision.html'
    form_class = PacienteForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
