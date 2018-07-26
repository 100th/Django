from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from .models import Item, Order
from .forms import PayForm


class ItemListView(ListView):
    model = Item
    queryset = Item.objects.filter(is_public=True)

    # 검색하면 그 Item만 보여지도록 Queryset 설정
    def get_queryset(self):
        self.q = self.request.GET.get('q', '')   # q가 있으면 가져오고, 없으면 공백
        qs = super().get_queryset()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs

    # 검색하면 어떤 것 검색했는지 검색창에 글자로 남아있도록
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.q
        return context


index = ItemListView.as_view() #(model=Item, queryset=Item.objects.filter(is_public=True))


@login_required
def order_new(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    order = Order.objects.create(user=request.user, item=item, name=item.name, amount=item.amount)
    return redirect('shop:order_pay', item_id, str(order.merchant_uid))


@login_required
def order_pay(request, item_id, merchant_uid):
    order = get_object_or_404(Order, user=request.user, merchant_uid=merchant_uid, status='ready')
    
    if request.method == 'POST':
        form = PayForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PayForm(instance=order)
    return render(request, 'shop/pay_form.html', {
        'form': form,
        })
