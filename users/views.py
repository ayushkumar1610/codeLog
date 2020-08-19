from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm 

# Create your views here. Views are for which to use and where to redirect.

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    sucess_url = reverse_lazy('login')
    template_name = 'signup.html'