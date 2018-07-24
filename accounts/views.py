from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    order_list = request.user.order_set.all()
    # order_list = Order.objects.filter(user=request.user) 위랑 같음
    return render(request, 'accounts/profile.html', {
        'order_list' : order_list,
    })
