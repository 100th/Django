from django.shortcuts import render

def home(request):
    order_list = request.user.order_set.all()
    return render(request, 'home/main.html', {
        'order_list' : order_list,
    })
