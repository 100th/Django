from django.shortcuts import render
from django.views.generic import ListView
from .models import Item


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
