from django.views.generic import ListView
from .models import Dbapp

class HomePageView(ListView):
    model = Dbapp
    template_name = 'home.html'
