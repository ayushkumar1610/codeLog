from django.views.generic import TemplateView # This generic view lets view exact view as template

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'
    