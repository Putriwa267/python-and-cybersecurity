from django.http import HttpResponse
from django.template import loader
from .models import Pengguna

# Create your views here.
def pengguna(request):
    context = {
        'nama': 'Anton'
    }
    template = loader.get_template('pengguna.html')
    return HttpResponse(template.render(context, request))

def penggunadb(request):
    data = Pengguna.objects.all().values()[5]
    context = {
        'data_pengguna': data
    }
    template = loader.get_template('pengguna2.html')
    return HttpResponse(template.render(context, request))
