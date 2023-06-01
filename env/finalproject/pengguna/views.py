from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pengguna(request):
    return HttpResponse("Selamat Datang Pengguna")
