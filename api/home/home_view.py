from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from api.home.valid_const import URL_LOGIN

# Create your views here.
@login_required(login_url=URL_LOGIN)
def home_views(request):
    template_name = 'index.html'
    
    return render(request,template_name)