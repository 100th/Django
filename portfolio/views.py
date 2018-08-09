from django.shortcuts import render

def portfolio(request):
    return render(request, 'portfolio/main.html', {
    })
