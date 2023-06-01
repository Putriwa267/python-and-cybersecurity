from django.http import HttpResponse
from django.template import loader

# Create your views here.
def pengguna(request):
    template = loader.get_template('pengguna.html')
    return HttpResponse(template.render())
