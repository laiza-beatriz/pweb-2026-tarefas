from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def usuarios(request):
    lista_usuarios = [
        {"nome": 'Alice', "matricula": '12345', "idade": 25, "cidade": 'São Paulo do Potengi'},
        {"nome": 'Bob', "matricula": '67890', "idade": 30, "cidade": 'São Pedro'},
        {"nome": 'Charlie', "matricula": '54321', "idade": 35, "cidade": 'Barcelona'},
        {"nome": 'Samuelly', "matricula": '98765', "idade": 28, "cidade": 'São Tomé'},
        {"nome": 'David', "matricula": '45678', "idade": 32, "cidade": 'Cajazeiras'}
    ]
    context = {
        "usuarios": lista_usuarios
    }

    return render(request, 'usuarios.html', context)
