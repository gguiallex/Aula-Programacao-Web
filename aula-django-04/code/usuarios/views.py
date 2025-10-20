from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        usuario = request.POST.get('usuario')
        email = request.POST.get('email') 
        senha = request.POST.get('senha')
        return HttpResponse(usuario)
