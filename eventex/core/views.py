from django.shortcuts import render

def home(request):
    # Render renderiza o request dentro do templete
    return render(request, 'index.html')
